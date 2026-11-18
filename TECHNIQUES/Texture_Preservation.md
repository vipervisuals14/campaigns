# TECHNIQUE — Texture Preservation

**Purpose:** Keep the photographic micro-detail that makes a composite read as a real photograph.
**Last updated:** 2026-11-18

---

## 1. Core concepts

- **Skin texture** — pores, fine lines, micro-contrast. Destroyed by smoothing/regeneration.
- **Fabric detail** — weave, stitching, prints, wear.
- **Environmental texture** — ground grain, material surfaces, architectural detail.
- **Photographic grain/noise** — sensor grain structure; must be matched across the composite.
- **Sharpness** — authentic edge acuity without halos.

## 2. Rules

- Extract the subject from the **original full-resolution** file, not a derivative.
- Never apply global smoothing or "beauty" filters to the subject.
- Preserve grain; when extending the environment, match the grain structure of the original.
- Avoid excessive sharpening; use localized, restrained sharpening only if required.
- Do not repeatedly re-process the same pixels; return to the original each time.
- Never use a degraded AI-generated composite as a source for a new composite.

## 3. Grain matching workflow

1. Sample the original's noise/grain in a flat area.
2. Characterize size, luminance and chroma noise.
3. Apply matching grain to generated environment areas.
4. Verify at 100% zoom that grain is consistent across subject and environment.

## 4. Common mistakes

| Symptom | Cause |
|---|---|
| Plastic skin | Smoothing, regeneration, over-processing |
| Mismatched texture | Environment grain not matched to original |
| Halo artifacts | Excessive sharpening |
| Loss of detail | Downscaling then upscaling |

## 5. Verification

- Inspect at 100% zoom for skin pores, fabric weave and grain consistency.
- Compare a subject crop before/after compositing to confirm no texture loss.
- Confirm output resolution equals source resolution.
