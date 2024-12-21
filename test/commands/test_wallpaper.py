import shutil
import tempfile
import unittest
from unittest.mock import MagicMock, patch

from click.testing import CliRunner

from ebenezer.commands.wallpaper import cli


class TestWallpaperCommands(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = tempfile.mkdtemp()
        self.tmp_file = tempfile.NamedTemporaryFile(
            delete=False, dir=self.tmp_dir, suffix=".jpg"
        ).name
        self.runner = CliRunner()

    def tearDown(self):
        shutil.rmtree(self.tmp_dir)

    @patch("ebenezer.commands.wallpaper.run")
    @patch("ebenezer.commands.wallpaper.click.echo")
    @patch("ebenezer.commands.wallpaper.Path")
    @patch("ebenezer.commands.wallpaper.random.choice")
    def test_set_wallpaper_with_directory(
        self, mock_random_choice, mock_path, mock_click_echo, mock_run
    ):
        mock_path_obj = MagicMock()
        mock_path.return_value = mock_path_obj
        mock_path_obj.is_dir.return_value = True
        mock_wallpaper = MagicMock()
        mock_path_obj.glob.return_value = [mock_wallpaper]
        mock_random_choice.return_value = mock_wallpaper

        result = self.runner.invoke(cli, ["set", self.tmp_dir])

        mock_path.assert_called_with(self.tmp_dir)
        mock_path_obj.is_dir.assert_called_once()
        mock_path_obj.glob.assert_called_once_with("*")
        mock_random_choice.assert_called_once_with([mock_wallpaper])
        mock_run.assert_called_once_with(
            f'feh --bg-scale "{mock_wallpaper}"', shell=True
        )
        mock_click_echo.assert_called_once_with(f'Wallpaper set to: "{mock_wallpaper}"')

    @patch("ebenezer.commands.wallpaper.run")
    @patch("ebenezer.commands.wallpaper.click.echo")
    @patch("ebenezer.commands.wallpaper.Path")
    def test_set_wallpaper_with_file(self, mock_path, mock_click_echo, mock_run):
        mock_path_obj = MagicMock()
        mock_path.return_value = mock_path_obj
        mock_path_obj.is_file.return_value = True
        mock_path_obj.is_dir.return_value = False

        result = self.runner.invoke(cli, ["set", self.tmp_file])

        mock_path.assert_called_with(self.tmp_file)
        mock_path_obj.is_file.assert_called_once()
        mock_run.assert_called_once_with(
            f'feh --bg-scale "{self.tmp_file}"', shell=True
        )
        mock_click_echo.assert_called_once_with(f'Wallpaper set to: "{self.tmp_file}"')

    def test_set_wallpaper_with_invalid_path(self):
        result = self.runner.invoke(cli, ["set", "/invalid/path"])
        self.assertEqual(result.exit_code, 2)

    @patch("ebenezer.commands.wallpaper._set_wallpaper")
    @patch("time.sleep")
    def test_random_wallpaper(self, mock_sleep, mock_set_wallpaper):
        mock_sleep.side_effect = lambda x: None

        self.runner.invoke(
            cli, ["random", "/tmp", "--timeout", "1", "--max-changes", 1]
        )
        mock_sleep.assert_called_with(1)

        mock_set_wallpaper.assert_called_with("/tmp")
        mock_sleep.assert_called_with(1)


if __name__ == "__main__":
    unittest.main()
