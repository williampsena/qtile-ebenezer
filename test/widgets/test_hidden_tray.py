import unittest

from libqtile import widget

from ebenezer.config.settings import AppSettings
from ebenezer.widgets.hidden_tray import build_hidden_tray


class TestBuildHiddenTray(unittest.TestCase):
    def setUp(self):
        self.settings = AppSettings()
        self.settings.fonts.font_icon = "FontAwesome"
        self.settings.environment.os_logo_icon = ""
        self.settings.environment.os_logo_icon_color = "#FFFFFF"
        self.settings.colors.bg_topbar_arrow = "#000000"

    def test_build_hidden_tray_default(self):
        kwargs = {}
        hidden_tray_widget = build_hidden_tray(self.settings, kwargs)
        self.assertIsInstance(hidden_tray_widget, widget.WidgetBox)
        self.assertEqual(hidden_tray_widget.padding, 10)
        self.assertEqual(hidden_tray_widget.font, "FontAwesome")
        self.assertEqual(hidden_tray_widget.text_open, "")
        self.assertEqual(hidden_tray_widget.text_closed, "")
        self.assertEqual(hidden_tray_widget.foreground, "#FFFFFF")
        self.assertEqual(hidden_tray_widget.background, "#000000")

    def test_build_hidden_tray_custom_args(self):
        kwargs = {"padding": 20, "foreground": "#000000"}
        hidden_tray_widget = build_hidden_tray(self.settings, kwargs)
        self.assertIsInstance(hidden_tray_widget, widget.WidgetBox)
        self.assertEqual(hidden_tray_widget.padding, 20)
        self.assertEqual(hidden_tray_widget.foreground, "#000000")


if __name__ == "__main__":
    unittest.main()
