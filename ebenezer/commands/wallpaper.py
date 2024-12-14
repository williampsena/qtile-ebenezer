import random
import time
from pathlib import Path
from subprocess import run

import typer

app = typer.Typer()

LOOP = True


@app.command("set")
def set_wallpaper(wallpaper_path: str):
    if Path(wallpaper_path).is_dir():
        wallpapers = list(Path(wallpaper_path).glob("*"))

        if wallpapers:
            wallpaper = random.choice(wallpapers)
            run(f"feh --bg-scale {wallpaper}", shell=True)
            typer.echo(f"Wallpaper set to: {wallpaper}")
        else:
            typer.echo("No wallpapers found in the directory")
    elif Path(wallpaper_path).is_file():
        run(f"feh --bg-scale {wallpaper_path}", shell=True)
        typer.echo(f"Wallpaper set to: {wallpaper_path}")
    else:
        typer.echo("No wallpaper file is found")


@app.command("random")
def random_wallpaper(wallpaper_dir: str, timeout: int = 1800, max_changes: int = 0):
    def _change_wallpaper():
        set_wallpaper(wallpaper_dir)
        time.sleep(timeout)

    if max_changes == 0:
        while True:
            _change_wallpaper()
    else:
        for _ in range(max_changes):
            _change_wallpaper()


if __name__ == "__main__":
    app()
