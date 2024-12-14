import unittest
from unittest.mock import patch

from typer.testing import CliRunner

from ebenezer.commands.volume import app

runner = CliRunner()


class TestVolumeCommands(unittest.TestCase):
    @patch("ebenezer.commands.volume.run_command")
    @patch("ebenezer.commands.volume.typer.echo")
    def test_volume_level(self, mock_typer_echo, mock_run_command):
        mock_run_command.return_value = "50%"

        result = runner.invoke(app, ["level"])

        mock_run_command.assert_called_once_with(
            "pactl list sinks | grep 'Volume:' | head -n 1 | awk '{print $5}' | tail -n 1 | grep -o '[0-9]\\+'"
        )
        mock_typer_echo.assert_called_once_with("50%")

    @patch("ebenezer.commands.volume.run_command")
    @patch("ebenezer.commands.volume.typer.echo")
    def test_volume_up(self, mock_typer_echo, mock_run_command):
        result = runner.invoke(app, ["up"])

        mock_run_command.assert_called_once_with(
            "pactl set-sink-volume @DEFAULT_SINK@ +5%"
        )
        mock_typer_echo.assert_called_once_with("Volume increased by 5%")

    @patch("ebenezer.commands.volume.run_command")
    @patch("ebenezer.commands.volume.typer.echo")
    def test_volume_down(self, mock_typer_echo, mock_run_command):
        result = runner.invoke(app, ["down"])

        mock_run_command.assert_called_once_with(
            "pactl set-sink-volume @DEFAULT_SINK@ -5%"
        )
        mock_typer_echo.assert_called_once_with("Volume decreased by 5%")

    @patch("ebenezer.commands.volume.run_command")
    @patch("ebenezer.commands.volume.typer.echo")
    def test_mute_on(self, mock_typer_echo, mock_run_command):
        result = runner.invoke(app, ["mute_on"])

        mock_run_command.assert_called_once_with("pactl set-sink-mute @DEFAULT_SINK@ 1")
        mock_typer_echo.assert_called_once_with("Mute on")

    @patch("ebenezer.commands.volume.run_command")
    @patch("ebenezer.commands.volume.typer.echo")
    def test_mute_off(self, mock_typer_echo, mock_run_command):
        result = runner.invoke(app, ["mute_off"])

        mock_run_command.assert_called_once_with("pactl set-sink-mute @DEFAULT_SINK@ 0")
        mock_typer_echo.assert_called_once_with("Mute off")

    @patch("ebenezer.commands.volume.run_command")
    @patch("ebenezer.commands.volume.typer.echo")
    def test_mute_toggle(self, mock_typer_echo, mock_run_command):
        result = runner.invoke(app, ["mute_toggle"])

        mock_run_command.assert_called_once_with(
            "pactl set-sink-mute @DEFAULT_SINK@ toggle"
        )
        mock_typer_echo.assert_called_once_with("Mute toggled")


if __name__ == "__main__":
    unittest.main()
