import unittest
from unittest.mock import MagicMock, patch

from ebenezer.commands.helpers import run_command


class TestHelpers(unittest.TestCase):

    @patch("ebenezer.commands.helpers.subprocess.run")
    def test_run_command_success(self, mock_subprocess_run):
        mock_result = MagicMock()
        mock_result.stdout = "command output"
        mock_subprocess_run.return_value = mock_result

        result = run_command("echo 'Hello, World!'")

        mock_subprocess_run.assert_called_once_with(
            "echo 'Hello, World!'", shell=True, capture_output=True, text=True
        )
        self.assertEqual(result, "command output")

    @patch("ebenezer.commands.helpers.subprocess.run")
    def test_run_command_failure(self, mock_subprocess_run):
        mock_result = MagicMock()
        mock_result.stdout = ""
        mock_result.stderr = "command error"
        mock_subprocess_run.return_value = mock_result

        result = run_command("invalid_command")

        mock_subprocess_run.assert_called_once_with(
            "invalid_command", shell=True, capture_output=True, text=True
        )
        self.assertEqual(result, "")


if __name__ == "__main__":
    unittest.main()
