import unittest

from libqtile import widget

from ebenezer.config.settings import AppSettings
from ebenezer.widgets.group_box import build_group_box


class TestBuildGroupBox(unittest.TestCase):
    def setUp(self):
        self.settings = AppSettings()
        self.settings.colors.fg_normal = "#FFFFFF"
        self.settings.colors.bg_topbar_selected = "#FF0000"
        self.settings.colors.fg_blue = "#0000FF"

    def test_build_group_box_default(self):
        kwargs = {}
        group_box_widget = build_group_box(self.settings, kwargs)
        self.assertIsInstance(group_box_widget, widget.GroupBox)
        self.assertEqual(group_box_widget.margin_y, 3)
        self.assertEqual(group_box_widget.margin_x, 3)
        self.assertEqual(group_box_widget.padding, 1)
        self.assertEqual(group_box_widget.borderwidth, 2)
        self.assertEqual(group_box_widget.active, "#FFFFFF")
        self.assertEqual(group_box_widget.inactive, "#FFFFFF")
        self.assertEqual(group_box_widget.this_current_screen_border, "#FF0000")
        self.assertEqual(group_box_widget.this_screen_border, "#0000FF")

    def test_build_group_box_custom_args(self):
        kwargs = {"padding": 5, "borderwidth": 4}
        group_box_widget = build_group_box(self.settings, kwargs)
        self.assertIsInstance(group_box_widget, widget.GroupBox)
        self.assertEqual(group_box_widget.padding, 5)
        self.assertEqual(group_box_widget.borderwidth, 4)


if __name__ == "__main__":
    unittest.main()
