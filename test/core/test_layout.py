import unittest

from libqtile import layout

from ebenezer.config.settings import AppSettings
from ebenezer.core.layout import build_layouts


class TestBuildLayouts(unittest.TestCase):
    def setUp(self):
        self.settings = AppSettings()
        self.settings.layouts = {
            "bsp": {"margin": 5},
            "max": {"border_width": 2},
            "tile": {"shift_windows": False, "ratio": 0.5},
            "win11": {"screen": "#0000FF"},
        }

    def test_build_layouts(self):
        layouts = build_layouts(self.settings)

        self.assertEqual(len(layouts), 3)
        self.assertIsInstance(layouts[0], layout.Bsp)
        self.assertIsInstance(layouts[1], layout.Max)
        self.assertIsInstance(layouts[2], layout.Tile)

        self.assertEqual(layouts[0].margin, 5)
        self.assertEqual(layouts[1].border_width, 2)
        self.assertEqual(layouts[2].shift_windows, False)
        self.assertEqual(layouts[2].ratio, 0.5)


if __name__ == "__main__":
    unittest.main()
