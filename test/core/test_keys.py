import unittest

from libqtile.config import Key

from ebenezer.config.keybindings import AppSettingsKeyBinding
from ebenezer.config.settings import AppSettings
from ebenezer.core.keys import _build_key_spawn


class TestBuildKeySpawn(unittest.TestCase):
    def test_build_key_spawn(self):
        settings = AppSettings()
        settings.environment.modkey = "mod4"

        binding = AppSettingsKeyBinding(
            name="test", keys="mod4 Return", action="spawn", command="xterm"
        )

        key = _build_key_spawn(settings, binding)

        self.assertIsInstance(key, Key)

        self.assertEqual(key.modifiers, ["mod4"])
        self.assertEqual(key.key, "Return")

        self.assertEqual(key.commands[0].args[0], "xterm")


if __name__ == "__main__":
    unittest.main()
