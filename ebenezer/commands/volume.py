import subprocess

import typer

app = typer.Typer()


def run_command(command: str) -> str:
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout.strip()


@app.command("level")
def volume_level():
    command = "pactl list sinks | grep 'Volume:' | head -n 1 | awk '{print $5}' | tail -n 1 | grep -o '[0-9]\\+'"
    level = run_command(command)
    typer.echo(level)


@app.command("up")
def volume_up():
    command = "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    run_command(command)
    typer.echo("Volume increased by 5%")


@app.command("down")
def volume_down():
    command = "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    run_command(command)
    typer.echo("Volume decreased by 5%")


@app.command("mute_toggle")
def mute_toggle():
    command = "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    run_command(command)
    typer.echo("Mute toggled")


@app.command("mute_on")
def mute_on():
    command = "pactl set-sink-mute @DEFAULT_SINK@ 1"
    run_command(command)
    typer.echo("Mute on")


@app.command("mute_off")
def mute_off():
    command = "pactl set-sink-mute @DEFAULT_SINK@ 0"
    run_command(command)
    typer.echo("Mute off")


@app.command("mute_status")
def mute_status():
    command = "pactl list sinks | grep 'Mute:' | head -n 1 | awk '{print $2}'"
    run_command(command)
    typer.echo("Mute off")


if __name__ == "__main__":
    app()
