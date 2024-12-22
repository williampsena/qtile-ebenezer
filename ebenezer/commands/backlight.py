import click

from ebenezer.commands.helpers import run_command


@click.group()
def cli():
    pass


@cli.command()
def level():
    level = backlight_level()
    click.echo(level)


@cli.command()
def up():
    backlight_up()
    click.echo("Backlight increased by 10%")


@cli.command()
def down():
    backlight_down()
    click.echo("Backlight decreased by 10%")


@cli.command()
@click.argument("level", type=int)
def set(level: int):
    backlight_set(level)
    click.echo(f"Backlight changed to {level}%")


def backlight_level() -> str:
    command = "brightnessctl | grep -oP '\\d+%'"
    return run_command(command)


def backlight_up():
    command = "brightnessctl set 10%+"
    run_command(command)


def backlight_down():
    command = "brightnessctl set 10%-"
    run_command(command)


def backlight_set(level: int):
    command = f"brightnessctl set {level}%"
    run_command(command)


if __name__ == "__main__":
    cli()
