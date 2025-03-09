import unittest
from unittest.mock import patch

from click.testing import CliRunner

from ebenezer.commands.volume import cli

PACTL_SHORT_SINKS = (
    "0\talsa_output.pci-0000_00_1f.3.analog-stereo module-alsa-card.c\t"
    "s16le 2ch\t44100Hz\tSUSPENDED\n"
)

PACTL_SHORT_SINKS_PHONE = PACTL_SHORT_SINKS + (
    "1\talsa_output.usb-Logitech_Logitech_USB_Headset-00.analog-stereo module-alsa-card.c\t"
    "s16le 2ch\t44100Hz\tRUNNING\n"
)


class TestVolumeCommands(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()

    @patch("ebenezer.commands.volume.run_command")
    @patch("ebenezer.commands.volume.click.echo")
    def test_volume_level(self, mock_click_echo, mock_run_command):
        mock_run_command.side_effect = lambda cmd: (
            PACTL_SHORT_SINKS_PHONE if "pactl list short sinks" in cmd else "50%"
        )

        result = self.runner.invoke(cli, ["level"])

        mock_run_command.assert_has_calls(
            [
                unittest.mock.call("pactl list short sinks"),
                unittest.mock.call(
                    "pactl list sinks | grep -A 15 'Name: alsa_output.pci-0000_00_1f.3.analog-stereo module-alsa-card.c' | grep 'Volume:' | head -n 1 | awk '{print $5}' | grep -o '[0-9]\\+'"
                ),
                unittest.mock.call(
                    "pactl list sinks | grep -A 15 'Name: alsa_output.usb-logitech_logitech_usb_headset-00.analog-stereo module-alsa-card.c' | grep 'Volume:' | head -n 1 | awk '{print $5}' | grep -o '[0-9]\\+'"
                ),
            ]
        )

        mock_click_echo.assert_called_once_with("50%")
        assert result.exit_code == 0

    @patch("ebenezer.commands.volume.run_command")
    @patch("ebenezer.commands.volume.click.echo")
    def xtest_volume_levels(self, mock_click_echo, mock_run_command):
        mock_run_command.return_value = "speaker: 50%\nbluetooth: 80%"

        self.runner.invoke(cli, ["levels"])

        mock_run_command.assert_called_once_with(
            "pactl list sinks | grep 'Volume:' | head -n 1 | awk '{print $5}' | tail -n 1 | grep -o '[0-9]\\+'"
        )
        mock_click_echo.assert_called_once_with("50%")

    @patch("ebenezer.commands.volume.run_command")
    @patch("ebenezer.commands.volume.click.echo")
    def test_volume_up(self, mock_click_echo, mock_run_command):
        result = self.runner.invoke(cli, ["up"])

        mock_run_command.assert_called_once_with(
            "pactl set-sink-volume @DEFAULT_SINK@ +5%"
        )
        mock_click_echo.assert_called_once_with("Volume increased by 5%")
        assert result.exit_code == 0

    @patch("ebenezer.commands.volume.run_command")
    @patch("ebenezer.commands.volume.click.echo")
    def test_volume_down(self, mock_click_echo, mock_run_command):
        result = self.runner.invoke(cli, ["down"])

        mock_run_command.assert_called_once_with(
            "pactl set-sink-volume @DEFAULT_SINK@ -5%"
        )
        mock_click_echo.assert_called_once_with("Volume decreased by 5%")
        assert result.exit_code == 0

    @patch("ebenezer.commands.volume.run_command")
    @patch("ebenezer.commands.volume.click.echo")
    def test_mute_on(self, mock_click_echo, mock_run_command):
        result = self.runner.invoke(cli, ["mute-on"])

        mock_run_command.assert_called_once_with("pactl set-sink-mute @DEFAULT_SINK@ 1")
        mock_click_echo.assert_called_once_with("Mute on")
        assert result.exit_code == 0

    @patch("ebenezer.commands.volume.run_command")
    @patch("ebenezer.commands.volume.click.echo")
    def test_mute_off(self, mock_click_echo, mock_run_command):
        result = self.runner.invoke(cli, ["mute-off"])

        mock_run_command.assert_called_once_with("pactl set-sink-mute @DEFAULT_SINK@ 0")
        mock_click_echo.assert_called_once_with("Mute off")
        assert result.exit_code == 0

    @patch("ebenezer.commands.volume.run_command")
    @patch("ebenezer.commands.volume.click.echo")
    def test_mute_toggle(self, mock_click_echo, mock_run_command):
        result = self.runner.invoke(cli, ["mute-toggle"])

        mock_run_command.assert_called_once_with(
            "pactl set-sink-mute @DEFAULT_SINK@ toggle"
        )
        mock_click_echo.assert_called_once_with("Mute toggled")
        assert result.exit_code == 0

    @patch("ebenezer.commands.volume.run_command")
    @patch("ebenezer.commands.volume.click.echo")
    def test_mute_mic(self, mock_click_echo, mock_run_command):
        result = self.runner.invoke(cli, ["mute-mic"])

        mock_run_command.assert_called_once_with(
            "pactl set-source-mute @DEFAULT_SOURCE@ toggle"
        )
        mock_click_echo.assert_called_once_with("Microphone mute toggled")
        assert result.exit_code == 0

    @patch("ebenezer.commands.volume.run_command")
    @patch("ebenezer.commands.volume.click.echo")
    def test_phone_plugged(self, mock_click_echo, mock_run_command):
        mock_run_command.return_value = PACTL_SHORT_SINKS_PHONE

        result = self.runner.invoke(cli, ["phone-plugged"])

        mock_click_echo.assert_called_once_with(True)
        self.assertEqual(result.exit_code, 0)

    @patch("ebenezer.commands.volume.run_command")
    @patch("ebenezer.commands.volume.click.echo")
    def test_phone_not_plugged(self, mock_click_echo, mock_run_command):
        mock_run_command.return_value = PACTL_SHORT_SINKS

        result = self.runner.invoke(cli, ["phone-plugged"])

        mock_click_echo.assert_called_once_with(False)
        self.assertEqual(result.exit_code, 0)


if __name__ == "__main__":
    unittest.main()
