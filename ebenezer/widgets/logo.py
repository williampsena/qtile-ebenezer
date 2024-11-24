from libqtile import qtile, widget

from ebenezer.config.settings import AppSettings
from ebenezer.core.files import resolve_file_path


def build_os_logo(settings: AppSettings):
    """
    Builds a list containing the OS logo widget based on the provided settings.

    Args:
        settings (AppSettings): The application settings containing environment configurations.

    Returns:
        list: A list containing the OS logo widget. If neither `os_logo_icon` nor `os_logo`
              is specified in the settings, an empty list is returned.
    """
    if settings.environment.os_logo_icon != "":
        return [_build_os_logo_icon(settings)]

    if settings.environment.os_logo != "":
        return [_build_os_logo_image(settings)]

    return []


def _build_os_logo_icon(settings: AppSettings):
    return widget.TextBox(
        settings.environment.os_logo_icon,
        font=settings.fonts.font_icon,
        fontsize=settings.fonts.font_icon_size,
        padding=10,
        foreground=settings.environment.os_logo_icon_color,
        name="os_logo",
        mouse_callbacks={
            "Button1": lambda: qtile.cmd_spawn(settings.environment.terminal)
        },
    )


def _build_os_logo_image(settings: AppSettings):
    return widget.Image(
        filename=resolve_file_path(settings.environment.os_logo),
        scale="False",
        mouse_callbacks={
            "Button1": lambda: qtile.cmd_spawn(settings.environment.terminal)
        },
    )
