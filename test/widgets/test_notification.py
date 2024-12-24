import unittest
from unittest.mock import MagicMock, patch

from ebenezer.config.settings import AppSettings
from ebenezer.widgets.notification import DunstWidget, build_notification_widget


class TestDunstWidget(unittest.TestCase):
    def setUp(self):
        self.settings = AppSettings()
        self.settings.fonts.font_icon = "FontAwesome"
        self.settings.fonts.font_icon_size = 12
        self.settings.colors.fg_normal = "#FFFFFF"
        self.settings.colors.fg_yellow = "#FFFF00"
        self.settings.commands = {"modal_confirm": "echo 'Confirm'"}

    @patch("ebenezer.widgets.notification.subprocess.run")
    @patch("ebenezer.widgets.notification.subprocess.check_output")
    def test_poll(self, mock_check_output, mock_run):
        mock_check_output.return_value = (
            "Waiting: 0\nCurrently displayed: 0\nHistory: 5".encode("utf-8")
        )
        widget = DunstWidget(settings=self.settings)
        result = widget.poll()
        self.assertEqual(result, "󰂚 5")

    @patch("ebenezer.widgets.notification.subprocess.Popen")
    def test_show_notifications(self, mock_popen):
        widget = DunstWidget(settings=self.settings)
        widget.show_notifications()
        mock_popen.assert_called_once_with(["dunstctl", "history-pop"])

    @patch("ebenezer.widgets.notification.subprocess.run")
    @patch("ebenezer.widgets.notification.confirm_cmd")
    def test_clear_notifications(self, mock_confirm_cmd, mock_run):
        def side_effect_confirm(cmd, *args, **kwargs):
            return True

        def side_effect_run(cmd, *args, **kwargs):
            return MagicMock(stdout="")

        mock_confirm_cmd.side_effect = side_effect_confirm
        mock_run.side_effect = side_effect_run

        widget = DunstWidget(settings=self.settings)
        widget.count = 5
        widget.clear_notifications()

        mock_run.assert_any_call("dunstctl history-clear", shell=True)

    def test_build_notification_widget_default(self):
        kwargs = {}
        notification_widget = build_notification_widget(self.settings, kwargs)
        self.assertIsInstance(notification_widget, DunstWidget)
        self.assertEqual(notification_widget.font, "FontAwesome")
        self.assertEqual(notification_widget.fontsize, 12)
        self.assertEqual(notification_widget.foreground, "#FFFFFF")


if __name__ == "__main__":
    unittest.main()
