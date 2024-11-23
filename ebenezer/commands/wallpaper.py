import random
import time
from pathlib import Path
from subprocess import run

import typer

app = typer.Typer()


@app.command("set")
def set_wallpaper(wallpaper_dir: str):
    wallpapers = list(Path(wallpaper_dir).glob("*"))
    if wallpapers:
        wallpaper = random.choice(wallpapers)
        run(f"feh --bg-scale {wallpaper}", shell=True)
        typer.echo(f"Wallpaper set to: {wallpaper}")
    else:
        typer.echo("No wallpapers found in the directory")


@app.command("random")
def random_wallpaper(wallpaper_dir: str, timeout: int = 1800):
    while True:
        set_wallpaper(wallpaper_dir)
        time.sleep(timeout)


if __name__ == "__main__":
    app()
