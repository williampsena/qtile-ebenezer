#!/usr/bin/env python3

import subprocess
import importlib.resources as pkg_resources

from ebenezer.config.settings import load_settings_by_files
from ebenezer.core.theme import preload_colors

YES_LABEL = "󰩐"
NO_LABEL = ""


def confirm_cmd(title, question, theme):
    command = ["rofi", "-dmenu", "-p", title, "-mesg", question, "-theme", theme]
    return (
        subprocess.run(
            command, input=f"{YES_LABEL}\n{NO_LABEL}".encode(), stdout=subprocess.PIPE
        )
        .stdout.decode("utf-8")
        .strip()
    )


def main():
    settings = load_settings_by_files()
    maybe_preload_colors(settings)

    with pkg_resources.files("ebenezer.rofi.powermenu").joinpath(
        "powermenu.rasi"
    ) as theme_file:
        title = "Confirmation"
        question = "Are you sure?"
        yes = "yes"

        choice = confirm_cmd(title, question, theme_file)

        if choice == yes:
            print("yes")
        else:
            print("no")


if __name__ == "__main__":
    main()
