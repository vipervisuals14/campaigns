# Corrections Log

## Project 001 — initial setup and subject-preservation correction

- **User correction:** The athlete in the supplied source photograph must not be changed or replaced. The task is to composite the supplied subject into a scene. The subject is wrapping his hands to prepare for boxing and must never be shown in the ring. Do not include the environment reference's gym name in the composition.
- **Underlying lesson:** Generated subject replacement is not acceptable when the source subject is already the intended subject. Environment editing must not alter pose, identity, clothing or the pre-training action. The reference environment provides atmosphere and materials, not permission to copy its signage.
- **Action for future work:** Preserve the source photograph and use it as the subject layer; reconstruct/replace only the environment and use a non-destructive matte. Keep the subject on the gym floor, outside any ring. Exclude the gym name and inspect all visible signage before delivery.
- **Process issue:** A first generated-image option was offered before the user's compositing-only preference was understood. Do not use image generation to replace an already supplied subject. Read repository instructions and project notes before processing; in this conversation, the first draft preceded the user's master workflow being available.
- **Status:** Draft exists but is not approved. No claim of approval or permanent benchmark.

## 2026-11-18 — user-selected style and quality benchmark

- **User feedback:** The user supplied `COMPOSITING_KNOWLEDGE/References/boxing-gym-editorial-user-benchmark.png`, said it is substantially better than our composites, and asked that future work match its style and quality.
- **Observed direction:** Portrait editorial framing; subject fills the frame and sits naturally in the environment; moody, warm industrial-gym atmosphere; soft directional/window light; nuanced tonal depth; softly defocused environmental detail. Integration appears natural rather than sharply pasted onto a wide, flat background.
- **Underlying issue in v1/v2:** They were wide composites on the reference plate, the subject read as a cutout/paste, and the treatment did not reach the benchmark's portrait framing and environmental depth. Do not defend or reuse those drafts as style references.
- **Action:** Preserve the supplied benchmark unchanged; use it for style/quality only. For future work, return to the original subject photograph, choose/reconstruct an environment compatible with its camera view, match portrait framing and depth where suitable, and prioritize believable integration. Never use the benchmark as a replacement subject or fixed background plate.
- **Status:** User-confirmed style benchmark. This feedback does not approve the existing Project 001 drafts.

## 2026-11-18 — Project 002 cutout-and-paste draft rejection and pipeline correction

- **User correction:** The user explicitly rejected `PROJECTS/PROJECT_002/Working_Composites/boxing-speedbag-draft-v1.png` as “really bad.” It is not approved and must not be reused as a quality reference or polished further as the primary approach.
- **Underlying issue:** A hand-cut subject pasted onto an empty generated plate does not produce scene-aware integration. Studio rim spill, footwear brightness, lighting mismatch, missing environmental bounce/contact, and pose/prop/ground geometry remain apparent. Earlier threshold/GrabCut/polygon experiments were also artifact-prone.
- **Action:** Adopt the three-stage hybrid documented in `TECHNIQUES/Compositing_Pipeline.md`: scene-aware multi-reference generation (original subject first, environment/style second, optional prop third) with two distinct candidates in parallel; single-objective edits that re-include the original raw subject; then deterministic OpenCV/matting cleanup and native-pixel QA. Protect white footwear, socks, logos and colourful details.
- **Provider caveat:** The handoff recommends possible OpenAI, Gemini and Black Forest Labs editing families but does not establish which proprietary Arena models were used. Do not guess model IDs or attribute any past result to a vendor without exposed metadata.
- **Status:** Workflow/tooling guidance recorded. No new composite generated or approved; original Project 002 files remain unchanged.

## 2026-11-18 — immutable original subject rule

- **User correction:** The generated speed-bag options altered the boxer. The user stated the original subject image cannot be changed and this must be the rule.
- **Action:** Treat the raw subject photo as immutable and the sole source of final subject pixels. No AI redraw, replacement, retouch, relighting, recoloring, rescaling, crop, warp, sharpening, smoothing, or invented subject detail. Preserve the original file byte-for-byte. Since the current Arena image tool exposes no reliable protected-pixel mask, any generated subject pixels are invalid for a final; generated output is context/layout only until the untouched original foreground is restored and verified. Do not show an A/B composite before that verification. Do not run color/rim cleanup or grain changes on the boxer.
- **Result:** The user rejected the generated options; none was selected or saved. No Project 002 composite is approved. Updated `MASTER_INSTRUCTIONS.md`, `COMPOSITING_KNOWLEDGE.md`, `TECHNIQUES/Compositing_Pipeline.md`, Project 002 notes, and the prompt/tool guidance to make immutability controlling over the earlier scene-aware editing recommendation.

## 2026-11-18 — rejection of immutable-subject speedbag draft v2

- **User feedback:** The user called `PROJECTS/PROJECT_002/Working_Composites/boxing-speedbag-immutable-subject-draft-v2.png` “terrible.” It is rejected and not a reusable base or quality reference.
- **Process failure:** Protecting the original subject pixels was necessary but insufficient. I used a crude threshold/manual polygon matte, a generated generic background, and a relocated prop. The result had an obvious cutout edge, failed environmental integration, and did not convincingly connect the fist to the bag. This repeated the forbidden sticker-like approach despite the prior warning.
- **Action:** Do not polish or reuse this draft. Future attempts require a genuinely high-quality reviewed matte, subject-aware layout and verified hand/bag contact before presentation. Do not generate/show a composite until it passes full-frame and 100% edge/contact QA. If the current tools cannot both preserve the original subject and achieve credible integration, disclose that limitation instead of presenting another poor draft as progress.
- **Status:** Rejected; no Project 002 composite approved.
