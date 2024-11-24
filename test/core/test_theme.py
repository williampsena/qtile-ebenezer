import os
import tempfile
import unittest

from ebenezer.config.settings import AppSettings, AppSettingsColors
from ebenezer.core.theme import _apply_theme_color


class TestApplyThemeColor(unittest.TestCase):
    def test_apply_theme_color(self):
        with tempfile.NamedTemporaryFile(
            delete=False, mode="w", suffix=".yaml"
        ) as temp_file:
            temp_file.write(
                """
            colors:
              fg_normal: "#FFFFFF"
              fg_focus: "#123456"
            """
            )
            theme_filepath = temp_file.name

        try:
            settings = AppSettings()
            settings.colors = AppSettingsColors(raw={"fg_focus": "#000000"})

            updated_settings = _apply_theme_color(theme_filepath, settings)

            self.assertEqual(updated_settings.colors.fg_focus, "#123456")
            self.assertEqual(updated_settings.colors.fg_normal, "#FFFFFF")
        finally:
            os.remove(theme_filepath)

    def test_apply_theme_color_file_not_found(self):
        settings = AppSettings()
        settings.colors = AppSettingsColors(raw={"fg_focus": "#000000"})

        theme_filepath = "/path/to/non_existent_theme.yaml"

        updated_settings = _apply_theme_color(theme_filepath, settings)

        self.assertEqual(updated_settings.colors.fg_focus, "#fff")


if __name__ == "__main__":
    unittest.main()
