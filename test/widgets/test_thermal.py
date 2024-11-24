import unittest
from unittest.mock import MagicMock, patch

from libqtile import widget
from libqtile.widget import ThermalSensor

from ebenezer.config.settings import AppSettings
from ebenezer.widgets.thermal import (
    ColorizedThermalWidget,
    _get_temperature,
    build_thermal_widget,
)


class TestColorizedThermalWidget(unittest.TestCase):
    def setUp(self):
        self.settings = AppSettings()
        self.settings.fonts.font_icon = "FontAwesome"
        self.settings.fonts.font_size = 10
        self.settings.fonts.font_icon_size = 10
        self.settings.monitoring.default_color = "#FFFFFF"
        self.settings.monitoring.high_color = "#FF0000"
        self.settings.monitoring.medium_color = "#FFFF00"
        self.settings.monitoring.threshold_medium = 50
        self.settings.monitoring.threshold_high = 70
        self.settings.colors.fg_normal = "#FFFFFF"
        self.settings.colors.fg_light_blue = "#00FFFF"
        self.settings.colors.bg_topbar_arrow = "#000000"

    def test_colorized_thermal_widget_default(self):
        config = {
            "settings": self.settings,
            "font": "FontAwesome",
            "fontsize": 10,
            "foreground": self.settings.colors.fg_normal,
        }
        thermal_widget = ColorizedThermalWidget(**config)
        self.assertIsInstance(thermal_widget, ThermalSensor)
        self.assertEqual(thermal_widget.font, "FontAwesome")
        self.assertEqual(thermal_widget.fontsize, 10)
        self.assertEqual(thermal_widget.foreground, "#FFFFFF")

    def test_colorized_thermal_widget_custom_args(self):
        config = {
            "settings": self.settings,
            "fontsize": 14,
            "font": "FontAwesome",
            "foreground": "#000000",
            "icon": {
                "fontsize": 14,
                "font": "FontAwesome",
            },
        }
        thermal_widget = ColorizedThermalWidget(**config)
        self.assertIsInstance(thermal_widget, ThermalSensor)
        self.assertEqual(thermal_widget.fontsize, 14)
        self.assertEqual(thermal_widget.foreground, "#000000")

    @patch("ebenezer.widgets.thermal.psutil.sensors_temperatures")
    def test_get_temperature(self, mock_sensors_temperatures):
        mock_sensors_temperatures.return_value = {
            "coretemp": [
                MagicMock(label="Core 0", current=55.0),
                MagicMock(label="Core 1", current=60.0),
            ]
        }
        result = _get_temperature()
        self.assertEqual(result, 55.0)

    @patch("ebenezer.widgets.thermal.ThermalSensor.poll", return_value="75°C")
    def test_colorized_thermal_widget_poll(self, mock_poll):
        config = {
            "settings": self.settings,
            "fontsize": 14,
            "foreground": "#000000",
        }
        thermal_widget = ColorizedThermalWidget(**config)
        result = thermal_widget.poll()
        self.assertEqual(result, "🔥 75°C")
        self.assertEqual(thermal_widget.foreground, self.settings.monitoring.high_color)

    def test_build_thermal_widget_default(self):
        kwargs = {"fontsize": 10}
        thermal_widgets = build_thermal_widget(self.settings, kwargs)
        self.assertEqual(len(thermal_widgets), 2)
        self.assertIsInstance(thermal_widgets[0], widget.TextBox)
        self.assertIsInstance(thermal_widgets[1], ColorizedThermalWidget)
        self.assertEqual(thermal_widgets[0].text, "󱃂")
        self.assertEqual(thermal_widgets[1].font, "FontAwesome")
        self.assertEqual(thermal_widgets[1].fontsize, 10)
        self.assertEqual(thermal_widgets[1].foreground, "#FFFFFF")

    def test_build_thermal_widget_custom_args(self):
        kwargs = {"sensor": {"fontsize": 14}, "icon": {"text": "󱃂 Custom"}}
        thermal_widgets = build_thermal_widget(self.settings, kwargs)
        self.assertEqual(len(thermal_widgets), 2)
        self.assertIsInstance(thermal_widgets[0], widget.TextBox)
        self.assertIsInstance(thermal_widgets[1], ColorizedThermalWidget)
        self.assertEqual(thermal_widgets[0].text, "󱃂 Custom")
        self.assertEqual(thermal_widgets[1].fontsize, 14)


if __name__ == "__main__":
    unittest.main()
