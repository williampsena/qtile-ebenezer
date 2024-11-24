import unittest
from unittest.mock import patch

from ebenezer.config.settings import AppSettings
from ebenezer.core.startup import run_startup_once


class TestRunStartupOnce(unittest.TestCase):
    @patch("ebenezer.core.startup.run_shell_command")
    @patch("ebenezer.core.startup._env_substitutions")
    def test_run_startup_once(self, mock_env_substitutions, mock_run_shell_command):
        settings = AppSettings()
        settings.startup = {
            "command1": "echo 'Running command1'",
            "command2": "echo 'Running command2'",
        }

        mock_env_substitutions.return_value = {"key": "value"}

        run_startup_once(settings)

        mock_run_shell_command.assert_any_call(
            "echo 'Running command1'", timeout=3, key="value"
        )
        mock_run_shell_command.assert_any_call(
            "echo 'Running command2'", timeout=3, key="value"
        )

        mock_env_substitutions.assert_called_with(settings)


if __name__ == "__main__":
    unittest.main()
