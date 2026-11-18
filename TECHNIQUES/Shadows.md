# TECHNIQUE — Shadows

**Purpose:** Build physically believable contact and cast shadows that anchor the subject to the environment.
**Last updated:** 2026-11-18

---

## 1. Core concepts

- **Contact shadow** — the dark, tight occlusion where the subject meets the ground/contact surface. Essential for grounding.
- **Cast shadow** — the projected shadow from the subject onto the environment, direction determined by the light source.
- **Shadow softness** — depends on light source size and distance; hard sun = sharp edge, overcast = soft.
- **Shadow length** — depends on light elevation (time of day).
- **Ambient occlusion** — subtle darkening in crevices and where forms meet.

## 2. Analysis workflow

1. Identify the light direction and elevation from existing shadows in the original.
2. Note shadow edge softness and opacity.
3. Determine the subject's contact points with the ground.
4. Derive the cast shadow shape from the subject's silhouette and the ground plane.

## 3. Reconstruction rules

- Contact shadows are non-negotiable; without them the subject floats.
- Cast shadow direction must agree with the environment's light source.
- Shadow softness and opacity must match the original lighting conditions.
- Shadows must follow the ground plane's perspective (they are not flat stickers).
- Preserve any existing shadows in the original where the subject is unchanged.

## 4. Common mistakes

| Symptom | Cause |
|---|---|
| Floating subject | Missing or too-weak contact shadow |
| Shadow points the wrong way | Light direction not matched |
| Shadow too hard/soft | Light quality mismatch |
| Shadow breaks perspective | Not projected onto the ground plane correctly |

## 5. Verification

- Toggle the shadow layer on/off to confirm it changes the perceived grounding.
- Compare shadow direction against a known environmental shadow.
- Check that shadow length is consistent with the light elevation.
