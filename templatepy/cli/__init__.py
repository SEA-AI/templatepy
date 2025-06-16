import click  # noqa: D104

from .hello import hello


@click.group()
def cli() -> None:
    """Placeholder for the CLI group."""
    pass


cli.add_command(hello)
