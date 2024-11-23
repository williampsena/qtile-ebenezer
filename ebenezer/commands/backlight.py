import subprocess

import typer

app = typer.Typer()


def run_command(command: str) -> str:
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout.strip()


@app.command("level")
def backlight_level():
    level = do_backlight_level()
    typer.echo(level)


@app.command("up")
def backlight_up():
    do_backlight_up()
    typer.echo("Backlight increased by 10%")


@app.command("down")
def backlight_down():
    do_backlight_down()
    typer.echo("Backlight decreased by 10%")


def do_backlight_level() -> str:
    command = "brightnessctl | grep -oP '\\d+%'"
    return run_command(command)


def do_backlight_up():
    command = "brightnessctl set 10%+"
    run_command(command)


def do_backlight_down():
    command = "brightnessctl set 10%-"
    run_command(command)


if __name__ == "__main__":
    app()
