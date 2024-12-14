import unittest
from unittest.mock import MagicMock, patch

from typer.testing import CliRunner

from ebenezer.commands.wallpaper import app

runner = CliRunner()


class TestWallpaperCommands(unittest.TestCase):

    @patch("ebenezer.commands.wallpaper.run")
    @patch("ebenezer.commands.wallpaper.typer.echo")
    @patch("ebenezer.commands.wallpaper.Path")
    @patch("ebenezer.commands.wallpaper.random.choice")
    def test_set_wallpaper_with_directory(
        self, mock_random_choice, mock_path, mock_typer_echo, mock_run
    ):
        # Mock the Path object and its methods
        mock_path_obj = MagicMock()
        mock_path.return_value = mock_path_obj
        mock_path_obj.is_dir.return_value = True
        mock_wallpaper = MagicMock()
        mock_path_obj.glob.return_value = [mock_wallpaper]
        mock_random_choice.return_value = mock_wallpaper

        # Invoke the set_wallpaper command
        result = runner.invoke(app, ["set", "/path/to/wallpapers"])

        # Assertions
        mock_path.assert_called_with("/path/to/wallpapers")
        mock_path_obj.is_dir.assert_called_once()
        mock_path_obj.glob.assert_called_once_with("*")
        mock_random_choice.assert_called_once_with([mock_wallpaper])
        mock_run.assert_called_once_with(f"feh --bg-scale {mock_wallpaper}", shell=True)
        mock_typer_echo.assert_called_once_with(f"Wallpaper set to: {mock_wallpaper}")

    @patch("ebenezer.commands.wallpaper.run")
    @patch("ebenezer.commands.wallpaper.typer.echo")
    @patch("ebenezer.commands.wallpaper.Path")
    def xtest_set_wallpaper_with_file(self, mock_path, mock_typer_echo, mock_run):
        mock_path_obj = MagicMock()
        mock_path.return_value = mock_path_obj
        mock_path_obj.is_file.return_value = True

        result = runner.invoke(app, ["set", "/path/to/wallpaper.jpg"])

        mock_path.assert_called_with("/path/to/wallpaper.jpg")
        mock_path_obj.is_file.assert_called_once()
        mock_run.assert_called_once_with(
            "feh --bg-scale /path/to/wallpaper.jpg", shell=True
        )
        mock_typer_echo.assert_called_once_with(
            "Wallpaper set to: /path/to/wallpaper.jpg"
        )

    @patch("ebenezer.commands.wallpaper.run")
    @patch("ebenezer.commands.wallpaper.typer.echo")
    @patch("ebenezer.commands.wallpaper.Path")
    def test_set_wallpaper_with_invalid_path(
        self, mock_path, mock_typer_echo, mock_run
    ):
        # Mock the Path object and its methods
        mock_path_obj = MagicMock()
        mock_path.return_value = mock_path_obj
        mock_path_obj.is_dir.return_value = False
        mock_path_obj.is_file.return_value = False

        # Invoke the set_wallpaper command
        result = runner.invoke(app, ["set", "/invalid/path"])

        # Assertions
        mock_path.assert_called_with("/invalid/path")
        mock_path_obj.is_dir.assert_called_once()
        mock_path_obj.is_file.assert_called_once()
        mock_typer_echo.assert_called_once_with("No wallpaper file is found")
        mock_run.assert_not_called()

    @patch("ebenezer.commands.wallpaper.set_wallpaper")
    @patch("time.sleep")
    def test_random_wallpaper(self, mock_sleep, mock_set_wallpaper):
        mock_sleep.side_effect = lambda x: None

        runner.invoke(
            app, ["random", "/path/to/wallpapers", "--timeout", "1", "--max-changes", 1]
        )
        mock_sleep.assert_called_with(1)

        mock_set_wallpaper.assert_called_with("/path/to/wallpapers")
        mock_sleep.assert_called_with(1)


if __name__ == "__main__":
    unittest.main()
