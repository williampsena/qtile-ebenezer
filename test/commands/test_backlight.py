import unittest
from unittest.mock import patch

from click.testing import CliRunner

from ebenezer.commands.backlight import cli


class TestBacklightCommands(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()

    @patch("ebenezer.commands.backlight.run_command")
    @patch("ebenezer.commands.backlight.click.echo")
    def test_backlight_level(self, mock_click_echo, mock_run_command):
        mock_run_command.return_value = "50"

        result = self.runner.invoke(cli, ["level"])

        mock_run_command.assert_called_once_with("brightnessctl | grep -oP '\\d+%'")
        mock_click_echo.assert_called_once_with("50")

    @patch("ebenezer.commands.backlight.run_command")
    @patch("ebenezer.commands.backlight.click.echo")
    def test_backlight_up(self, mock_click_echo, mock_run_command):
        result = self.runner.invoke(cli, ["up"])

        mock_run_command.assert_called_once_with("brightnessctl set 10%+")
        mock_click_echo.assert_called_once_with("Backlight increased by 10%")

    @patch("ebenezer.commands.backlight.run_command")
    @patch("ebenezer.commands.backlight.click.echo")
    def test_backlight_down(self, mock_click_echo, mock_run_command):
        result = self.runner.invoke(cli, ["down"])

        mock_run_command.assert_called_once_with("brightnessctl set 10%-")
        mock_click_echo.assert_called_once_with("Backlight decreased by 10%")

    @patch("ebenezer.commands.backlight.run_command")
    @patch("ebenezer.commands.backlight.click.echo")
    def test_backlight_set(self, mock_click_echo, mock_run_command):
        self.runner.invoke(cli, ["set", "75"])

        mock_run_command.assert_called_once_with("brightnessctl set 75%")
        mock_click_echo.assert_called_once_with("Backlight changed to 75%")


if __name__ == "__main__":
    unittest.main()
