# Local compositing utilities

These helpers implement only deterministic matting/edge QA stages; they do not call an image-generation provider. The Stage 1/2 candidate-generation process and provider caveats are documented in `../../TECHNIQUES/Compositing_Pipeline.md`.

## Install

```bash
python -m pip install -r tools/compositing/requirements.txt
```

`rembg` downloads ONNX weights on first model use and may need network access to its model host. Those weights have not been fetched in this repository. `pymatting` is optional for future trimap workflows. The `edge_cleanup.py` utilities require only NumPy and OpenCV.

## Use

- Convert images to RGB `uint8`; ensure the matte is aligned to the same original-resolution pixels.
- For indoor scenes, call `extract_fused_athlete_mask()` with manually reviewed white-garment boxes. Review `detect_white_rim_heatmap()` before applying `remove_studio_white_rim()`.
- For its dedicated dark-sky case only, `remove_studio_white_rim(..., fg_mask=None)` uses the nocturnal color key; do not use this mode on a gym.
- Run edge cleanup on a working copy, preserve the raw photo, use footwear/accessory protection boxes, and inspect output at 100% before export.
- Save lossless PNG and compare unchanged regions to the source. No universal pixel-preservation percentage is promised.

## Tests

```bash
python -m unittest discover -s tools/compositing/tests -v
```
