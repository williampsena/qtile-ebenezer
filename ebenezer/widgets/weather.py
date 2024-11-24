from libqtile import widget

from ebenezer.config.settings import AppSettings


def build_weather_widget(settings: AppSettings, kwargs: dict):
    """
    Build a weather widget using the provided settings and additional arguments.

    Args:
        settings (AppSettings): An instance of AppSettings containing configuration for fonts, colors, and environment.
        kwargs (dict): Additional keyword arguments to override the default widget settings.

    Returns:
        widget.OpenWeather: An instance of the OpenWeather widget configured with the specified settings.
    """
    default_args = {
        "font": settings.fonts.font_icon,
        "fontsize": settings.fonts.font_icon_size,
        "foreground": settings.colors.fg_normal,
        "padding": 2,
        "cityid": settings.environment.city_id,
        "app_key": settings.environment.weather_api_key,
        "location": "London",
        "format": "{icon}",
    }

    args = default_args | kwargs

    return widget.OpenWeather(**args)
