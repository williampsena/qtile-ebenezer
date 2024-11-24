import unittest

from libqtile.config import Screen

from ebenezer.config.settings import AppSettings
from ebenezer.core.screen import build_screen


class TestBuildScreen(unittest.TestCase):
    def test_build_screen_top(self):
        settings = AppSettings()
        settings.bar.position = "top"

        screen = build_screen(settings)

        self.assertIsInstance(screen, Screen)

        self.assertIsNotNone(screen.top)
        self.assertIsNone(screen.bottom)

    def test_build_screen_bottom(self):
        settings = AppSettings()
        settings.bar.position = "bottom"

        screen = build_screen(settings)

        self.assertIsInstance(screen, Screen)

        self.assertIsNotNone(screen.bottom)
        self.assertIsNone(screen.top)


if __name__ == "__main__":
    unittest.main()
