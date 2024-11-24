import unittest

from libqtile import widget

from ebenezer.config.settings import AppSettings
from ebenezer.widgets.window_name import build_window_name_widget


class TestBuildWindowNameWidget(unittest.TestCase):
    def setUp(self):
        self.settings = AppSettings()
        self.settings.fonts.font_icon = "FontAwesome"
        self.settings.fonts.font_icon_size = 12
        self.settings.colors.fg_normal = "#FFFFFF"

    def test_build_window_name_widget_default(self):
        kwargs = {}
        window_name_widget = build_window_name_widget(self.settings, kwargs)
        self.assertIsInstance(window_name_widget, widget.WindowName)
        self.assertEqual(window_name_widget.font, "FontAwesome")
        self.assertEqual(window_name_widget.fontsize, 12)
        self.assertEqual(window_name_widget.foreground, "#FFFFFF")
        self.assertEqual(window_name_widget.max_chars, 30)

    def test_build_window_name_widget_custom_args(self):
        kwargs = {"fontsize": 14, "max_chars": 50}
        window_name_widget = build_window_name_widget(self.settings, kwargs)
        self.assertIsInstance(window_name_widget, widget.WindowName)
        self.assertEqual(window_name_widget.fontsize, 14)
        self.assertEqual(window_name_widget.max_chars, 50)


if __name__ == "__main__":
    unittest.main()
