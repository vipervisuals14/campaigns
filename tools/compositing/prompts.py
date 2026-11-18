"""Reusable prompts for scene-aware sports-photo compositing and targeted refinements.

Use exact reference order: original subject first; environment/style second; optional
prop interaction third. Fill analytical values from each source capture; never infer
camera or light values from a different photo in the series.
"""

STAGE1_TEMPLATE = """Authentic, raw, full-frame on-location sports editorial photograph.
Composite the exact athlete from image 1 into {environment_description}, guided by
image 2 for materials, palette, atmosphere and optical style; use image 3 only as an
optional prop/interaction reference. Narrative: {narrative_placement_and_constraints}.

1. ORIGINAL SUBJECT AND CAMERA — IMAGE 1 IS SOURCE OF TRUTH
- Preserve the exact {aspect_ratio} {framing_type}, camera height/tilt {camera_geometry},
  horizon {horizon_description}, pose, motion vector {motion_vector}, face, expression,
  hair, skin texture/pores, proportions, clothing, gear and existing brand marks.
- No beauty filtering, skin smoothing, muscle enhancement, invented details, pose change
  or identity drift. Reconstruct the environment to fit image 1; do not force its camera
  into the reference photograph's view.

2. ENVIRONMENT AND PROP REFERENCES
- {spatial_layout_and_prop_alignment}
- Image 2 guides architectural materials, colour, atmosphere, depth-of-field and light
  character only; do not copy its exact perspective/horizon where incompatible. Image 3
  guides the optional prop's shape/placement only; remove third-party brand marks if asked.
- Keep the subject and action at the correct place: {action_location_constraint}.

3. PHOTOGRAPHIC INTEGRATION
- Match a single motivated key: {key_light_direction_quality_and_color_temp}, with
  corresponding room falloff from {lit_side} to {shadow_side}. Suppress conflicting
  secondary colour temperatures. Ground plane, scale, prop orientation, floor contact,
  cast shadows, reflections and depth of field must agree with image 1.
- Remove the cyclorama, including trapped white pockets and bright rims, without
  reshaping the subject. Protect intentional white socks/shoes and colourful detail.
- Optical rendering: subject/interaction {focus_plane}; background {depth_of_field}.
  Natural sensor texture, realistic highlights and shadows; no synthetic HDR or
  oversharpening.

STRICTLY NO {forbidden_elements}."""

STAGE2_TEMPLATE = """Modify only this single target: {single_target_change}.
Use image 1 as the current selected composite and image 2 as the original raw subject
photo. Lock the composition, camera view, subject pose/height, face, identity, skin pores,
clothing, gear, prop geometry and existing grain unless explicitly named in the target.
Do not regenerate or soften the original subject. Keep all other elements unchanged.
"""


def build_stage1_prompt(**values: str) -> str:
    """Fill the Stage 1 prompt, failing clearly if any analysis field is absent."""
    return STAGE1_TEMPLATE.format(**values)


def build_stage2_prompt(single_target_change: str) -> str:
    """Build a one-objective refinement prompt; never combine unrelated fixes."""
    if not single_target_change or not single_target_change.strip():
        raise ValueError("single_target_change must be a specific, non-empty instruction")
    return STAGE2_TEMPLATE.format(single_target_change=single_target_change.strip())
