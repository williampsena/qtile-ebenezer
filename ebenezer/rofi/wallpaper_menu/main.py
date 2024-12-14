#!/usr/bin/env python3

import importlib.resources as pkg_resources
import os
import subprocess

from ebenezer.config.settings import load_settings_by_files
from ebenezer.core.wallpaper import change_wallpaper

CHANGE_WALLPAPER_OPTION = "󰑓 Change Wallpaper"
CANCEL_OPTION = " Cancel"


def get_base_dir():
    return os.path.realpath(os.path.join(os.getcwd(), ".."))


def rofi_menu(options, prompt, theme):
    command = ["rofi", "-dmenu", "-p", prompt, "-theme", theme]
    result = subprocess.run(
        command, input="\n".join(options).encode(), stdout=subprocess.PIPE
    )
    return result.stdout.decode("utf-8").strip()


def main():
    settings = load_settings_by_files()

    options = [CHANGE_WALLPAPER_OPTION, CANCEL_OPTION]
    theme_file = pkg_resources.files("ebenezer.rofi.wallpaper_menu").joinpath(
        "theme.rasi"
    )
    chosen = rofi_menu(options, "Menu", theme_file)

    if chosen == CHANGE_WALLPAPER_OPTION:
        change_wallpaper(settings)


if __name__ == "__main__":
    main()
