import unittest

from libqtile import widget

from ebenezer.config.settings import AppSettings
from ebenezer.widgets.app_menu import build_app_menu_widget


class TestBuildAppMenuWidget(unittest.TestCase):
    def setUp(self):
        self.settings = AppSettings()
        self.settings.fonts.font_icon = "FontAwesome"
        self.settings.fonts.font_icon_size = 12
        self.settings.environment.os_logo_icon = ""
        self.settings.environment.os_logo_icon_color = "#FFFFFF"

    def test_build_app_menu_widget_default(self):
        kwargs = {}
        app_menu_widget = build_app_menu_widget(self.settings, kwargs)
        self.assertIsInstance(app_menu_widget, widget.TextBox)
        self.assertEqual(app_menu_widget.font, "FontAwesome")
        self.assertEqual(app_menu_widget.fontsize, 12)
        self.assertEqual(app_menu_widget.foreground, "#FFFFFF")
        self.assertEqual(app_menu_widget.text, " ")

    def test_build_app_menu_widget_custom_icon(self):
        kwargs = {"icon": ""}
        app_menu_widget = build_app_menu_widget(self.settings, kwargs)
        self.assertIsInstance(app_menu_widget, widget.TextBox)
        self.assertEqual(app_menu_widget.text, " ")

    def test_build_app_menu_widget_custom_args(self):
        kwargs = {"padding": 20, "foreground": "#000000"}
        app_menu_widget = build_app_menu_widget(self.settings, kwargs)
        self.assertIsInstance(app_menu_widget, widget.TextBox)
        self.assertEqual(app_menu_widget.padding, 20)
        self.assertEqual(app_menu_widget.foreground, "#000000")


if __name__ == "__main__":
    unittest.main()
