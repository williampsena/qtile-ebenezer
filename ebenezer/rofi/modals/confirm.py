#!/usr/bin/env python3

import importlib.resources as pkg_resources
import subprocess

YES_LABEL = "󰩐"
NO_LABEL = ""


def confirm_cmd(title, question) -> str:
    theme = pkg_resources.files("ebenezer.rofi.modals").joinpath("confirm.rasi")
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
    choice = confirm_cmd(title, question)

    if choice == YES_LABEL:
        print("yes")
    else:
        print("no")


if __name__ == "__main__":
    main()
