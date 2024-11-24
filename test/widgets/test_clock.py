import unittest

from libqtile import widget

from ebenezer.config.settings import AppSettings
from ebenezer.widgets.clock import build_clock_widget


class TestBuildClockWidget(unittest.TestCase):
    def setUp(self):
        self.settings = AppSettings()
        self.settings.fonts.font_icon = "FontAwesome"
        self.settings.fonts.font_icon_size = 12
        self.settings.colors.fg_normal = "#FFFFFF"

    def test_build_clock_widget_default(self):
        kwargs = {}
        clock_widget = build_clock_widget(self.settings, kwargs)
        self.assertIsInstance(clock_widget, widget.Clock)
        self.assertEqual(clock_widget.font, "FontAwesome")
        self.assertEqual(clock_widget.fontsize, 12)
        self.assertEqual(clock_widget.foreground, "#FFFFFF")
        self.assertEqual(clock_widget.padding, 2)
        self.assertEqual(clock_widget.format, "%b %d, %I:%M %p")

    def test_build_clock_widget_custom_args(self):
        kwargs = {"fontsize": 14, "format": "%H:%M:%S"}
        clock_widget = build_clock_widget(self.settings, kwargs)
        self.assertIsInstance(clock_widget, widget.Clock)
        self.assertEqual(clock_widget.fontsize, 14)
        self.assertEqual(clock_widget.format, "%H:%M:%S")


if __name__ == "__main__":
    unittest.main()
