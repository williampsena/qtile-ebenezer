import unittest
from unittest.mock import patch

from libqtile import widget

from ebenezer.config.settings import AppSettings
from ebenezer.widgets.wallpaper import build_wallpaper_widget


class TestBuildWallpaperWidget(unittest.TestCase):
    def setUp(self):
        self.settings = AppSettings()
        self.settings.fonts.font_icon = "FontAwesome"
        self.settings.fonts.font_icon_size = 12
        self.settings.colors.fg_normal = "#FFFFFF"
        self.settings.colors.bg_topbar_arrow = "#000000"
        self.settings.commands = {
            "wallpaper_menu": "echo 'Wallpaper Menu'",
            "change_wallpaper": "echo 'Change Wallpaper'",
        }

    @patch("ebenezer.widgets.wallpaper.lazy_command")
    def test_build_wallpaper_widget_default(self, mock_lazy_command):
        kwargs = {}
        wallpaper_widget = build_wallpaper_widget(self.settings, kwargs)
        self.assertIsInstance(wallpaper_widget, widget.TextBox)
        self.assertEqual(wallpaper_widget.font, "FontAwesome")
        self.assertEqual(wallpaper_widget.fontsize, 12)
        self.assertEqual(wallpaper_widget.foreground, "#FFFFFF")
        self.assertEqual(wallpaper_widget.background, "#000000")
        self.assertEqual(wallpaper_widget.text, " ")

    @patch("ebenezer.widgets.wallpaper.lazy_command")
    def test_build_wallpaper_widget_custom_args(self, mock_lazy_command):
        kwargs = {"fontsize": 14, "icon": " Custom"}
        wallpaper_widget = build_wallpaper_widget(self.settings, kwargs)
        self.assertIsInstance(wallpaper_widget, widget.TextBox)
        self.assertEqual(wallpaper_widget.fontsize, 14)
        self.assertEqual(wallpaper_widget.text, " Custom")


if __name__ == "__main__":
    unittest.main()
