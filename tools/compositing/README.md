# Local compositing utilities

These helpers implement deterministic matting/edge QA only; they do not call an image-generation provider. The workflow and provider caveats are documented in `../../TECHNIQUES/Compositing_Pipeline.md`.

## Non-negotiable source-subject lock

The raw subject image is immutable and is the only source of final subject pixels. Keep the original file byte-for-byte. Model output that alters the subject must never be delivered; restore the foreground from the raw source before showing a candidate. Prompts do not guarantee pixel protection. In this workspace the image-generation tool has no reliable protected-pixel mask.

For a subject-preserving composite, use these utilities only to analyze/extract a matte and to QA it. Do **not** run `remove_studio_white_rim()`, `unpremultiply_cyclorama_edge()`, grain matching, relighting, recoloring, sharpening, or other pixel changes on the subject. Those functions can change RGB values and conflict with the immutable-subject rule. If a matte cannot separate the subject without unacceptable changes, stop and report the limitation.

## Install

```bash
python -m pip install -r tools/compositing/requirements.txt
```

`rembg` downloads ONNX weights on first model use and may need network access to its model host. Those weights have not been fetched in this repository. `pymatting` is optional for future trimap workflows. The `edge_cleanup.py` utilities require only NumPy and OpenCV.

## Utilities and tests

- `extract_fused_athlete_mask()` can produce an optional initial matte; manually review, especially white socks/shoes and colorful details.
- `detect_white_rim_heatmap()` can diagnose a boundary. A diagnostic is not permission to recolor subject pixels.
- The nocturnal-sky key is for that dedicated background case only, never for the gym source.
- Synthetic utility tests:

```bash
python -m unittest discover -s tools/compositing/tests -v
```
