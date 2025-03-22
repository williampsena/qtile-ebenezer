import click

from ebenezer.core.keys import fetch_keybindings_text


@click.group()
def cli():
    pass


@cli.command()
def keybindings():
    click.echo(fetch_keybindings_text())


if __name__ == "__main__":
    cli()
