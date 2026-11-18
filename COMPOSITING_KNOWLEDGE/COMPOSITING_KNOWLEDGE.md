# COMPOSITING KNOWLEDGE

**Purpose:** Living, general (non-project-specific) knowledge base for Viper Visuals photographic compositing.
**Last updated:** 2026-11-18
**Related:** `MASTER_INSTRUCTIONS.md` (role & workflow), `VISUAL_STANDARDS.md` (quality bar), `TECHNIQUES/` (deep technical reference), `CORRECTIONS_LOG.md` (lessons), `APPROVED_REFERENCES.md` (benchmarks).

---

## 1. Core Doctrine

1. **The original photograph is the source of truth.** The subject, its detail and its photographic character are preserved; the environment is reconstructed.
2. **The environment adapts to the camera, not the camera to a fixed plate.** A single approved composite defines look and materials, not a reusable background image.
3. **Photographic realism over stylization.** Every choice must be defensible as something a camera could have captured.
4. **Quality is non-negotiable.** Resolution, texture, grain, sharpness and natural lighting transitions are preserved or improved — never degraded.
5. **Knowledge compounds.** Every correction and success is written back to this repository.

---

## 2. Analysis Before Action

Before touching an image, record (in the project notes) the following for every source photograph:

| Attribute | What to determine |
|---|---|
| Camera height | Eye level / low / elevated / overhead |
| Camera angle | Frontal / three-quarter / profile / low / high |
| Lens character | Wide (stretched perspective), standard, telephoto (compressed) |
| Subject scale | Proportion of frame occupied |
| Ground plane | Surface type, slope, horizon height in frame |
| Horizon / vanishing points | Estimated positions for geometry checks |
| Lighting | Direction, quality (hard/soft), colour temperature, ambient level |
| Shadows | Direction, length, softness, contact vs. cast |
| Depth of field | Focal plane, background blur amount |
| Background perspective | Recession direction and scale cues |

Two photos from the same shoot are **never** assumed to share perspective. Verify before matching.

---

## 3. Environment Reconstruction Principles

- Establish the environment once (from a reference or approved composite), then **re-derive** it for each camera angle.
- Keep a consistent **environment bible** per project: geometry, materials, colours, key background elements, lighting direction.
- Rebuild perspective cues per image: lane lines, tile grids, architectural edges, shadows, ground texture scale.
- Match horizon height and vanishing-point placement to each photo's camera.
- Keep lighting physically believable; do not copy a lighting rig into a photo taken at a different time/angle without adapting it.

---

## 4. Subject Preservation Rules

- Mask/extract the subject from the **original full-resolution** capture.
- Never re-generate the subject's face, identity, proportions, pose, clothing or hair.
- Preserve skin texture and fabric detail; no smoothing, no re-lighting that erases micro-texture.
- Preserve original grain character; match grain when adding environment.
- Keep the original composition and subject positioning unless a change is explicitly requested.

---

## 5. Integration Checklist

- [ ] Subject scale consistent with environment geometry.
- [ ] Contact shadow present and correct at the subject's feet/contact points.
- [ ] Cast shadow direction consistent with environment light source.
- [ ] Light wrap / ambient bounce from environment onto subject is plausible.
- [ ] Colour temperature and exposure matched between subject and environment.
- [ ] Depth of field consistent (background blur matches lens/camera of original).
- [ ] Atmospheric depth (haze, contrast falloff) consistent with distance.
- [ ] Grain/noise matched across subject and environment.
- [ ] Edge quality: no halos, fringes, or cut-out artifacts.
- [ ] Resolution and sharpness preserved; no invented detail.

---

## 6. Common Failure Modes (to watch for)

| Symptom | Likely cause | First check |
|---|---|---|
| "Cut-out" / sticker look | Missing contact shadow, mismatched grain, colour temp | Contact shadow + grain |
| Plastic skin | Over-processing, subject regeneration, smoothing | Return to original subject |
| Floating subject | Wrong ground plane / shadow direction | Horizon + VP alignment |
| Fake-looking environment | Fixed plate reused at wrong angle | Reconstruct per-camera |
| Muddy / flat image | Over-sharpening, HDR, excessive contrast | Process pipeline |
| Wrong scale | Subject scale vs. environment cues | Perspective cues |

---

## 7. Lessons Learned

> This section is appended over time. Each entry should reference a `CORRECTIONS_LOG.md` ID.

*(No entries yet — the knowledge base has just been established.)*
