import unittest
from unittest.mock import MagicMock, patch

import pytest
import ttkbootstrap as ttk

from ebenezer.config.settings import AppSettings
from ebenezer.ui.settings.about_frame import AboutFrame


@pytest.mark.ui
class TestAboutFrame(unittest.TestCase):

    @patch("ebenezer.ui.settings.about_frame.build_fonts")
    @patch("ebenezer.ui.settings.about_frame.build_label")
    @patch("ebenezer.ui.settings.about_frame.importlib.metadata.version")
    def test_about_frame(self, mock_version, mock_build_label, mock_build_fonts):
        mock_version.return_value = "1.0.0"
        mock_build_fonts.return_value = MagicMock()
        mock_build_label.return_value = MagicMock()

        settings = MagicMock(spec=AppSettings)
        settings.colors.fg_selected = "white"
        settings.colors.fg = "black"

        app = ttk.Window(themename="darkly")
        about_frame = AboutFrame(settings, app, app)

        mock_version.assert_called_once_with("qtile-ebenezer")
        self.assertEqual(about_frame._version(), "1.0.0")


if __name__ == "__main__":
    unittest.main()
