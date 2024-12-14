import typer

from ebenezer.rofi.modals.confirm import main as run_confirm
from ebenezer.rofi.powermenu.main import main as run_powermenu
from ebenezer.rofi.wallpaper_menu.main import main as run_wallpaper_menu
from ebenezer.ui.settings.main import main as run_settings

app = typer.Typer()


@app.command("powermenu")
def powermenu():
    run_powermenu()


@app.command("confirm")
def confirm():
    run_confirm()


@app.command("wallpaper_menu")
def confirm():
    run_wallpaper_menu()


@app.command("settings")
def confirm():
    run_settings()


if __name__ == "__main__":
    app()
