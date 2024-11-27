import typer

from ebenezer.commands.backlight import app as backlight_app
from ebenezer.commands.volume import app as volume_app
from ebenezer.commands.wallpaper import app as wallpaper_app

app = typer.Typer()

app.add_typer(backlight_app, name="backlight")
app.add_typer(wallpaper_app, name="wallpaper")
app.add_typer(volume_app, name="volume")

if __name__ == "__main__":
    app()
