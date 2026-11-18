# TECHNIQUE — Perspective

**Purpose:** Match and reconstruct camera perspective so composites belong to the same physical space.
**Last updated:** 2026-11-18

---

## 1. Core concepts

- **Camera height** determines where the horizon sits in frame and how much ground vs. sky is visible.
- **Camera angle** (tilt/rotation) determines convergence of vertical and horizontal lines.
- **Focal length** determines perspective compression: wide lenses stretch near/far relationships; telephoto lenses compress them.
- **Vanishing points** are where parallel lines converge; their placement is the strongest cue for matching geometry.
- **Ground plane** must be consistent: texture scale, slope and contact points must agree with the subject's position.

## 2. Analysis workflow

1. Estimate the horizon line in the original photo (eye-level line).
2. Identify two or more sets of parallel environmental lines (lane markings, tile edges, architecture).
3. Derive vanishing points from those lines.
4. Estimate camera height and focal length from the geometry.
5. Note the subject's position relative to the ground plane and horizon.

## 3. Reconstruction rules

- Rebuild the environment so its vanishing points land where the original photo's geometry dictates.
- Keep horizon height consistent across all images of the same camera position.
- Scale ground texture to the camera's distance and focal length.
- Never reuse a fixed background plate at a different camera angle.

## 4. Common mistakes

| Symptom | Cause |
|---|---|
| Floating subject | Ground plane or shadow direction wrong |
| Stretched/flattened space | Focal length mismatch |
| Lines converging incorrectly | Vanishing points misplaced |
| Inconsistent scale between shots | Subject scale not tied to perspective cues |

## 5. Verification

- Overlay perspective guides (horizon + VPs) during QC.
- Compare the same environmental edge across multiple composites.
- Check that ground texture scale changes plausibly with distance.
