import unittest

from ebenezer.config.loader import TEST_CONFIG
from ebenezer.config.settings import load_settings_by_files
from ebenezer.core.wallpaper import change_wallpaper


class TestCoreWallpaper(unittest.TestCase):
    def test_change_wallpaper(self):
        settings = load_settings_by_files(config_filepath=TEST_CONFIG)
        change_wallpaper(settings)


if __name__ == "__main__":
    unittest.main()
