from ebenezer.config.colors import AppSettingsColors
from ebenezer.config.environment import AppSettingsEnvironment
from ebenezer.config.fonts import AppSettingsFonts
from ebenezer.config.loader import load_raw_test_settings
from ebenezer.config.lock_screen import AppSettingsLockScreen
from ebenezer.config.monitoring import AppSettingsMonitoring
from ebenezer.config.scratchpads import AppSettingsScratchpads
from ebenezer.config.settings import AppSettings, load_settings


def test_parse_settings():
    raw_settings = load_raw_test_settings()
    settings = load_settings(raw_settings)
    expected = AppSettings(
        environment=AppSettingsEnvironment(
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
            scripts="/home/foo/.config/qtile/scripts",
        ),
        fonts=AppSettingsFonts(
            font="Fira Code Nerd Font Bold",
            font_regular="Fira Code Nerd Font Medium",
            font_light="Fira Code Nerd Font Light",
            font_strong="Fira Code Nerd Font Semibold",
            font_strong_bold="Fira Code Nerd Font Bold",
            font_size=14,
            font_icon="Fira Code Nerd Font Medium",
            font_icon_size=16,
        ),
        groups={
            "browsers": "",
            "terminal": "",
            "editors": "󰘐",
            "games": "",
            "files": "󰉋",
            "win": "󰍲",
        },
        layouts={"monadtall": {}, "max": {}, "tile": {"ratio": 1}, "floating": {}},
        groups_layout={"default": "monadtall", "win": "tile"},
        startup={
            "keyboard_layout": "setxkbmap -model abnt2 -layout br && localectl set-x11-keymap br",
            "dunst": "pkill dunst && dunst &",
        },
        floating={
            "title": ["ebenezer - configuration manager"],
            "wm_class": [
                "pavucontrol",
                "gnome-calculator",
            ],
        },
        colors=AppSettingsColors(
            fg_normal="#D8DEE9",
            fg_focus="#C4C7C5",
            fg_urgent="#CC9393",
            bg_normal="#263238",
            bg_focus="#1E2320",
            bg_urgent="#424242",
            bg_systray="#37444b",
            bg_selected="#5c6b73",
            fg_blue="#304FFE",
            fg_light_blue="#B3E5FC",
            fg_yellow="#FFFF00",
            fg_red="#D50000",
            fg_orange="#FFC107",
            fg_purple="#AA00FF",
            fg_green="#4BC1CC",
            fg_gray="#9db4c0",
            fg_black="#000000",
            fg_white="#ffffff",
            fg_selected="#AA00FF",
            bg_topbar="#282a36",
            bg_topbar_arrow="#5c6b73",
            bg_topbar_selected="#6200EA",
            border_color_normal="#AA00FF",
            border_color_active="#6200EA",
            border_color_marked="#c678dd",
            titlebar_bg_focus="#263238",
            titlebar_bg_normal="#253238",
            taglist_bg_focus="#37474F",
            group_focus="#e0fbfc",
            group_normal="#C4C7C5",
            lock_screen_blank_color="#00000000",
            lock_screen_clear_color="#ffffff22",
            lock_screen_default_color="#9db4c0",
            lock_screen_key_color="#8a8ea800",
            lock_screen_text_color="#4BC1CC",
            lock_screen_wrong_color="#D50000",
            lock_screen_verifying_color="#41445800",
            lock_screen_quote_foreground_color="#000",
            lock_screen_quote_text_color="#fff",
            theme=None,
        ),
        commands={
            "screenshot": "flameshot gui --clipboard --path ~/Pictures/Screenshots",
            "screenshot_full": "flameshot full --clipboard --path ~/Pictures/Screenshots",
            "change_wallpaper": "echo 'change wallpaper'",
        },
        lock_screen=AppSettingsLockScreen(
            command="~/.config/qtile/lock.py",
            timeout=10,
            font="Mononoki Nerd Font Bold",
            font_size=40,
            quote_font_path="/usr/share/fonts/TTF/MononokiNerdFont-Regular.ttf",
            quote_font_size=17,
            joke_providers="reddit,icanhazdad",
            icanhazdad_joke_url="https://icanhazdadjoke.com/",
            reddit_joke_url="https://www.reddit.com/r/ProgrammerDadJokes.json",
            blurtype="0x7",
        ),
        monitoring=AppSettingsMonitoring(
            default_color="fg_normal",
            high_color="fg_orange",
            medium_color="fg_yellow",
            threshold_medium=70,
            threshold_high=90,
            burn="yes",
        ),
        scratchpads=AppSettingsScratchpads(
            dropdowns={
                "term": {
                    "command": "kitty --name dropdown --title dropdown --class dropdown -e zsh",
                    "args": {
                        "opacity": 0.9,
                        "width": 0.7,
                        "height": 0.7,
                        "x": 0.15,
                        "y": 0.15,
                    },
                },
                "browser": {
                    "command": "firefox",
                    "args": {"width": 0.7, "height": 0.7, "x": 0.15, "y": 0.15},
                },
            }
        ),
    )

    assert settings.environment.__dict__ == expected.environment.__dict__
    assert settings.fonts.__dict__ == expected.fonts.__dict__
    assert settings.groups == expected.groups
    assert settings.groups_layout == expected.groups_layout
    assert settings.layouts == expected.layouts
    assert settings.startup == expected.startup
    assert settings.floating == expected.floating
    assert settings.colors.__dict__ == expected.colors.__dict__
    assert settings.commands == expected.commands
    assert settings.lock_screen.__dict__ == expected.lock_screen.__dict__
    assert settings.monitoring.__dict__ == expected.monitoring.__dict__
    assert (
        settings.scratchpads.dropdowns.get("browser").__dict__
        == expected.scratchpads.dropdowns.get("browser").__dict__
    )
    assert (
        settings.scratchpads.dropdowns.get("term").__dict__
        == expected.scratchpads.dropdowns.get("term").__dict__
    )
