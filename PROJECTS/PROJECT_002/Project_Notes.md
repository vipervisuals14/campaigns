# Project 002 — Boxer Striking a Speed Bag

## Status

**Rejected by the user as “really bad.”** `Working_Composites/boxing-speedbag-draft-v1.png` is not approved and must not be used as a quality reference, style benchmark, or base for polishing. The earlier cutout-over-empty-plate method is retired as the main composition approach. No Project 002 composite is approved.

## Inputs

- `Original_Images/boxer-strike-original.png` — supplied side-on boxer in a forward punch, full-body stance on a white studio background. Preserve this exact photographed subject, pose and clothing.
- `Environment_References/speed-bag-gym-reference.png` — supplied speed-bag and industrial gym reference. It contains a different boxer; use the bag and environmental cues, not that person as a subject.
- Global quality reference: `../../COMPOSITING_KNOWLEDGE/References/boxing-gym-editorial-user-benchmark.png`.

## User direction

- Add a speed bag based on the second supplied image.
- Place the action in a slightly different area of the established industrial gym, not the same exact background plate used for Project 001.
- Carry forward the user's requested editorial quality/style: portrait framing, moody industrial atmosphere, natural depth, and convincing integration.
- Preserve the supplied subject unchanged; do not regenerate him or alter his pose. Align the speed bag with his existing punch so it reads as a strike.
- Keep him outside a boxing ring. Do not add a ring or invent unrelated scene elements.

## Camera/environment analysis

The source is a 1707 × 2560 portrait with a strong side-on stance and fist extended toward frame-left. The environment reference is a 1080 × 1340 portrait with an industrial beam, concrete/brick walls and a suspended teardrop speed bag; the reference also contains another boxer that must not become a second foreground subject. The source's punch direction can naturally meet the speed bag. The source has bright studio lighting; the environment is warmer, dimmer and directional, so match integration conservatively without retouching the source subject.

## Existing rejected working files

- `Working_Composites/boxing-speedbag-draft-v1.png` — 848 × 1264 cutout-and-paste draft; explicitly rejected by the user as “really bad.” Retained as historical work only. Do not reuse, polish, approve, or cite it as a quality reference.
- `Working_Composites/speedbag-environment-plate-v1.png` — generated environment-only plate, not a source photograph or approved background. Retained for history only; it is not a standalone compositing method.

## Revised workflow before any new composite

Use the scene-aware three-stage workflow in `../../TECHNIQUES/Compositing_Pipeline.md`. For a new Stage 1 attempt, submit the original subject photo first, the speed-bag/gym reference second, and an optional prop reference third. Generate two distinct scene-aware candidates in parallel for A/B selection; do not use the rejected draft or the empty plate as the base. Any targeted Stage 2 refinement must include both the current candidate and the original raw subject image, and change one objective only. Stage 3 uses the deterministic, inspectable OpenCV helpers under `../../tools/compositing/` for local edge cleanup and QA.

Preserve the exact original subject, pose, identity, skin texture, clothing, logos and camera geometry. Keep the boxer outside the ring; no ring, unwanted person or gym-name text. Match one motivated light, environmental falloff, plausible bag interaction, contact/cast shadows, depth of field and grain. Protect white socks/shoes and colorful detail. Keep original files untouched and do not mark any new version approved without explicit user approval.
