import click

from ebenezer.commands.backlight import cli as backlight_cli
from ebenezer.commands.ui import cli as ui_cli
from ebenezer.commands.volume import cli as volume_cli
from ebenezer.commands.wallpaper import cli as wallpaper_cli


@click.group()
def cli():
    pass


cli.add_command(backlight_cli, name="backlight")
cli.add_command(wallpaper_cli, name="wallpaper")
cli.add_command(volume_cli, name="volume")
cli.add_command(ui_cli, name="ui")

if __name__ == "__main__":
    cli()
