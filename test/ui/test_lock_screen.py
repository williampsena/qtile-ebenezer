import os
import subprocess
import unittest
from unittest.mock import MagicMock, patch

from PIL import Image

from ebenezer.config.settings import AppSettings
from ebenezer.ui.lock_screen import _build_background
from ebenezer.ui.lock_screen import main as lock_screen


class TestLockScreen(unittest.TestCase):
    def setUp(self):
        self.settings = AppSettings()
        self.settings.lock_screen.timeout = 10
        self.quote_file = "/tmp/quote.png"
        self.output_file = "/tmp/i3lock.png"

        image = Image.new("RGB", (1920, 1080), self.settings.colors.bg_normal)
        image.save(self.output_file)
        image.save(self.quote_file)

    def tearDown(self):
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    @patch("ebenezer.ui.lock_screen.ImageFont.truetype")
    @patch("ebenezer.ui.lock_screen.ImageDraw.Draw")
    @patch("ebenezer.ui.lock_screen.Image.new")
    def xtest_build_background(
        self, mock_image_new, mock_image_draw, mock_imagefont_truetype
    ):
        mock_image = MagicMock(spec=Image.Image)
        mock_image_new.return_value = mock_image
        mock_draw = MagicMock()
        mock_image_draw.return_value = mock_draw
        mock_font = MagicMock()
        mock_imagefont_truetype.return_value = mock_font

        _build_background(self.settings, self.output_file)

        mock_image_new.assert_called_once_with("RGB", (1920, 1080), color="#000")
        mock_image_draw.assert_called_once_with(mock_image)
        mock_imagefont_truetype.assert_called_once_with("", 17)
        mock_draw.text.assert_called_once()
        mock_image.save.assert_called_once_with(self.quote_file)

    @patch("ebenezer.ui.lock_screen._build_background")
    @patch("ebenezer.ui.lock_screen.subprocess.Popen")
    @patch("ebenezer.ui.lock_screen.subprocess.run")
    def test_lock_screen(
        self, mock_subprocess_run, mock_subprocess_popen, mock_build_background
    ):
        def side_effect_run(cmd, *args, **kwargs):
            if cmd == ["pgrep", "i3lock"]:
                raise subprocess.CalledProcessError(1, cmd)
            return MagicMock(stdout=None)

        mock_subprocess_run.side_effect = side_effect_run
        mock_subprocess_popen.return_value = MagicMock(stdout=None)
        mock_build_background.return_value = None

        lock_screen(settings=self.settings)
        self.assertTrue(
            any(
                call[0][0][0] == "i3lock"
                for call in mock_subprocess_popen.call_args_list
            )
        )

    @patch("ebenezer.ui.lock_screen.subprocess.run")
    def xtest_lock_screen_skip(self, mock_subprocess_run):
        mock_subprocess_run.return_value = MagicMock(stdout=b"1234\n")
        lock_screen(settings=self.settings, startup=False)

        mock_subprocess_run.assert_called_once_with(
            ["pgrep", "i3lock"], stdout=-1, timeout=None, check=True
        )

        self.assertFalse(
            any(
                call[0][0][0] == "i3lock" for call in mock_subprocess_run.call_args_list
            )
        )


if __name__ == "__main__":
    unittest.main()
