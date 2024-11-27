"""
environment.py
--------------

This module provides a class to manage environment settings for Qtile.

Classes:
    AppSettingsEnvironment:
        Manages environment settings including modkey, browser, terminal, and other configurations.
"""

from libqtile.utils import guess_terminal

from ebenezer.core.files import resolve_file_path


class AppSettingsEnvironment:
    modkey: str = "mod4"
    browser: str = "firefox"
    terminal: str = guess_terminal() or "xterm"
    wallpaper_dir: str = ""
    wallpaper_timeout: int = 60
    os_logo: str = ""
    os_logo_icon: str = ""
    os_logo_icon_color: str = ""
    theme: str = "ebenezer"
    backlight_name: str = ""
    weather_api_key: str = ""
    city_id: str = ""
    github_notifications_token: str = ""
    rofi_home: str = ""
    scripts: str = ""

    def __init__(self, **kwargs: object):
        """
        Initializes the AppSettingsEnvironment with optional keyword arguments.

        Args:
            **kwargs: Arbitrary keyword arguments to initialize the environment settings.
        """
        self.modkey = str(kwargs.get("modkey", self.modkey))
        self.browser = str(kwargs.get("browser", self.browser))
        self.terminal = str(kwargs.get("terminal", self.terminal))
        self.wallpaper_dir = resolve_file_path(
            str(kwargs.get("wallpaper_dir", self.wallpaper_dir))
        )
        self.wallpaper_timeout = int(
            str(kwargs.get("wallpaper_timeout", self.wallpaper_timeout))
        )
        self.theme = str(kwargs.get("theme", self.theme))
        self.os_logo = str(kwargs.get("os_logo", self.os_logo))
        self.os_logo_icon = str(kwargs.get("os_logo_icon", self.os_logo_icon))
        self.os_logo_icon_color = str(
            kwargs.get("os_logo_icon_color", self.os_logo_icon_color)
        )
        self.weather_api_key = str(kwargs.get("weather_api_key", self.weather_api_key))
        self.city_id = str(kwargs.get("city_id", self.city_id))
        self.github_notifications_token = str(
            kwargs.get("github_notifications_token", self.github_notifications_token)
        )
        self.rofi_home = str(kwargs.get("rofi_home", self.rofi_home))
        self.scripts = str(kwargs.get("scripts", self.scripts))
