# Project 002 — Boxer Striking a Speed Bag

## Status

Working draft created; not user-approved. Treat it as a draft, not an approved reference.

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

## Working composite

- `Working_Composites/boxing-speedbag-draft-v1.png` — portrait composite (848 × 1264). The boxer is cut from the supplied original photo and scaled down without pose or colour retouching; a background-only environment plate is generated from the speed-bag scene and the user's quality benchmark. The generated plate contains no people; the user's boxer is the only foreground athlete. The reference bag is aligned with the existing punch. No ring or gym name appears.
- `Working_Composites/speedbag-environment-plate-v1.png` — generated environment-only working plate, not a source photo. It reconstructs an industrial gym corner from the supplied speed-bag reference and global style benchmark. Since the reference photo contained a different boxer, this avoids retaining that person. This reconstruction is not evidence of the exact physical layout of another real area of the gym.

## Plan / quality checks

Check bag/fist contact, shoe-to-floor alignment, matte edges, perspective and lighting against the user's benchmark. The subject's original bright studio lighting differs from the warm environment; do not retouch the source person to hide that mismatch. The output is a draft for user review. Do not overwrite originals, Project 001 drafts or the style benchmark; create new versions for revisions.
