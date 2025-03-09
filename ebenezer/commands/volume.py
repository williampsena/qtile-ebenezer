import click

from ebenezer.commands.helpers import run_command

HEADSET_SINK = "@DEFAULT_SINK@"


def _phone_plugged(sink_name: str):
    return "bluez_output" in sink_name or "headset" in sink_name


def _speaker_plugged(sink_name: str):
    return "alsa_output" in sink_name or "analog" in sink_name


def _get_headset_sinks() -> str:
    return run_command("pactl list short sinks")


def _get_headset_sinks_and_volume() -> dict[str, str]:
    result = _get_headset_sinks()
    levels: dict[str, str] = {}

    for line in result.splitlines():
        parts = line.split("\t")

        if len(parts) < 2:
            continue

        sink_name = parts[1].lower()

        if _phone_plugged(sink_name):
            levels["phone"] = _do_get_volume_level(sink_name)
        elif _speaker_plugged(sink_name):
            levels["speaker"] = _do_get_volume_level(sink_name)

    return levels


def get_volume_level() -> str:
    levels = _get_headset_sinks_and_volume()

    phone_level = levels.get("phone")
    speaker_level = levels.get("speaker")

    if phone_level:
        return phone_level
    if speaker_level:
        return speaker_level

    return ""


def get_volume_levels() -> str:
    levels = _get_headset_sinks_and_volume()
    return "\n".join(f"{sink}: {level}" for sink, level in levels.items())


def _do_get_volume_level(sink: str = None) -> str:
    if sink is None:
        command = "pactl list sinks | grep 'Volume:' | head -n 1 | awk '{print $5}' | tail -n 1 | grep -o '[0-9]\\+'"
    else:
        command = f"pactl list sinks | grep -A 15 'Name: {sink}' | grep 'Volume:' | head -n 1 | awk '{{print $5}}' | grep -o '[0-9]\\+'"

    return run_command(command)


@click.group()
def cli():
    pass


@cli.command()
def level():
    level = get_volume_level()
    click.echo(level)


@cli.command()
def levels():
    levels = get_volume_levels()
    click.echo(levels)


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


@cli.command()
def phone_plugged():
    sinks = _get_headset_sinks()
    headset_plugged = any("headset" in s.lower() for s in sinks.splitlines())
    click.echo(headset_plugged)


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
