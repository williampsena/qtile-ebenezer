import click

from ebenezer.rofi.modals.confirm import main as run_confirm
from ebenezer.rofi.powermenu.main import main as run_powermenu
from ebenezer.rofi.wallpaper_menu.main import main as run_wallpaper_menu
from ebenezer.ui.settings.main import main as run_settings


@click.group()
def cli():
    pass


@cli.command()
def powermenu():
    run_powermenu()


@cli.command()
def confirm():
    run_confirm()


@cli.command()
def wallpaper_menu():
    run_wallpaper_menu()


@cli.command()
def settings():
    run_settings()


if __name__ == "__main__":
    cli()
