import unittest
from unittest.mock import patch

from ebenezer.core.notify import (
    push_notification,
    push_notification_no_history,
    push_notification_progress,
)


class TestNotify(unittest.TestCase):
    @patch("ebenezer.core.notify.run_shell_command")
    def test_push_notification(self, mock_run_shell_command):
        title = "Test Title"
        message = "Test Message"
        push_notification(title, message)
        mock_run_shell_command.assert_called_once_with(
            'notify-send -r 999 --urgency=low  "$title" "$message"',
            title=title,
            message=message,
        )

    @patch("ebenezer.core.notify.run_shell_command")
    def test_push_notification_progress(self, mock_run_shell_command):
        message = "Test Message"
        progress = 50
        push_notification_progress(message, progress)
        mock_run_shell_command.assert_called_once_with(
            'notify-send -r 999 --urgency=low  "$message" -h int:value:$progress',
            message=message,
            progress=str(progress),
        )

    @patch("ebenezer.core.notify.run_shell_command")
    def test_push_notification_no_history(self, mock_run_shell_command):
        title = "Test Title"
        message = "Test Message"
        push_notification_no_history(title, message)
        mock_run_shell_command.assert_called_once_with(
            'notify-send --urgency=low "$title" "$message"',
            title=title,
            message=message,
        )


if __name__ == "__main__":
    unittest.main()
