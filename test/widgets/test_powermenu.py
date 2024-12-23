import unittest
from unittest.mock import patch

from libqtile import widget

from ebenezer.config.settings import AppSettings
from ebenezer.widgets.powermenu import _powermenu_modal, build_powermenu_widget


class TestBuildPowermenuWidget(unittest.TestCase):
    def setUp(self):
        self.settings = AppSettings()
        self.settings.fonts.font_icon = "FontAwesome"
        self.settings.fonts.font_icon_size = 12
        self.settings.colors.fg_normal = "#FFFFFF"
        self.settings.colors.bg_topbar_arrow = "#000000"
        self.settings.commands = {"powermenu": "echo 'Power Menu'"}

    @patch("ebenezer.widgets.powermenu.run_shell_command")
    def test_powermenu_modal(self, mock_run_shell_command):
        modal = _powermenu_modal()
        modal()
        mock_run_shell_command.assert_called_once_with("ebenezer ui powermenu", **{})

    def test_build_powermenu_widget_default(self):
        kwargs = {}
        powermenu_widget = build_powermenu_widget(self.settings, kwargs)
        self.assertIsInstance(powermenu_widget, widget.TextBox)
        self.assertEqual(powermenu_widget.font, "FontAwesome")
        self.assertEqual(powermenu_widget.fontsize, 12)
        self.assertEqual(powermenu_widget.foreground, "#FFFFFF")
        self.assertEqual(powermenu_widget.background, "#000000")


if __name__ == "__main__":
    unittest.main()
