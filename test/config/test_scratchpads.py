import unittest

from ebenezer.config.scratchpads import (
    AppSettingsScratchpads,
    AppSettingsScratchpadsDropdown,
)


class TestAppSettingsScratchpadsDropdown(unittest.TestCase):
    def test_initialization_with_defaults(self):
        dropdown = AppSettingsScratchpadsDropdown()
        self.assertEqual(dropdown.command, "")
        self.assertEqual(dropdown.args, {})

    def test_initialization_with_arguments(self):
        dropdown = AppSettingsScratchpadsDropdown(
            command="test_command", args={"key": "value"}
        )
        self.assertEqual(dropdown.command, "test_command")
        self.assertEqual(dropdown.args, {"key": "value"})


class TestAppSettingsScratchpads(unittest.TestCase):
    def test_initialization_with_defaults(self):
        scratchpads = AppSettingsScratchpads()
        self.assertEqual(scratchpads.dropdowns, {})

    def test_initialization_with_arguments(self):
        dropdowns = {
            "term": {"command": "alacritty", "args": {"width": 0.5}},
            "browser": {"command": "firefox", "args": {"height": 0.7}},
        }
        scratchpads = AppSettingsScratchpads(dropdowns=dropdowns)

        for name, settings in dropdowns.items():
            with self.subTest(dropdown=name):
                self.assertEqual(
                    scratchpads.dropdowns[name].__dict__,
                    {"name": name} | settings,
                )

    def test_update_dropdowns(self):
        scratchpads = AppSettingsScratchpads()
        dropdowns = {
            "editor": AppSettingsScratchpadsDropdown(
                command="vim", args={"fullscreen": True}
            ),
        }
        scratchpads.dropdowns = dropdowns
        self.assertEqual(scratchpads.dropdowns, dropdowns)
