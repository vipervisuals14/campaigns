"""Prompt scaffolds for scene context with an immutable photographic subject.

Prompts cannot guarantee pixel locking. Any generated athlete pixels are forbidden in
final output; restore the foreground from the unchanged raw photo before presentation.
"""

STAGE1_TEMPLATE = """Create a photorealistic {aspect_ratio} editorial sports scene/context for:
{environment_description}. This is a background/layout integration task, not permission
to alter or replace the photographed athlete in image 1.

IMMUTABLE SOURCE — IMAGE 1
Image 1 is a read-only source of truth. Preserve the original camera geometry, framing,
pose, action direction, scale, identity, face, expression, hair, skin texture/pores,
anatomy, clothing, logos, colors, accessories, shoes, shadows, highlights, sharpness and
every visible subject detail exactly. Do not regenerate, redraw, retouch, relight, recolor,
reshape, sharpen, smooth, crop, scale, warp, or invent any pixels on the person. Do not
change the original subject photo. If exact protection cannot be guaranteed, generate
only a subject-free environment/layout reference and do not present it as a finished
composite. Prompts are not pixel masks: verify output and restore original subject pixels
from image 1 before any final candidate is shown.

REFERENCE USE
Image 2 guides environment materials, palette, atmosphere and optical style only. Image 3
is an optional prop reference only. Do not copy another person's identity, pose, body or
clothing. The environment must fit image 1's {camera_geometry}, {horizon_description},
{motion_vector} and {framing_type}; do not force a reference photograph's perspective.

SCENE REQUIREMENTS
Narrative and placement: {narrative_placement_and_constraints}.
Spatial layout and prop alignment: {spatial_layout_and_prop_alignment}.
Action location restriction: {action_location_constraint}.
Motivated environment light matching the unmodified source: {key_light_direction_quality_and_color_temp};
room falloff from {lit_side} to {shadow_side}. Keep subject and interaction in focus:
{focus_plane}; environment depth of field: {depth_of_field}. Build physically plausible
floor plane, room geometry, prop suspension, cast shadows and ambient falloff around the
source camera. No unrelated people, rings, signage, readable text or unwanted props.

STRICTLY NO {forbidden_elements}. Output may be used only as a scene/layout candidate
until the original subject pixels have been restored and checked against image 1."""

STAGE2_TEMPLATE = """Change only this environmental target: {single_target_change}.
Image 1 is the current scene/context; image 2 is the immutable original subject photograph.
Do not alter any subject pixel: no regeneration, repainting, retouching, relighting,
recoloring, reshaping, rescaling, warping, cropping, sharpening, smoothing or logo/wardrobe
changes. Keep all subject attributes, colors, original lighting and source camera geometry
unchanged. If the model cannot guarantee subject preservation, treat its returned person
pixels as invalid and use only the environment result; restore the subject from image 2
before presenting a candidate. Never show a generated, altered subject as the final.
"""


def build_stage1_prompt(**values: str) -> str:
    """Fill the Stage 1 prompt, failing clearly if any analysis field is absent."""
    return STAGE1_TEMPLATE.format(**values)


def build_stage2_prompt(single_target_change: str) -> str:
    """Build a one-objective environmental refinement prompt."""
    if not single_target_change or not single_target_change.strip():
        raise ValueError("single_target_change must be a specific, non-empty instruction")
    return STAGE2_TEMPLATE.format(single_target_change=single_target_change.strip())
