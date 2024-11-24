"""
wallpaper.py
------------

This module provides functions to change the wallpaper.

Functions:
    change_wallpaper(settings: AppSettings):
        Changes the wallpaper based on the provided settings.
"""

import subprocess
from string import Template

from ebenezer.config.settings import AppSettings
from ebenezer.core.files import resolve_file_path


def change_wallpaper(settings: AppSettings):
    """
    Changes the wallpaper based on the provided settings.

    Args:
        settings (AppSettings): The application settings containing wallpaper configurations.
    """
    change_wallpaper_cmd = settings.commands.get("change_wallpaper")

    if change_wallpaper_cmd is None:
        return

    cmd_template = Template(resolve_file_path(change_wallpaper_cmd))
    cmd = (
        cmd_template.substitute(
            wallpaper_dir=settings.environment.wallpaper_dir,
            wallpaper_timeout=settings.environment.wallpaper_timeout * 60,
        )
        .strip()
        .split(" ")
    )

    subprocess.call(cmd)
