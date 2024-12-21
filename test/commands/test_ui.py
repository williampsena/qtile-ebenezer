import unittest
from unittest.mock import patch

from click.testing import CliRunner

from ebenezer.commands.ui import cli


class TestUICommands(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()

    @patch("ebenezer.commands.ui.run_powermenu")
    def test_powermenu(self, mock_run_powermenu):
        result = self.runner.invoke(cli, ["powermenu"])
        mock_run_powermenu.assert_called_once()
        self.assertEqual(result.exit_code, 0)

    @patch("ebenezer.commands.ui.run_confirm")
    def test_confirm(self, mock_run_confirm):
        result = self.runner.invoke(cli, ["confirm"])
        mock_run_confirm.assert_called_once()
        self.assertEqual(result.exit_code, 0)

    @patch("ebenezer.commands.ui.run_wallpaper_menu")
    def test_wallpaper_menu(self, mock_run_wallpaper_menu):
        result = self.runner.invoke(cli, ["wallpaper-menu"])
        mock_run_wallpaper_menu.assert_called_once()
        self.assertEqual(result.exit_code, 0)


if __name__ == "__main__":
    unittest.main()
