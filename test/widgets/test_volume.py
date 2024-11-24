import unittest
from unittest.mock import patch

from libqtile import widget

from ebenezer.config.settings import AppSettings
from ebenezer.widgets.volume import (
    _do_volume_down,
    _do_volume_up,
    _get_current_volume,
    _is_muted,
    _mute_toggle,
    _push_volume_notification,
    _unmute,
    build_volume_widget,
    setup_volume_keys,
)


class TestBuildVolumeWidget(unittest.TestCase):
    def setUp(self):
        self.settings = AppSettings()
        self.settings.fonts.font_icon = "FontAwesome"
        self.settings.fonts.font_icon_size = 12
        self.settings.colors.fg_normal = "#FFFFFF"
        self.settings.colors.bg_topbar_arrow = "#000000"
        self.settings.commands = {
            "mixer": "echo 'Mixer'",
            "volume_level": "echo '50%'",
            "mute_status": "echo 'no'",
            "volume_up": "echo 'Volume Up'",
            "volume_down": "echo 'Volume Down'",
            "mute": "echo 'Mute'",
            "mute_off": "echo 'Mute Off'",
        }

    def test_build_volume_widget_default(self):
        kwargs = {}
        volume_widget = build_volume_widget(self.settings, kwargs)
        self.assertIsInstance(volume_widget, widget.Volume)
        self.assertEqual(volume_widget.font, "FontAwesome")
        self.assertEqual(volume_widget.fontsize, 12)
        self.assertEqual(volume_widget.foreground, "#FFFFFF")
        self.assertEqual(volume_widget.background, "#000000")

    def test_build_volume_widget_custom_args(self):
        kwargs = {"fontsize": 14, "padding": 10}
        volume_widget = build_volume_widget(self.settings, kwargs)
        self.assertIsInstance(volume_widget, widget.Volume)
        self.assertEqual(volume_widget.fontsize, 14)
        self.assertEqual(volume_widget.padding, 10)

    @patch("ebenezer.widgets.volume.run_shell_command_stdout")
    def test_get_current_volume(self, mock_run_shell_command_stdout):
        mock_run_shell_command_stdout.return_value.stdout = "50%\n"
        result = _get_current_volume(self.settings)
        self.assertEqual(result, "50")

    @patch("ebenezer.widgets.volume.run_shell_command_stdout")
    def test_is_muted(self, mock_run_shell_command_stdout):
        mock_run_shell_command_stdout.return_value.stdout = "yes\n"
        result = _is_muted(self.settings)
        self.assertTrue(result)

    @patch("ebenezer.widgets.volume.push_notification_progress")
    @patch("ebenezer.widgets.volume._get_current_volume")
    def test_push_volume_notification(
        self, mock_get_current_volume, mock_push_notification_progress
    ):
        mock_get_current_volume.return_value = "50"
        _push_volume_notification(self.settings, "Volume")
        mock_push_notification_progress.assert_called_once_with(
            message="Volume 50%", progress=50
        )

    @patch("ebenezer.widgets.volume._get_current_volume")
    @patch("ebenezer.widgets.volume._unmute")
    @patch("ebenezer.widgets.volume.run_shell_command")
    def test_do_volume_up(
        self, mock_run_shell_command, mock_unmute, mock_get_current_volume
    ):
        mock_get_current_volume.return_value = "50"

        _do_volume_up(self.settings.commands.get("volume_up"), self.settings)

        mock_get_current_volume.assert_called_with(self.settings)
        mock_unmute.assert_called_once_with(self.settings)
        mock_run_shell_command.assert_called_once_with("echo 'Volume Up'")

    @patch("ebenezer.widgets.volume.run_shell_command")
    def test_do_volume_down(self, mock_run_shell_command):
        _do_volume_down(self.settings.commands.get("volume_down"), self.settings)

        mock_run_shell_command.assert_called_once_with("echo 'Volume Down'")

    @patch("ebenezer.widgets.volume.run_shell_command")
    @patch("ebenezer.widgets.volume.push_notification")
    def test_mute_toggle(self, mock_push_notification, mock_run_shell_command):
        _mute_toggle(self.settings)
        mock_run_shell_command.assert_called_once_with("echo 'Mute'")
        mock_push_notification.assert_called_once()

    @patch("ebenezer.widgets.volume.run_shell_command")
    @patch("ebenezer.widgets.volume.push_notification")
    def test_unmute(self, mock_push_notification, mock_run_shell_command):
        _unmute(self.settings, notify=True)
        mock_run_shell_command.assert_called_once_with("echo 'Mute Off'")
        mock_push_notification.assert_called_once_with("Volume 󰖁", "Muted")

    def test_setup_volume_keys(self):
        keys = setup_volume_keys(self.settings)
        self.assertEqual(len(keys), 7)


if __name__ == "__main__":
    unittest.main()
