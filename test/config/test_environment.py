from ebenezer.config.environment import AppSettingsEnvironment
from ebenezer.config.loader import load_raw_test_settings


def test_parse_environment():
    settings = load_raw_test_settings()
    environment = AppSettingsEnvironment(**settings.get("environment"))
    expected = AppSettingsEnvironment(
        mod="mod4",
        browser="firefox",
        terminal="kitty",
        wallpaper_dir="/home/foo/wallpapers",
        wallpaper_timeout="60",
        os_logo="/home/foo/logos/linux.svg",
        os_logo_icon="󰌽",
        os_logo_icon_color="fg_purple",
        theme="ebenezer",
        backlight_name="",
        weather_api_key="foo",
        city_id="1",
        rofi_home="/home/foo/.config/qtile/rofi",
        scripts="/home/foo/.config/qtile/scripts",
    )

    assert environment.__dict__ == expected.__dict__
