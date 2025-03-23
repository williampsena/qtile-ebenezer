import unittest
from typing import List

from libqtile.config import Key

from ebenezer.config.scratchpads import AppSettingsScratchpads
from ebenezer.config.settings import AppSettings
from ebenezer.core.groups import build_groups


class TestBuildGroups(unittest.TestCase):
    def test_build_groups(self):
        settings = AppSettings()
        settings.environment.modkey = "mod4"
        settings.startup = ["command1", "command2"]
        settings.groups = {
            "1": "Terminal",
            "2": "Web",
            "3": "Code",
            "4": "Files",
            "5": "Music",
            "6": "Video",
            "7": "Misc",
        }
        settings.scratchpads = AppSettingsScratchpads(
            dropdowns={
                "term": {"command": "alacritty", "args": {"width": 0.5}},
                "browser": {"command": "firefox", "args": {"height": 0.7}},
            }
        )
        keys: List[Key] = []

        groups, keys = build_groups(keys, settings)

        self.assertGreater(len(groups), 0)

        for vt in range(1, 8):
            self.assertTrue(any(key.key == str(vt) for key in keys))


if __name__ == "__main__":
    unittest.main()
