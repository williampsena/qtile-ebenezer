import click

from ebenezer.commands.helpers import run_command


def get_volume_level() -> str:
    command = "pactl list sinks | grep 'Volume:' | head -n 1 | awk '{print $5}' | tail -n 1 | grep -o '[0-9]\\+'"
    return run_command(command)


@click.group()
def cli():
    pass


@cli.command()
def level():
    level = get_volume_level()
    click.echo(level)


@cli.command()
def up():
    volume_up()
    click.echo("Volume increased by 5%")


@cli.command()
def down():
    volume_down()
    click.echo("Volume decreased by 5%")


@cli.command()
def mute_toggle():
    volume_mute_toggle()
    click.echo("Mute toggled")


@cli.command()
def mute_on():
    volume_mute_on()
    click.echo("Mute on")


@cli.command()
def mute_off():
    volume_mute_off()
    click.echo("Mute off")


@cli.command()
def mute_status():
    status = volume_mute_status()
    click.echo(status)


@cli.command()
def mute_mic():
    microphone_mute_toggle()
    click.echo("Microphone mute toggled")


def volume_up():
    command = "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    run_command(command)


def volume_down():
    command = "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    run_command(command)


def volume_mute_toggle():
    command = "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    run_command(command)


def volume_mute_on():
    command = "pactl set-sink-mute @DEFAULT_SINK@ 1"
    run_command(command)


def volume_mute_off():
    command = "pactl set-sink-mute @DEFAULT_SINK@ 0"
    run_command(command)


def volume_mute_status():
    command = "pactl list sinks | grep 'Mute:' | head -n 1 | awk '{print $2}'"
    return run_command(command)


def microphone_mute_toggle():
    command = "pactl set-source-mute @DEFAULT_SOURCE@ toggle"
    run_command(command)


if __name__ == "__main__":
    cli()
