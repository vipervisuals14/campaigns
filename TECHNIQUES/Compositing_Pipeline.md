# Editorial Sports Compositing Pipeline

This document captures the user's technical handoff from the other campaign chat. It supersedes the earlier Project 002 approach of pasting a raw cutout onto a generated empty plate as a finished result.

## Workflow that did not work

A plain studio cutout pasted over a generated empty environment is **not a finished composite**. White cyclorama reflections can remain as a 2–8 px rim on skin, hair, hands and dark clothes; white socks and shoes can remain too bright for a low-key scene; and pose, prop, camera and floor geometry can disagree. Repeated image edits without the original source also soften pores, footwear and small logos. Project 002's `boxing-speedbag-draft-v1.png` is explicitly **rejected** as a quality result and must not be used as a style or source reference.

## Three-stage hybrid workflow

### Stage 1 — scene-aware multi-reference composite

1. Analyze the raw subject photograph first: camera height/tilt, lens and perspective, horizon, framing, 3D pose/action vector, key-light direction/quality/colour temperature, contrast, clothing/logos and footwear.
2. Supply references in strict order: `images[0]` original subject; `images[1]` environment or approved series/style reference; optional `images[2]` prop/interaction reference. The environment reference guides materials, colour, mood, lighting and depth-of-field style; it must not force its camera horizon/perspective onto the new photograph. Avoid copying its exact plate for a different camera view.
3. Generate scene-aware integrated candidates in parallel and present an A/B choice. In Arena the image tool abstracts provider/model IDs and exposes its options interaction; do not claim a specific vendor produced an option unless the platform exposes that metadata.
4. Keep narrative constraints explicit: no unwanted people, ring ropes, gym names, readable text or props; a boxer wrapping hands stays on the prep floor; props must align with the photographed pose's actual motion vector.

### Stage 2 — one-objective refinement

Only refine a selected candidate when needed. Supply `[current_best_composite, original_raw_subject_photo]` on every edit pass. Each pass should change one thing only: (a) placement/clearance and footwear focus; (b) optical depth of field, lighting ratio and colour temperature; or (c) ground contact/cast-shadow physics. Lock face, pose, body scale, clothing/gear, composition and grain unless that specific item is the requested change. Do not chain edits without the original raw photo.

### Stage 3 — deterministic pixel cleanup and QA

Run the Python/OpenCV helpers in `tools/compositing/` on the selected composite. Use `rembg` masks for complex indoor scenes and the dark-sky colour-key only for its intended nocturnal-track use. Fuse `isnet-general-use` with `u2net_human_seg` in white sock/footwear zones, inspect the rim heatmap, protect bright accessories/footwear, run localized de-rimming if needed, then export lossless PNG and inspect native-pixel crops. Stage 3 must not regenerate the image. The cleanup function is conservative near protected areas, but must still be visually reviewed; do not claim a fixed 99.5% pixel-preservation guarantee without measuring a particular run.

## Lighting, optics and physics rules

- Match one motivated key light: direction, apparent size, intensity, temperature and inverse-square falloff. A visible/off-frame source should explain highlights on both subject and room; suppress conflicting practicals when they contradict the subject's light.
- Shape room brightness in the same direction as subject light (lit wall/bags/floor sheen to shadow-side falloff). Preserve the original face and skin texture; any model relighting is a candidate for human review, not automatically accepted.
- For portrait sports editorial work, use shallow optical depth of field only when compatible with the source lens/view; the target guidance is roughly full-frame 50/85 mm at f/1.4–f/1.8. Keep subject and relevant prop tack sharp; progressively soften mid/deep background without smearing architectural edges unnaturally.
- Ground contact should be tight (approximately 1–2 cm at the ground), with cast direction consistent for all objects. Mid-height shadows are compact and moderately soft; airborne objects cast broader, softer, lower-density shadows. Never add generic oversized drop-shadows.
- Keep raw texture and fine detail. For footwear that is actually in focus, preserve mesh, seams, laces, midsole and tread; do not invent detail or sharpen beyond source evidence. Protect white socks/uppers, red laces, logos and other bright accessories from dark-edge cleanup.

## Prompt templates

Reusable Stage 1 and Stage 2 prompt templates are in `tools/compositing/prompts.py`. Always fill them from analysis of the current raw images; do not reuse another photograph's camera or lighting values by assumption. Preserve source clothing/brand marks unless the user explicitly requests a change. Exclude environmental text/gym names unless explicitly authorized.

## Models and availability

The supplied handoff recommends a dual-model A/B pattern and lists OpenAI image editing (`gpt-image-1` / `gpt-image-1.5`), Google Gemini image editing (`gemini-2.5-flash-image` / `gemini-3-pro-image-preview`) and Black Forest Labs FLUX Kontext/FLUX.2 as possible pluggable providers. These are **provider recommendations from the handoff, not verified models used for the prior composites**. Exact proprietary Arena option-slot IDs are not exposed in this workspace; do not guess them, hard-code a provider, or claim model attribution. No provider API integration or credentials are configured in this repository. Arena's image tool can surface separate candidate options, but model selection and metadata are abstracted.

For local matting the handoff recommends `rembg` ONNX sessions `isnet-general-use` and `u2net_human_seg`, optionally `pymatting`; it warns that BiRefNet models may exceed low-RAM CPU worker memory. These model weights may require downloads and have not been fetched or benchmarked here. The local pixel cleanup code is available independently of any image-generation provider.

## Implementation map

- `tools/compositing/edge_cleanup.py`: white-rim heatmap, nocturnal-sky mask, bright-region protection and frequency-separated edge cleanup.
- `tools/compositing/matting.py`: optional dual-rembg mask fusion, cyclorama unpremultiplication and grain matching.
- `tools/compositing/prompts.py`: reusable prompt scaffolds with strict reference order and one-objective refinement.
- `tools/compositing/tests/`: deterministic synthetic tests for the local utility layer.
- `PROJECTS/PROJECT_002/Project_Notes.md`: Project 002 rejection and revised workflow status.
