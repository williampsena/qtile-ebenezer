import unittest

from libqtile.widget import CPU

from ebenezer.config.settings import AppSettings
from ebenezer.widgets.cpu import ColorizedCPUWidget


class TestColorizedCPUWidget(unittest.TestCase):
    def setUp(self):
        self.settings = AppSettings()
        self.settings.colors.fg_normal = "#FFFFFF"
        self.settings.colors.fg_high = "#FF0000"
        self.settings.colors.fg_medium = "#FFFF00"
        self.settings.colors.fg_low = "#00FF00"

    def test_colorized_cpu_widget_default(self):
        config = {
            "settings": self.settings,
            "font": "FontAwesome",
            "fontsize": 12,
            "foreground": self.settings.colors.fg_normal,
        }
        cpu_widget = ColorizedCPUWidget(**config)
        self.assertIsInstance(cpu_widget, CPU)
        self.assertEqual(cpu_widget.font, "FontAwesome")
        self.assertEqual(cpu_widget.fontsize, 12)
        self.assertEqual(cpu_widget.foreground, "#FFFFFF")

    def test_colorized_cpu_widget_custom_args(self):
        config = {
            "settings": self.settings,
            "fontsize": 14,
            "foreground": "#000000",
        }
        cpu_widget = ColorizedCPUWidget(**config)
        self.assertIsInstance(cpu_widget, CPU)
        self.assertEqual(cpu_widget.fontsize, 14)
        self.assertEqual(cpu_widget.foreground, "#000000")


if __name__ == "__main__":
    unittest.main()
