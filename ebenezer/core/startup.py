"""
startup.py
----------

This module provides functions to run startup commands for Qtile.

Functions:
    run_startup_once(settings: AppSettings):
        Runs startup commands defined in the settings.

    _env_substitutions(settings: AppSettings) -> dict[str, Any]:
        Returns a dictionary of environment substitutions based on the settings.
"""

from typing import Any

from libqtile.log_utils import logger

from ebenezer.config.settings import AppSettings
from ebenezer.core.command import run_shell_command

DEFAULT_TIMEOUT = 3


def run_startup_once(settings: AppSettings):
    """
    Runs startup commands defined in the settings.

    Args:
        settings (AppSettings): The application settings containing startup commands.
    """
    for raw_cmd in settings.startup:
        try:
            cmd = settings.startup[raw_cmd]
            run_shell_command(
                cmd, timeout=DEFAULT_TIMEOUT, **_env_substitutions(settings)
            )
            logger.info(f"the script {cmd} was loaded")
        except Exception as e:
            logger.warning(
                f"error while trying to run command {raw_cmd}", e, exc_info=True
            )


def _env_substitutions(settings: AppSettings) -> dict[str, Any]:
    """
    Returns a dictionary of environment substitutions based on the settings.

    Args:
        settings (AppSettings): The application settings containing environment configurations.

    Returns:
        dict[str, Any]: A dictionary of environment substitutions.
    """
    return {
        "lock_screen_timeout": settings.lock_screen.timeout,
        "wallpaper_dir": settings.environment.wallpaper_dir,
        "wallpaper_timeout": settings.environment.wallpaper_timeout * 60,
    }
