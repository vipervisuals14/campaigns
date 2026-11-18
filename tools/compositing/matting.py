"""Optional rembg matting and source-grain utilities for Stage 3.

These helpers operate on original-resolution inputs. They do not synthesize or relight
subjects. Install the optional ONNX dependencies and model weights before use.
"""
from __future__ import annotations

import cv2
import numpy as np


def extract_fused_athlete_mask(
    img_pil: Image.Image,
    white_garment_boxes: list[tuple[int, int, int, int]] | None = None,
    session_isnet=None,
    session_human=None,
) -> np.ndarray:
    """Fuse IS-Net detail with U2Net human silhouette in white-clothing zones.

    Boxes use original-image (x0,y0,x1,y1) pixel coordinates. Sessions can be
    injected to reuse loaded ONNX models rather than reloading per image.
    """
    try:
        from rembg import new_session, remove
    except ImportError as exc:  # keep the core OpenCV cleanup importable without rembg
        raise RuntimeError('Install the optional "rembg[cpu]" dependency for matting') from exc
    if session_isnet is None:
        session_isnet = new_session("isnet-general-use")
    if session_human is None:
        session_human = new_session("u2net_human_seg")

    a_isnet = np.asarray(remove(img_pil, session=session_isnet, only_mask=True), dtype=np.float32) / 255.0
    a_human = np.asarray(remove(img_pil, session=session_human, only_mask=True), dtype=np.float32) / 255.0
    if a_isnet.shape != a_human.shape:
        raise ValueError("rembg sessions returned masks with different dimensions")
    fused = a_isnet.copy()
    h, w = fused.shape[:2]
    for x0, y0, x1, y1 in white_garment_boxes or []:
        x0, x1 = max(0, x0), min(w, x1)
        y0, y1 = max(0, y0), min(h, y1)
        if x1 <= x0 or y1 <= y0:
            raise ValueError(f"Invalid white-garment box: {(x0, y0, x1, y1)}")
        fused[y0:y1, x0:x1] = np.maximum(a_isnet[y0:y1, x0:x1], a_human[y0:y1, x0:x1])

    tight = np.clip((fused - 0.60) / 0.25, 0.0, 1.0)
    aa = cv2.GaussianBlur(tight, (0, 0), 0.85)
    alpha = np.where(tight >= 0.99, 1.0, aa)
    return np.round(alpha * 255.0).astype(np.uint8)


def unpremultiply_cyclorama_edge(img_u8: np.ndarray, alpha_u8: np.ndarray) -> np.ndarray:
    """Estimate/remove white studio contamination on semitransparent matte pixels.

    This changes edge RGB only where alpha is semi-transparent. Preserve and keep the
    original source file; visually inspect the boundary after compositing.
    """
    if img_u8.dtype != np.uint8 or img_u8.ndim != 3 or img_u8.shape[2] != 3:
        raise ValueError("img_u8 must be an HxWx3 RGB uint8 array")
    if alpha_u8.shape != img_u8.shape[:2]:
        raise ValueError("alpha_u8 must match image dimensions")
    img = img_u8.astype(np.float32)
    a = alpha_u8.astype(np.float32) / 255.0
    fg_dil = cv2.dilate((a > 0.02).astype(np.uint8), cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11)))
    bg_est = np.zeros_like(img)
    for channel in range(3):
        bg_est[:, :, channel] = cv2.inpaint(img_u8[:, :, channel], fg_dil, 9, cv2.INPAINT_TELEA).astype(np.float32)
    bg_local = cv2.GaussianBlur(bg_est, (15, 15), 4.0)
    semi = (a > 0.04) & (a < 0.98)
    a_safe = np.maximum(a, 0.12)[:, :, None]
    decontam = np.clip((img - (1.0 - a[:, :, None]) * bg_local) / a_safe, 0.0, 255.0)
    return np.round(np.where(semi[:, :, None], decontam, img)).astype(np.uint8)


def add_matched_35mm_grain(
    img_u8: np.ndarray, base_std: float = 0.85, seed: int = 7
) -> np.ndarray:
    """Add subtle luminance-weighted monochromatic sensor grain deterministically."""
    if img_u8.dtype != np.uint8 or img_u8.ndim != 3 or img_u8.shape[2] != 3:
        raise ValueError("img_u8 must be an HxWx3 RGB uint8 array")
    arr = img_u8.astype(np.float32)
    luma = (0.299 * arr[:, :, 0] + 0.587 * arr[:, :, 1] + 0.114 * arr[:, :, 2]) / 255.0
    weight = 4.0 * luma * (1.0 - luma) * 0.75 + 0.25
    rng = np.random.default_rng(seed)
    noise = rng.normal(0.0, base_std, size=(arr.shape[0], arr.shape[1])).astype(np.float32)
    noise = cv2.GaussianBlur(noise, (3, 3), 0.45)[:, :, None]
    return np.round(np.clip(arr + noise * weight[:, :, None], 0.0, 255.0)).astype(np.uint8)
