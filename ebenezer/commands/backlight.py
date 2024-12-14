import typer

from ebenezer.commands.helpers import run_command

app = typer.Typer()


@app.command("level")
def backlight_level():
    level = _do_backlight_level()
    typer.echo(level)


@app.command("up")
def backlight_up():
    _do_backlight_up()
    typer.echo("Backlight increased by 10%")


@app.command("down")
def backlight_down():
    _do_backlight_down()
    typer.echo("Backlight decreased by 10%")


@app.command("set")
def backlight_set(level: int):
    _do_backlight_set(level)
    typer.echo(f"Backlight changed to {level}%")


def _do_backlight_level() -> str:
    command = "brightnessctl | grep -oP '\\d+%'"
    return run_command(command)


def _do_backlight_up():
    command = "brightnessctl set 10%+"
    run_command(command)


def _do_backlight_down():
    command = "brightnessctl set 10%-"
    run_command(command)


def _do_backlight_set(level: int):
    command = f"brightnessctl set {level}%"
    run_command(command)


if __name__ == "__main__":
    app()
