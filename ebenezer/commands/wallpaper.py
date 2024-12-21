import random
import time
from pathlib import Path
from subprocess import run

import click


def _set_wallpaper(wallpaper_path: str) -> str:
    if Path(wallpaper_path).is_dir():
        wallpapers = list(Path(wallpaper_path).glob("*"))

        if wallpapers:
            wallpaper = random.choice(wallpapers)
            run(f'feh --bg-scale "{wallpaper}"', shell=True)
            return f'Wallpaper set to: "{wallpaper}"'
        else:
            click.echo("No wallpapers found in the directory")
    elif Path(wallpaper_path).is_file():
        run(f'feh --bg-scale "{wallpaper_path}"', shell=True)
        return f'Wallpaper set to: "{wallpaper_path}"'
    else:
        return "No wallpaper file is found"


@click.group()
def cli():
    pass


@cli.command()
@click.argument("wallpaper_path", type=click.Path(exists=True))
def set(wallpaper_path: str):
    output = _set_wallpaper(wallpaper_path)
    click.echo(output)


@cli.command(name="random")
@click.argument("wallpaper_dir", type=click.Path(exists=True))
@click.option(
    "--timeout", default=1800, help="Timeout between wallpaper changes in seconds"
)
@click.option(
    "--max-changes",
    default=0,
    help="Maximum number of wallpaper changes (0 for infinite)",
)
def random_wallpaper(wallpaper_dir: str, timeout: int, max_changes: int):
    def _change_wallpaper():
        _set_wallpaper(wallpaper_dir)
        time.sleep(timeout)

    if max_changes == 0:
        while True:
            _change_wallpaper()
    else:
        for _ in range(max_changes):
            _change_wallpaper()


if __name__ == "__main__":
    cli()
