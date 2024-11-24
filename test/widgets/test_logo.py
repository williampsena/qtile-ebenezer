import unittest
from unittest.mock import patch

from ebenezer.config.settings import AppSettings
from ebenezer.widgets.logo import build_os_logo


class TestBuildOsLogo(unittest.TestCase):
    def setUp(self):
        self.settings = AppSettings()
        self.settings.environment.os_logo_icon = ""
        self.settings.environment.os_logo = ""

    @patch("ebenezer.widgets.logo._build_os_logo_icon")
    def test_build_os_logo_with_icon(self, mock_build_os_logo_icon):
        self.settings.environment.os_logo_icon = ""
        mock_build_os_logo_icon.return_value = "icon_widget"

        result = build_os_logo(self.settings)

        self.assertEqual(result, ["icon_widget"])
        mock_build_os_logo_icon.assert_called_once_with(self.settings)

    @patch("ebenezer.widgets.logo._build_os_logo_image")
    def test_build_os_logo_with_image(self, mock_build_os_logo_image):
        self.settings.environment.os_logo = "/path/to/logo.png"
        mock_build_os_logo_image.return_value = "image_widget"

        result = build_os_logo(self.settings)

        self.assertEqual(result, ["image_widget"])
        mock_build_os_logo_image.assert_called_once_with(self.settings)

    def test_build_os_logo_empty(self):
        result = build_os_logo(self.settings)
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
