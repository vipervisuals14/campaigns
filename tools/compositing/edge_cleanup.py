"""Deterministic Stage 3 edge cleanup for editorial sports composites.

All image arrays are RGB uint8 unless otherwise documented. This module never calls
an image-generation model; its edits are restricted to the detected subject boundary.
"""
from __future__ import annotations

import numpy as np
import cv2


def detect_white_rim_heatmap(
    img_rgb: np.ndarray,
    fg_mask: np.ndarray,
    band_px: int = 8,
    luma_thresh: float = 95.0,
) -> tuple[np.ndarray, np.ndarray]:
    """Flag bright pixels in an outer subject edge band; return mask and diagnostic RGB."""
    if img_rgb.ndim != 3 or img_rgb.shape[2] != 3:
        raise ValueError("img_rgb must be an HxWx3 RGB array")
    if fg_mask.shape[:2] != img_rgb.shape[:2]:
        raise ValueError("fg_mask dimensions must match img_rgb")
    if band_px < 1:
        raise ValueError("band_px must be >= 1")
    fg = (fg_mask > 0).astype(np.uint8)
    bg = (fg == 0).astype(np.uint8)
    k = 2 * band_px + 1
    dil = cv2.dilate(bg, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (k, k)))
    edge_band = (dil > 0) & (fg > 0)
    luma = (0.299 * img_rgb[:, :, 0] + 0.587 * img_rgb[:, :, 1] + 0.114 * img_rgb[:, :, 2])
    rim_mask = edge_band & (luma > luma_thresh)
    diag = img_rgb.copy()
    diag[rim_mask] = [0, 255, 80]
    return rim_mask, diag


def extract_nocturnal_sky_fg_mask(
    roi_rgb: np.ndarray, min_sky_area: int = 120
) -> np.ndarray:
    """Color-key a cool dark sky for the dedicated nocturnal-track workflow only."""
    if roi_rgb.ndim != 3 or roi_rgb.shape[2] != 3:
        raise ValueError("roi_rgb must be an HxWx3 RGB array")
    R, G, B = roi_rgb[:, :, 0], roi_rgb[:, :, 1], roi_rgb[:, :, 2]
    luma = 0.299 * R + 0.587 * G + 0.114 * B
    sky_raw = (R <= 15) & (G <= 27) & (B <= 48) & ((B - R) >= 6.0) & (luma <= 26.0)
    n, labels, stats, _ = cv2.connectedComponentsWithStats(sky_raw.astype(np.uint8), connectivity=8)
    clean_sky = np.zeros_like(labels, dtype=np.uint8)
    for label in range(1, n):
        if stats[label, cv2.CC_STAT_AREA] >= min_sky_area:
            clean_sky[labels == label] = 1
    return (1 - clean_sky).astype(np.uint8)


def build_auto_protection_mask(
    roi_rgb: np.ndarray,
    footwear_boxes: list[tuple[int, int, int, int]] | None = None,
    accessory_boxes: list[tuple[int, int, int, int]] | None = None,
    exclude_boxes: list[tuple[int, int, int, int]] | None = None,
) -> tuple[np.ndarray, np.ndarray]:
    """Protect intentional white/color detail; boxes use ROI-local (x0,y0,x1,y1)."""
    rh, rw, channels = roi_rgb.shape
    if channels != 3:
        raise ValueError("roi_rgb must be an HxWx3 RGB array")
    R, G, B = roi_rgb[:, :, 0], roi_rgb[:, :, 1], roi_rgb[:, :, 2]
    luma = 0.299 * R + 0.587 * G + 0.114 * B
    sat = np.max(roi_rgb, axis=2) - np.min(roi_rgb, axis=2)

    acc_mask = np.zeros((rh, rw), dtype=np.float32)
    for x0, y0, x1, y1 in accessory_boxes or []:
        x0, y0, x1, y1 = _clip_box((x0, y0, x1, y1), rw, rh)
        sub_sat = (sat[y0:y1, x0:x1] > 58.0).astype(np.float32)
        acc_mask[y0:y1, x0:x1] = cv2.GaussianBlur(sub_sat, (3, 3), 0.7)

    fw_zone = np.zeros((rh, rw), dtype=bool)
    for box in footwear_boxes or []:
        x0, y0, x1, y1 = _clip_box(box, rw, rh)
        fw_zone[y0:y1, x0:x1] = True
    is_skin_tone = (R > G + 14) & (G > B + 6) & (R < 215) & ((R - G) < 85)
    is_white_part = (luma > 125) & (sat < 48) & (~is_skin_tone)
    is_red_part = (R > 110) & ((R - G) > 55)
    is_blue_sole = (B > R + 20) & (luma > 35)
    fw_keep = fw_zone & (is_white_part | is_red_part | is_blue_sole)
    fw_protect = cv2.dilate(
        fw_keep.astype(np.uint8), cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    ).astype(np.float32)

    for box in exclude_boxes or []:
        x0, y0, x1, y1 = _clip_box(box, rw, rh)
        acc_mask[y0:y1, x0:x1] = 0.0
        fw_protect[y0:y1, x0:x1] = 0.0
    fw_protect = cv2.GaussianBlur(fw_protect, (3, 3), 0.8)
    return np.clip(np.maximum(acc_mask, fw_protect), 0.0, 1.0), fw_protect


