import unittest
from unittest.mock import patch

from typer.testing import CliRunner

from ebenezer.commands.backlight import app

runner = CliRunner()


class TestBacklightCommands(unittest.TestCase):
    @patch("ebenezer.commands.backlight.run_command")
    @patch("ebenezer.commands.backlight.typer.echo")
    def test_backlight_level(self, mock_typer_echo, mock_run_command):
        mock_run_command.return_value = "50"

        result = runner.invoke(app, ["level"])

        mock_run_command.assert_called_once_with("brightnessctl | grep -oP '\\d+%'")
        mock_typer_echo.assert_called_once_with("50")

    @patch("ebenezer.commands.backlight.run_command")
    @patch("ebenezer.commands.backlight.typer.echo")
    def test_backlight_up(self, mock_typer_echo, mock_run_command):
        result = runner.invoke(app, ["up"])

        mock_run_command.assert_called_once_with("brightnessctl set 10%+")
        mock_typer_echo.assert_called_once_with("Backlight increased by 10%")

    @patch("ebenezer.commands.backlight.run_command")
    @patch("ebenezer.commands.backlight.typer.echo")
    def test_backlight_down(self, mock_typer_echo, mock_run_command):
        result = runner.invoke(app, ["down"])

        mock_run_command.assert_called_once_with("brightnessctl set 10%-")
        mock_typer_echo.assert_called_once_with("Backlight decreased by 10%")

    @patch("ebenezer.commands.backlight.run_command")
    @patch("ebenezer.commands.backlight.typer.echo")
    def test_backlight_set(self, mock_typer_echo, mock_run_command):
        runner.invoke(app, ["set", "75"])

        mock_run_command.assert_called_once_with("brightnessctl set 75%")
        mock_typer_echo.assert_called_once_with("Backlight changed to 75%")


if __name__ == "__main__":
    unittest.main()
