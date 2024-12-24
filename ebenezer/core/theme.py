"""
theme.py
--------

This module provides functions to apply themes and styles for Qtile.

Functions:
    preload_colors(settings: AppSettings) -> AppSettings:
        Preloads colors and applies theme settings.

    _apply_theme_color(theme_filepath: str, settings: AppSettings) -> AppSettings:
        Applies theme colors from a YAML file.

    _apply_rofi_style(settings: AppSettings):
        Applies the Rofi style based on the provided settings.

    _extract_rasi_colors(colors: AppSettingsColors) -> str:
        Extracts Rasi colors from the settings.

    _apply_dusnt_style(settings: AppSettings):
        Applies the Dunst style based on the provided settings.
"""

from pathlib import Path
from string import Template
from typing import NamedTuple

from libqtile.log_utils import logger

from ebenezer.config.settings import AppSettings, AppSettingsColors
from ebenezer.core.dict import merge_dicts_recursive
from ebenezer.core.files import resolve_file_path
from ebenezer.core.yaml import read_yaml_file


class RofiTemplate(NamedTuple):
    template: str
    target: int


ROFI_TEMPLATES: list[RofiTemplate] = [
    RofiTemplate(
        template="$rofi_home/_vars.template.rasi",
        target="$home/.config/rofi/_qtile_theme.rasi",
    )
]
DUNSTRC_HOME_PATH = "$home/.config/dunst"

DUNSTRC_HOME_PATH = "$home/.config/dunst"


def preload_colors(settings: AppSettings, complete=False) -> AppSettings:
    """
    Preloads colors and applies theme settings.

    Args:
        settings (AppSettings): The application settings containing theme configurations.
        complete (bool): If True, applies the complete theme settings (dunst, rofi, etc.).

    Returns:
        AppSettings: The updated application settings with applied theme.
    """
    settings = apply_theme_color(settings)

    if complete:
        _apply_rofi_style(settings)
        _apply_dusnt_style(settings)

    return settings


def apply_theme_color(settings: AppSettings) -> AppSettings:
    """
    Applies the theme color to the given application settings.

    Args:
        settings (AppSettings): The application settings that include color configurations.

    Returns:
        AppSettings: The updated application settings with the applied theme color.
    """
    theme = settings.colors.theme

    if theme:
        settings = _apply_theme_color(theme, settings)

    return settings


def _apply_theme_color(raw_theme_filepath: str, settings: AppSettings) -> AppSettings:
    """
    Applies theme colors from a YAML file.

    Args:
        theme_filepath (str): The path to the theme YAML file.
        settings (AppSettings): The application settings to be updated.

    Returns:
        AppSettings: The updated application settings with applied theme colors.
    """
    try:
        theme_filepath = resolve_file_path(raw_theme_filepath)

        if not Path(theme_filepath).exists():
            logger.warning(f"Not found the selected theme {theme_filepath}.")
            return settings

        theme_config = read_yaml_file(resolve_file_path(theme_filepath))

        args = merge_dicts_recursive(
            settings.colors.raw, theme_config.get("colors", {})
        )

        settings.colors = AppSettingsColors(**args)
        settings.colors.theme = raw_theme_filepath

        return settings
    except Exception as e:
        logger.warning("error while trying to apply selected theme", e, exc_info=True)
        return settings


def _apply_rofi_style(settings: AppSettings):
    """
    Applies the Rofi style based on the provided settings.

    Args:
        settings (AppSettings): The application settings containing Rofi style configurations.
    """
    try:
        colors = {
            "font": f"{settings.fonts.rofi_font} {settings.fonts.rofi_font_size}",
            "background": settings.colors.rofi_background,
            "background_alt": settings.colors.rofi_background_alt,
            "foreground": settings.colors.rofi_foreground,
            "selected": settings.colors.rofi_selected,
            "active": settings.colors.rofi_active,
            "urgent": settings.colors.rofi_urgent,
            "border": settings.colors.rofi_border,
            "border_alt": settings.colors.rofi_border_alt,
            "colors": _extract_rasi_colors(settings.colors),
        }

        for template in ROFI_TEMPLATES:
            template_file = resolve_file_path(template.template)
            target_file = resolve_file_path(template.target)

            with open(template_file, "r") as f:
                cmd_template = Template(f.read())
                content = cmd_template.safe_substitute(colors).strip()

                with open(target_file, "w") as f:
                    f.write(content)
    except Exception as e:
        logger.warning("error while trying to build rofi style", e, exc_info=True)


def _extract_rasi_colors(colors: AppSettingsColors) -> str:
    """
    Extracts Rasi colors from the settings.

    Args:
        colors (AppSettingsColors): The application settings containing color configurations.

    Returns:
        str: The extracted Rasi colors as a string.
    """
    colors_list = [
        f"    {color.replace("_", "-")}: {value};"
        for color, value in colors.raw.items()
    ]
    return "\n".join(colors_list)


def _apply_dusnt_style(settings: AppSettings):
    """
    Applies the Dunst style based on the provided settings.

    Args:
        settings (AppSettings): The application settings containing Dunst style configurations.
    """
    try:
        template_file = resolve_file_path(f"{DUNSTRC_HOME_PATH}/dunstrcbaserc")
        target_file = resolve_file_path(f"{DUNSTRC_HOME_PATH}/dunstrc")

        style = {
            "font": f"{settings.fonts.font_notification} {settings.fonts.font_notification_size}",
            "background": settings.colors.bg_normal,
            "foreground": settings.colors.fg_normal,
            "frame_color": settings.colors.fg_normal,
            "highlight_color": settings.colors.fg_selected,
            "urgency_low_background": settings.colors.bg_normal,
            "urgency_low_foreground": settings.colors.fg_normal,
            "urgency_normal_background": settings.colors.bg_normal,
            "urgency_normal_foreground": settings.colors.fg_normal,
            "urgency_critical_background": settings.colors.bg_urgent,
            "urgency_critical_foreground": settings.colors.fg_urgent,
            "urgency_critical_frame_color": settings.colors.border_color_marked,
        }

        with open(resolve_file_path(template_file), "r") as f:
            cmd_template = Template(f.read())
            content = cmd_template.safe_substitute(style).strip()

            with open(resolve_file_path(target_file), "w") as f:
                f.write(content)
    except Exception as e:
        logger.warning("error while trying to build dusnt style", e, exc_info=True)
