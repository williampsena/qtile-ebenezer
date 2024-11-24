import unittest
from unittest.mock import patch

from libqtile.widget import Memory

from ebenezer.config.settings import AppSettings
from ebenezer.widgets.memory import ColorizedMemoryWidget


class TestColorizedMemoryWidget(unittest.TestCase):
    def setUp(self):
        self.settings = AppSettings()
        self.settings.colors.fg_normal = "#FFFFFF"
        self.settings.monitoring.threshold_medium = 50
        self.settings.monitoring.threshold_high = 80
        self.settings.monitoring.default_color = "#FFFFFF"
        self.settings.monitoring.high_color = "#FF0000"
        self.settings.monitoring.medium_color = "#FFFF00"
        self.settings.colors.fg_low = "#00FF00"

    def test_colorized_memory_widget_default(self):
        config = {
            "settings": self.settings,
            "font": "FontAwesome",
            "fontsize": 12,
            "foreground": self.settings.colors.fg_normal,
        }
        memory_widget = ColorizedMemoryWidget(**config)
        self.assertIsInstance(memory_widget, Memory)
        self.assertEqual(memory_widget.font, "FontAwesome")
        self.assertEqual(memory_widget.fontsize, 12)
        self.assertEqual(memory_widget.foreground, "#FFFFFF")

    def test_colorized_memory_widget_custom_args(self):
        config = {
            "settings": self.settings,
            "fontsize": 14,
            "foreground": "#000000",
        }
        memory_widget = ColorizedMemoryWidget(**config)
        self.assertIsInstance(memory_widget, Memory)
        self.assertEqual(memory_widget.fontsize, 14)
        self.assertEqual(memory_widget.foreground, "#000000")

    @patch("ebenezer.widgets.memory.psutil.virtual_memory")
    @patch.object(Memory, "poll", return_value="75%")
    def test_colorized_memory_widget_update(self, mock_poll, mock_virtual_memory):
        config = {
            "settings": self.settings,
            "fontsize": 14,
            "foreground": "#000000",
            "high_color": "#FF0000",
            "medium_color": "#FFFF00",
        }
        memory_widget = ColorizedMemoryWidget(**config)
        mock_virtual_memory.return_value.percent = 75

        memory_widget.poll()

        self.assertEqual(
            memory_widget.foreground, self.settings.monitoring.medium_color
        )

    @patch("ebenezer.widgets.memory.psutil.virtual_memory")
    @patch.object(Memory, "poll", return_value="85%")
    def test_colorized_memory_widget_update_high(self, mock_poll, mock_virtual_memory):
        config = {
            "settings": self.settings,
            "fontsize": 14,
            "foreground": "#000000",
            "high_color": "#FF0000",
            "medium_color": "#FFFF00",
        }
        memory_widget = ColorizedMemoryWidget(**config)
        mock_virtual_memory.return_value.percent = 85

        memory_widget.poll()

        self.assertEqual(memory_widget.foreground, self.settings.monitoring.high_color)


if __name__ == "__main__":
    unittest.main()
