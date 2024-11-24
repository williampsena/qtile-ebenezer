import unittest
from unittest.mock import MagicMock, patch

from libqtile import widget

from ebenezer.config.settings import AppSettings
from ebenezer.widgets.github import GitHubNotifications, _build_github_icon_widget


class TestGitHubNotifications(unittest.TestCase):
    def setUp(self):
        self.settings = AppSettings()
        self.settings.environment.github_notifications_token = "fake_token"

    @patch("ebenezer.widgets.github.request_retry")
    @patch("ebenezer.widgets.github.requests.get")
    def test_github_notifications_fetch(self, mock_requests_get, mock_request_retry):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [{"id": 1}, {"id": 2}]
        mock_requests_get.return_value = mock_response
        mock_request_retry.side_effect = lambda func: func()

        config = {
            "icon_widget": _build_github_icon_widget(self.settings, {}),
            "settings": self.settings,
            "update_interval": 60,
            "token": self.settings.environment.github_notifications_token,
        }
        github_widget = GitHubNotifications(**config)

        self.assertEqual(github_widget.poll(), "2+")

    @patch("ebenezer.widgets.github.request_retry")
    @patch("ebenezer.widgets.github.requests.get")
    def test_github_notifications_fetch_no_notifications(
        self, mock_requests_get, mock_request_retry
    ):
        mock_response = MagicMock()
        mock_response.json.return_value = []
        mock_requests_get.return_value = mock_response
        mock_request_retry.side_effect = lambda func, retries, delay: func()

        config = {
            "icon_widget": widget.TextBox(""),
            "settings": self.settings,
            "update_interval": 60,
            "token": self.settings.environment.github_notifications_token,
        }
        github_widget = GitHubNotifications(**config)

        self.assertEqual(github_widget.text, "")


if __name__ == "__main__":
    unittest.main()
