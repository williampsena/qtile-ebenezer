import importlib

import click

from ebenezer.commands.backlight import cli as backlight_cli
from ebenezer.commands.keyboard import cli as keyboard_cli
from ebenezer.commands.ui import cli as ui_cli
from ebenezer.commands.volume import cli as volume_cli
from ebenezer.commands.wallpaper import cli as wallpaper_cli

try:
    __version__ = importlib.metadata.version("qtile-ebenezer")
except:
    __version__ = "dev"


@click.group(invoke_without_command=True, no_args_is_help=True)
@click.version_option(__version__)
def cli():
    pass


cli.add_command(backlight_cli, name="backlight")
cli.add_command(wallpaper_cli, name="wallpaper")
cli.add_command(volume_cli, name="volume")
cli.add_command(ui_cli, name="ui")
cli.add_command(keyboard_cli, name="keyboard")

if __name__ == "__main__":
    cli()
