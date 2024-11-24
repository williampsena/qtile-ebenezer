import unittest

from libqtile import widget

from ebenezer.config.settings import AppSettings
from ebenezer.widgets.weather import build_weather_widget


class TestBuildWeatherWidget(unittest.TestCase):
    def setUp(self):
        self.settings = AppSettings()
        self.settings.fonts.font_icon = "FontAwesome"
        self.settings.fonts.font_icon_size = 12
        self.settings.colors.fg_normal = "#FFFFFF"
        self.settings.environment.city_id = "123456"
        self.settings.environment.weather_api_key = "fake_api_key"

    def test_build_weather_widget_default(self):
        kwargs = {}
        weather_widget = build_weather_widget(self.settings, kwargs)
        self.assertIsInstance(weather_widget, widget.OpenWeather)
        self.assertEqual(weather_widget.font, "FontAwesome")
        self.assertEqual(weather_widget.fontsize, 12)
        self.assertEqual(weather_widget.foreground, "#FFFFFF")
        self.assertEqual(weather_widget.cityid, "123456")
        self.assertEqual(weather_widget.app_key, "fake_api_key")
        self.assertEqual(weather_widget.location, "London")
        self.assertEqual(weather_widget.format, "{icon}")

    def test_build_weather_widget_custom_args(self):
        kwargs = {"fontsize": 14, "location": "New York"}
        weather_widget = build_weather_widget(self.settings, kwargs)
        self.assertIsInstance(weather_widget, widget.OpenWeather)
        self.assertEqual(weather_widget.fontsize, 14)
        self.assertEqual(weather_widget.location, "New York")


if __name__ == "__main__":
    unittest.main()