def _clip_box(box: tuple[int, int, int, int], width: int, height: int) -> tuple[int, int, int, int]:
    x0, y0, x1, y1 = box
    x0, x1 = max(0, min(width, x0)), max(0, min(width, x1))
    y0, y1 = max(0, min(height, y0)), max(0, min(height, y1))
    if x1 <= x0 or y1 <= y0:
        raise ValueError(f"Empty or invalid box: {box}")
    return x0, y0, x1, y1


def remove_studio_white_rim(
    img_u8: np.ndarray,
    fg_mask: np.ndarray | None = None,
    roi_box: tuple[int, int, int, int] | None = None,
    footwear_boxes: list[tuple[int, int, int, int]] | None = None,
    accessory_boxes: list[tuple[int, int, int, int]] | None = None,
    exclude_boxes: list[tuple[int, int, int, int]] | None = None,
    fingertip_boxes: list[tuple[int, int, int, int]] | None = None,
    skin_cap_rgb: tuple[float, float, float] = (124.0, 80.0, 58.0),
    rim_width_px: float = 11.0,
    min_grazing_mult: float = 0.40,
    grain_std: float = 1.1,
    seed: int = 42,
) -> np.ndarray:
    """Reduce studio-white edge spill only near a foreground boundary.

    `img_u8` must be RGB. `fg_mask` is HxW with 0/255 (or boolean) foreground.
    All boxes are global image coordinates; `roi_box` is (x0,y0,x1,y1).
    Returns RGB uint8. Always inspect the diagnostic mask and final edge crops.
    """
    if img_u8.dtype != np.uint8 or img_u8.ndim != 3 or img_u8.shape[2] != 3:
        raise ValueError("img_u8 must be an HxWx3 RGB uint8 array")
    H, W, _ = img_u8.shape
    x0, y0, x1, y1 = roi_box if roi_box is not None else (0, 0, W, H)
    x0, y0, x1, y1 = _clip_box((x0, y0, x1, y1), W, H)
    roi = img_u8[y0:y1, x0:x1].astype(np.float32)
    rh, rw, _ = roi.shape

    def to_local(boxes):
        if not boxes:
            return []
        result = []
        for ax, ay, bx, by in boxes:
            result.append(_clip_box((ax - x0, ay - y0, bx - x0, by - y0), rw, rh))
        return result

    if fg_mask is None:
        fg = extract_nocturnal_sky_fg_mask(roi.astype(np.uint8))
    else:
        if fg_mask.shape[:2] != (H, W):
            raise ValueError("fg_mask dimensions must match img_u8")
        fg = (fg_mask[y0:y1, x0:x1] > 0).astype(np.uint8)
    dist_in = cv2.distanceTransform(fg, cv2.DIST_L2, 5)

    edge_inpaint = ((fg > 0) & (dist_in <= 6.0)).astype(np.uint8)
    bg_inpainted = np.zeros_like(roi)
    for channel in range(3):
        bg_inpainted[:, :, channel] = cv2.inpaint(
            roi[:, :, channel].astype(np.uint8), edge_inpaint, 7, cv2.INPAINT_TELEA
        ).astype(np.float32)
    bg_local = cv2.GaussianBlur(bg_inpainted, (15, 15), 4.0)

    protect, fw_protect = build_auto_protection_mask(
        roi, footwear_boxes=to_local(footwear_boxes),
        accessory_boxes=to_local(accessory_boxes), exclude_boxes=to_local(exclude_boxes)
    )
    dist_smooth = cv2.GaussianBlur(dist_in, (9, 9), 2.2)
    gx = cv2.Sobel(dist_smooth, cv2.CV_32F, 1, 0, ksize=5)
    gy = cv2.Sobel(dist_smooth, cv2.CV_32F, 0, 1, ksize=5)
    gnorm = np.sqrt(gx * gx + gy * gy) + 1e-6
    nx, ny = gx / gnorm, gy / gnorm
    yy, xx = np.mgrid[0:rh, 0:rw].astype(np.float32)

    low = cv2.GaussianBlur(roi, (5, 5), 1.1)
    high = roi - low
    luma = 0.299 * roi[:, :, 0] + 0.587 * roi[:, :, 1] + 0.114 * roi[:, :, 2]
    low_luma = 0.299 * low[:, :, 0] + 0.587 * low[:, :, 1] + 0.114 * low[:, :, 2]
    local_thick = cv2.dilate(dist_in, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (19, 19)))
    step1 = np.clip(9.5 - dist_in, 0.0, np.maximum(local_thick - dist_in + 1.0, 2.5))
    step2 = np.clip(14.5 - dist_in, 0.0, np.maximum(local_thick - dist_in + 2.0, 3.5))
    ref1 = cv2.remap(low, np.clip(xx + nx * step1, 0, rw - 1), np.clip(yy + ny * step1, 0, rh - 1), cv2.INTER_LINEAR)
    ref2 = cv2.remap(low, np.clip(xx + nx * step2, 0, rw - 1), np.clip(yy + ny * step2, 0, rh - 1), cv2.INTER_LINEAR)
    l1 = 0.299 * ref1[:, :, 0] + 0.587 * ref1[:, :, 1] + 0.114 * ref1[:, :, 2]
    l2 = 0.299 * ref2[:, :, 0] + 0.587 * ref2[:, :, 1] + 0.114 * ref2[:, :, 2]
    ref = np.where(((l2 < l1) & (l2 > 14.0))[:, :, None], ref2, ref1)
    l_ref = 0.299 * ref[:, :, 0] + 0.587 * ref[:, :, 1] + 0.114 * ref[:, :, 2]
    cap = np.array(skin_cap_rgb, dtype=np.float32)[None, None, :]
    too_bright = np.clip((l_ref - 90.0) / 68.0, 0.0, 0.85)[:, :, None]
    ref_clean = ref * (1.0 - too_bright) + cap * too_bright

    ft_zone = np.zeros((rh, rw), dtype=np.float32)
    for fx0, fy0, fx1, fy1 in to_local(fingertip_boxes):
        ft_zone[fy0:fy1, fx0:fx1] = 1.0
    if fingertip_boxes:
        ft_zone = cv2.GaussianBlur(ft_zone, (15, 15), 4.5)

    t = np.clip((dist_in - 0.7) / 9.0, 0.0, 1.0)
    t_smooth = t * t * (3.0 - 2.0 * t)
    min_m = min_grazing_mult + 0.18 * ft_zone
    grazing_mult = min_m + (1.0 - min_m) * t_smooth
    target_low = ref_clean * grazing_mult[:, :, None]
    target_luma = 0.299 * target_low[:, :, 0] + 0.587 * target_low[:, :, 1] + 0.114 * target_low[:, :, 2]
    ew = np.clip((rim_width_px - dist_in) / (rim_width_px - 3.2), 0.0, 1.0)
    ew = ew * ew * (3.0 - 2.0 * ew) * (fg > 0).astype(np.float32) * (1.0 - protect)
    excess = np.clip((low_luma - target_luma) / 20.0, 0.0, 1.0)
    blend_w = ew * excess
    new_low = low * (1.0 - blend_w[:, :, None]) + target_low * blend_w[:, :, None]

    cloth_edge = np.clip((5.0 - dist_in) / 3.4, 0.0, 1.0) * (fg > 0).astype(np.float32) * (1.0 - protect)
    is_dark = np.clip((38.0 - l_ref) / 18.0, 0.0, 1.0)
    dark_flare = np.clip((low_luma - (l_ref * 0.82 + 1.5)) / 12.0, 0.0, 1.0)
    w_dark = cloth_edge * is_dark * dark_flare
    dark_target = ref * 0.70 + bg_local * 0.30
    new_low = new_low * (1.0 - w_dark[:, :, None]) + dark_target * w_dark[:, :, None]

    new_luma = 0.299 * new_low[:, :, 0] + 0.587 * new_low[:, :, 1] + 0.114 * new_low[:, :, 2]
    ratio = np.clip((new_luma + 8.0) / (low_luma + 8.0), 0.22, 1.0)[:, :, None]
    high_scaled = np.where(high > 0, high * (ratio ** 1.65), high * ratio)
    out_roi = new_low + high_scaled
    subpx = np.clip((2.15 - dist_in) / 1.55, 0.0, 1.0) * (fg > 0).astype(np.float32) * (1.0 - protect)
    orig_rim_flag = np.clip((luma - 36.0) / 52.0, 0.18, 0.72)
    w_bg = (subpx * orig_rim_flag)[:, :, None]
    out_roi = out_roi * (1.0 - w_bg) + bg_local * w_bg

    fw_edge = (np.clip((3.5 - dist_in) / 2.8, 0.0, 1.0) * (fg > 0) * fw_protect)[:, :, None]
    cool_shade = out_roi * np.array([0.76, 0.81, 0.88], dtype=np.float32)
    out_roi = out_roi * (1.0 - 0.58 * fw_edge) + cool_shade * (0.58 * fw_edge)
    fw_1px = (np.clip((1.75 - dist_in) / 1.15, 0.0, 1.0) * (fg > 0) * fw_protect)[:, :, None]
    out_roi = out_roi * (1.0 - 0.40 * fw_1px) + bg_local * (0.40 * fw_1px)

    rng = np.random.default_rng(seed)
    grain = rng.normal(0.0, grain_std, size=(rh, rw, 1)).astype(np.float32)
    mod_mask = np.clip(np.maximum(blend_w, w_dark), 0.0, 1.0)[:, :, None]
    out_roi = np.clip(out_roi + grain * mod_mask * 0.65, 0.0, 255.0)
    result = img_u8.copy()
    result[y0:y1, x0:x1] = np.round(out_roi).astype(np.uint8)
    return result
