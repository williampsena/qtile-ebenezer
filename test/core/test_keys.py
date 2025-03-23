import unittest

from libqtile.config import Key

from ebenezer.config.keybindings import AppSettingsKeyBinding
from ebenezer.config.scratchpads import AppSettingsScratchpads
from ebenezer.config.settings import AppSettings
from ebenezer.core.keys import (
    _build_key_dropdown,
    _build_key_spawn,
    fetch_keybindings_text,
)


class TestBuildKey(unittest.TestCase):
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

    def test_build_key_dropdown(self):
        settings = AppSettings()
        settings.environment.modkey = "mod4"
        settings.scratchpads = AppSettingsScratchpads(
            dropdowns={
                "xterm": {"command": "alacritty", "args": {"width": 0.5}},
            }
        )

        binding = AppSettingsKeyBinding(
            name="test", keys="mod4 Return", action="dropdown", command="xterm"
        )

        key = _build_key_dropdown(settings, binding)

        self.assertIsInstance(key, Key)

        self.assertEqual(key.modifiers, ["mod4"])
        self.assertEqual(key.key, "Return")
        self.assertEqual(key.commands[0].args[0], "xterm")

    def test_fetch_keybindings_text(self):
        settings = AppSettings()
        settings.environment.modkey = "mod4"

        settings.keybindings = [
            AppSettingsKeyBinding(
                name="test", keys="mod4 Return", action="spawn", command="xterm"
            )
        ]

        text = fetch_keybindings_text(settings)

        self.assertIn(
            "mod4 + \U000f0311 enter",
            text,
        )

        self.assertIn(
            "test",
            text,
        )


if __name__ == "__main__":
    unittest.main()
