import unittest
import numpy as np

from tools.compositing.edge_cleanup import (
    build_auto_protection_mask,
    detect_white_rim_heatmap,
    extract_nocturnal_sky_fg_mask,
    remove_studio_white_rim,
)
from tools.compositing.matting import add_matched_35mm_grain


class EdgeCleanupTests(unittest.TestCase):
    def test_white_rim_detector_marks_bright_subject_boundary(self):
        image = np.zeros((48, 48, 3), dtype=np.uint8)
        mask = np.zeros((48, 48), dtype=np.uint8)
        mask[12:36, 12:36] = 255
        image[12:36, 12:36] = 35
        image[12:14, 12:36] = 245
        rim, diagnostic = detect_white_rim_heatmap(image, mask, band_px=3)
        self.assertGreater(int(rim.sum()), 0)
        self.assertTrue(np.any(diagnostic[rim] == np.array([0, 255, 80])))

    def test_protection_mask_covers_white_footwear_zone(self):
        image = np.zeros((40, 50, 3), dtype=np.uint8)
        image[20:35, 20:40] = 230
        protect, footwear = build_auto_protection_mask(image, footwear_boxes=[(18, 18, 42, 37)])
        self.assertEqual(protect.shape, image.shape[:2])
        self.assertGreater(float(footwear[25, 25]), 0.0)
        self.assertGreater(float(protect[25, 25]), 0.0)

    def test_nocturnal_key_isolated_to_cool_dark_component(self):
        image = np.full((40, 40, 3), 4, dtype=np.uint8)
        image[5:25, 5:25] = (6, 17, 45)  # cool dark sky in RGB
        mask = extract_nocturnal_sky_fg_mask(image, min_sky_area=100)
        self.assertEqual(int(mask[10, 10]), 0)
        self.assertEqual(int(mask[30, 30]), 1)

    def test_rim_cleanup_preserves_pixels_outside_roi(self):
        image = np.full((64, 64, 3), 30, dtype=np.uint8)
        mask = np.zeros((64, 64), dtype=np.uint8)
        mask[12:52, 12:52] = 255
        image[12:52, 12:52] = 45
        image[12:15, 12:52] = 235
        before = image.copy()
        result = remove_studio_white_rim(image, fg_mask=mask, roi_box=(8, 8, 56, 56))
        self.assertEqual(result.dtype, np.uint8)
        self.assertTrue(np.array_equal(result[:8], before[:8]))
        self.assertTrue(np.array_equal(result[56:], before[56:]))
        self.assertTrue(np.array_equal(result[:, :8], before[:, :8]))
        self.assertTrue(np.array_equal(result[:, 56:], before[:, 56:]))

    def test_grain_is_reproducible_for_same_seed(self):
        image = np.full((32, 32, 3), 120, dtype=np.uint8)
        first = add_matched_35mm_grain(image, seed=11)
        second = add_matched_35mm_grain(image, seed=11)
        self.assertTrue(np.array_equal(first, second))
        self.assertFalse(np.array_equal(first, image))


if __name__ == "__main__":
    unittest.main()
