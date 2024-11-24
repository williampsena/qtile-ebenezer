import unittest

from libqtile import widget

from ebenezer.config.settings import AppSettings
from ebenezer.widgets.battery import build_battery_widget


class TestBuildBatteryWidget(unittest.TestCase):
    def setUp(self):
        self.settings = AppSettings()
        self.settings.fonts.font_icon = "FontAwesome"
        self.settings.fonts.font_icon_size = 12

    def test_build_battery_widget_default(self):
        kwargs = {}
        battery_widget = build_battery_widget(self.settings, kwargs)
        self.assertIsInstance(battery_widget, widget.Battery)
        self.assertEqual(battery_widget.font, "FontAwesome")
        self.assertEqual(battery_widget.fontsize, 12)
        self.assertEqual(battery_widget.format, "{char} {percent:2.0%}")
        self.assertEqual(battery_widget.charge_char, "")
        self.assertEqual(battery_widget.discharge_char, " ")
        self.assertEqual(battery_widget.empty_char, " ")
        self.assertEqual(battery_widget.full_char, " ")
        self.assertEqual(battery_widget.not_charging_char, "󰚦")

    def test_build_battery_widget_custom_args(self):
        kwargs = {"fontsize": 14, "format": "{char} {percent:1.0%}"}
        battery_widget = build_battery_widget(self.settings, kwargs)
        self.assertIsInstance(battery_widget, widget.Battery)
        self.assertEqual(battery_widget.fontsize, 14)
        self.assertEqual(battery_widget.format, "{char} {percent:1.0%}")


if __name__ == "__main__":
    unittest.main()
