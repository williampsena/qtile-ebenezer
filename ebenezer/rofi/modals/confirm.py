#!/usr/bin/env python3

import importlib.resources as pkg_resources
import subprocess

YES_LABEL = "󰩐"
NO_LABEL = ""


def confirm_cmd(title, question, theme):
    command = [
        "rofi",
        "-dmenu",
        "-p",
        title,
        "-mesg",
        question,
        "-theme",
        theme,
    ]
    return (
        subprocess.run(
            command, input=f"{YES_LABEL}\n{NO_LABEL}".encode(), stdout=subprocess.PIPE
        )
        .stdout.decode("utf-8")
        .strip()
    )


def main(title: str = "Confirmations", question: str = "Are you sure?"):
    theme_file = pkg_resources.files("ebenezer.rofi.modals").joinpath("confirm.rasi")
    choice = confirm_cmd(title, question, theme_file)

    if choice == YES_LABEL:
        print("yes")
    else:
        print("no")


if __name__ == "__main__":
    main()
