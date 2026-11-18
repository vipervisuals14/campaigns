# Editorial Sports Compositing Pipeline

This document records the user's handoff, with the user's later correction as the controlling requirement: **the original subject image is immutable.** No visual-quality goal or image model may override that rule. Project 002's `boxing-speedbag-draft-v1.png` is rejected and must not be reused as a base or benchmark.

## Non-negotiable subject-preservation rule

- The supplied raw subject photograph is the sole source of the athlete. Never accept AI-generated, regenerated, repainted, retouched, relit, reshaped, sharpened, smoothed, or reconstructed subject pixels as final.
- Do not change the subject's identity, pose, anatomy, expression, hair, skin/pores, clothing, logos, colors, proportions, camera geometry, sharpness, or original lighting. No scaling, warping, cropping, or generative edits to the subject.
- Preserve the original file byte-for-byte. For the composite, use the original image pixels as the foreground source; any matte/alpha is solely for separating the white background and must not be used to recolor or retouch the athlete. Keep opaque subject pixels copied from the raw source; any antialiased transition is confined to the smallest necessary boundary.
- The image-generation/editing tool does not offer a reliable protected-pixel mask in this workspace. Therefore a generated image that contains the athlete is **never itself an acceptable final composite**, even if a prompt asked it to preserve him. Use such an output only as a scene/layout reference or background source; restore the original photographed subject from the raw file before presenting a result. If the subject cannot be restored without unacceptable artifacts, stop and ask rather than silently altering him.
- Do not present A/B candidates for selection until the subject pixels have been restored from the original and the result checked against it. A candidate in which the subject changed must be discarded. The latest two generated options were not selected and are not saved or approved.

## Workflow correction

A plain subject cutout pasted onto an empty generated plate was previously rejected as a quality approach. The correction is **not** to let a generator redraw the subject. Instead, use generation only to explore or construct scene context, then build an integrated background/contact/shadow treatment around the immutable source subject. Restore the original subject pixels as a locked foreground after any generative scene pass. Scene-aware generation can guide bag placement, room geometry, lighting and shadows, but never supplies the final athlete. If the platform cannot retain the original subject, its output is a reference only.

## Three-stage hybrid workflow

### Stage 1 — scene/context candidates with subject lock

1. Analyze the raw subject photograph: camera height/tilt, lens and perspective, horizon, framing, pose/action vector, original light direction/quality/colour, contrast, clothing/logos and footwear. For Project 002, keep the original portrait framing and full figure; the extended fist points toward frame-left.
2. Supply references in strict order where the editor accepts them: raw subject first, environment/style second, optional prop third. Clearly mark the raw photo as read-only subject reference and demand no changes to the athlete. Arena models may still alter the subject despite instructions; this is expected risk, not a reason to waive the lock.
3. Generate two distinct scene-aware candidates in parallel for A/B exploration. Inspect both against the source. Any subject changes invalidate that candidate as a composite. Use only its environment/layout cues, or discard it. Before user presentation, rebuild/restore the exact source subject from the raw image and inspect at 100%.
4. In this Arena workspace, the image tool has no exposed pixel-protection mask. Do not claim prompt wording guarantees exact preservation. If a reliable protected-area editing operation is unavailable, use candidates only as background/layout references and keep the raw subject as an immutable layer.
5. Keep constraints explicit: no unwanted people, ring ropes, gym names, readable text or unrelated props; align any prop with the photographed motion vector. For the speed-bag image, place a plausible suspended bag just beyond the existing frame-left glove, preserving the athlete's position and pose.

### Stage 2 — one-objective context refinement

Refine only one environmental objective at a time (prop alignment; room lighting/falloff; or floor contact/cast shadows). Include the current environment/composite and the original raw subject for context, but do not use the model's returned athlete pixels. Reapply the untouched original subject foreground after every generated pass. Do not change subject scale, position, pose, lighting, grain, colors, clothing, gear, logos or face. If the new environment cannot fit around the unchanged source, reject the environment edit rather than modifying the person.

### Stage 3 — deterministic matte, integration and QA

Use the Python/OpenCV helpers in `tools/compositing/` only on a working copy. For this bright studio source, create and manually inspect an original-resolution subject matte; do not use the nocturnal color key. `rembg` mask fusion and `pymatting` are optional starts, not authority: protect white socks/shoes and colorful details, correct only the matte boundary, and never recolor the athlete to match the scene. Construct the environment/contact shadow around the unchanged person, export lossless PNG, and inspect full-frame plus 1:1 face, hair, glove, clothing/logo and footwear crops.

QA must compare the final subject to the source: no changed identity/pose/detail, no model-substituted pixels, no crop/rescale/warp, and no modified clothing/logo/color. Keep the original file untouched. If the boundary/background cannot be separated cleanly without changing the subject, report the limitation; do not trade away the immutability rule. Stage 3 must not regenerate the image.

## Lighting, optics and physics rules

- Match the environment to the source subject's actual light rather than relighting the subject. A motivated room key, reflected fill and falloff should explain the scene; protect the original highlights and shadows on the athlete.
- Ground contact should be plausible, with cast direction consistent for objects. Do not paint over the original shoes or feet to fabricate contact. Build floor shadows around their existing source pixels.
- Keep raw texture and fine detail. Protect white socks/uppers, red shoe details, logos and other bright accessories from edge cleanup. Avoid invented footwear detail or sharpening.
- Use depth of field consistent with the source camera; keep the subject and relevant speed bag sharp. Any requested treatment that would require changing subject pixels is not permitted.

## Prompt templates

`tools/compositing/prompts.py` supplies context-only and single-objective scaffolds. Prompts are requests, not guarantees of pixel preservation. Validate every result and restore the original subject pixels before presentation. Exclude environmental text/gym names unless explicitly authorized.

## Models and availability

The supplied handoff recommends OpenAI image editing (`gpt-image-1` / `gpt-image-1.5`), Google Gemini image editing (`gemini-2.5-flash-image` / `gemini-3-pro-image-preview`) and Black Forest Labs FLUX Kontext/FLUX.2 as possible pluggable providers. These are provider recommendations, not verified models used for earlier composites. Exact proprietary Arena option-slot IDs are not exposed here; do not guess, hard-code, or claim model attribution. No provider API integration or credentials are configured in this repository. Arena's image tool abstracts model metadata and currently exposes no protected-pixel mask.

For local matting the handoff recommends `rembg` ONNX sessions `isnet-general-use` and `u2net_human_seg`, optionally `pymatting`; weights have not been fetched or benchmarked here. Local pixel cleanup is independent of image generation. Edge cleanup must not change protected source-subject pixels.

## Implementation map

- `tools/compositing/edge_cleanup.py`: rim heatmap, nocturnal-sky mask, bright-region protection and frequency-separated edge cleanup; use conservatively and protect the original subject.
- `tools/compositing/matting.py`: optional dual-rembg mask fusion, cyclorama unpremultiplication and grain utility; only mask extraction may be used under the immutable-subject rule; do not run color decontamination or grain changes on the subject.
- `tools/compositing/prompts.py`: reusable context-generation and single-objective refinement scaffolds.
- `tools/compositing/tests/`: deterministic synthetic tests for the local utility layer.
- `PROJECTS/PROJECT_002/Project_Notes.md`: Project 002 rejection and revised status.
