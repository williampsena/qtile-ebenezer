import unittest
from typing import List

from libqtile.config import Key

from ebenezer.core.config.settings import AppSettings
from ebenezer.core.groups import build_groups


class TestBuildGroups(unittest.TestCase):
    def test_build_groups(self):
        settings = AppSettings()
        settings.environment.modkey = "mod4"
        settings.startup = ["command1", "command2"]

        keys: List[Key] = []

        build_groups(keys, settings)

        self.assertGreater(len(keys), 0)

        for vt in range(1, 8):
            self.assertTrue(any(key.key == str(vt) for key in keys))


if __name__ == "__main__":
    unittest.main()
