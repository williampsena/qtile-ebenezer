import click

from ebenezer.commands.helpers import run_command


@click.group()
def cli():
    pass


@cli.command()
def level():
    command = "pactl list sinks | grep 'Volume:' | head -n 1 | awk '{print $5}' | tail -n 1 | grep -o '[0-9]\\+'"
    level = run_command(command)
    click.echo(level)


@cli.command()
def up():
    command = "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    run_command(command)
    click.echo("Volume increased by 5%")


@cli.command()
def down():
    command = "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    run_command(command)
    click.echo("Volume decreased by 5%")


@cli.command()
def mute_toggle():
    command = "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    run_command(command)
    click.echo("Mute toggled")


@cli.command()
def mute_on():
    command = "pactl set-sink-mute @DEFAULT_SINK@ 1"
    run_command(command)
    click.echo("Mute on")


@cli.command()
def mute_off():
    command = "pactl set-sink-mute @DEFAULT_SINK@ 0"
    run_command(command)
    click.echo("Mute off")


@cli.command()
def mute_status():
    command = "pactl list sinks | grep 'Mute:' | head -n 1 | awk '{print $2}'"
    status = run_command(command)
    click.echo(status)


if __name__ == "__main__":
    cli()
