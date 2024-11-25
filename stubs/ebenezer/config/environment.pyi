from ebenezer.core.files import resolve_file_path as resolve_file_path

class AppSettingsEnvironment:
    modkey: str
    browser: str
    terminal: str
    wallpaper_dir: str
    wallpaper_timeout: int
    os_logo: str
    os_logo_icon: str
    os_logo_icon_color: str
    theme: str
    backlight_name: str
    weather_api_key: str
    city_id: str
    github_notifications_token: str
    def __init__(self, **kwargs: object) -> None: ...
