# Project 002 — Boxer Striking a Speed Bag

## Status

**No Project 002 composite is approved.** `Working_Composites/boxing-speedbag-draft-v1.png` was explicitly rejected as “really bad”; do not reuse it as a quality reference, style benchmark, or base. A later scene-aware generation attempt also altered the subject; the user rejected those options, none was selected or saved, and they must not be used. **The supplied original subject photo is immutable:** no AI redraw, retouch, relight, recolor, resize, crop, warp, or substituted subject pixels. Preserve the original file and restore the original subject from it before showing any candidate. The generator in this workspace has no reliable pixel-lock mask, so generated subject pixels are never final.

## Inputs

- `Original_Images/boxer-strike-original.png` — supplied side-on boxer in a forward punch, full-body stance on a white studio background. Sole source of the athlete; preserve this exact photograph and subject.
- `Environment_References/speed-bag-gym-reference.png` — supplied speed-bag and industrial gym reference. It contains a different boxer; use only the bag and environmental cues, never that person.
- Global quality reference: `../../COMPOSITING_KNOWLEDGE/References/boxing-gym-editorial-user-benchmark.png` — mood/quality reference only; not a subject source or fixed plate.

## User direction

- Add a speed bag based on the supplied reference.
- Place the action in a slightly different area of the established industrial gym, not the same exact background plate used for Project 001.
- Carry forward the editorial quality/style: portrait framing, moody industrial atmosphere, natural depth, and convincing integration.
- Preserve the supplied subject photo unchanged: do not regenerate, retouch, relight, recolor, resize, crop, warp, or alter him or his pose. The existing fist points toward frame-left; align the bag with that motion.
- Keep him outside a boxing ring. Do not add a ring or unrelated scene elements.

## Camera/environment analysis

The source is a 1707 × 2560 portrait with a strong side-on stance and fist extended toward frame-left. The environment reference is a 1080 × 1340 portrait with an industrial beam, concrete/brick walls and a suspended teardrop speed bag; its boxer must not become a second foreground subject. The source has bright studio lighting; adapt the environment to the source's unmodified lighting rather than relighting the athlete.

## Existing rejected working files

- `Working_Composites/boxing-speedbag-draft-v1.png` — 848 × 1264 cutout-and-paste draft; rejected as “really bad.” Historical only; do not reuse, polish, approve, or cite as a quality reference.
- `Working_Composites/speedbag-environment-plate-v1.png` — generated environment-only plate, not a source photograph or approved background. Historical only; not a standalone compositing method.
- The later scene-aware generation options changed the subject. The user rejected them, none was selected or saved, and they are not approved or usable as composites.

## Revised workflow before any new composite

Follow `../../TECHNIQUES/Compositing_Pipeline.md`. Scene-aware generation may explore environment/layout, but it cannot supply final subject pixels. The current image tool has no reliable protected-pixel mask. If a generated image contains an altered boxer, use it only as a scene/layout reference or discard it. Before presenting any candidate, restore the athlete from `Original_Images/boxer-strike-original.png`, make no subject retouch or color/light changes, and verify against the source. Use matte extraction only to separate the source foreground; do not run rim/color cleanup on the boxer. Build the environment and contact treatment around the unchanged source subject. The rejected draft and empty plate are not bases for another attempt.

Keep the boxer outside the ring; no ring, unwanted person, or gym-name text. Match the environment to the original light and camera geometry, with plausible bag suspension and shadows. Protect white socks/shoes and colorful details. Keep original files untouched; do not mark any new version approved without explicit user approval.
