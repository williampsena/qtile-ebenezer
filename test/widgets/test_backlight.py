import unittest

from libqtile import widget

from ebenezer.config.settings import AppSettings
from ebenezer.widgets.backlight import build_backlight_widget


class TestBuildBacklightWidget(unittest.TestCase):
    def setUp(self):
        self.settings = AppSettings()
        self.settings.fonts.font_icon = "FontAwesome"
        self.settings.fonts.font_icon_size = 12
        self.settings.colors.fg_normal = "#FFFFFF"
        self.settings.environment.backlight_name = "intel_backlight"

    def test_build_backlight_widget_default(self):
        kwargs = {}
        backlight_widget = build_backlight_widget(self.settings, kwargs)
        self.assertIsInstance(backlight_widget, widget.Backlight)
        self.assertEqual(backlight_widget.font, "FontAwesome")
        self.assertEqual(backlight_widget.fontsize, 12)
        self.assertEqual(backlight_widget.foreground, "#FFFFFF")
        self.assertEqual(backlight_widget.backlight_name, "intel_backlight")

    def test_build_backlight_widget_custom_args(self):
        kwargs = {"fontsize": 14, "foreground": "#000000"}
        backlight_widget = build_backlight_widget(self.settings, kwargs)
        self.assertIsInstance(backlight_widget, widget.Backlight)
        self.assertEqual(backlight_widget.fontsize, 14)
        self.assertEqual(backlight_widget.foreground, "#000000")


if __name__ == "__main__":
    unittest.main()
