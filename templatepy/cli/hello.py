import click  # noqa: D100


@click.command()
def hello() -> None:
    """Say hello to the world."""
    click.echo("Hello, World!")
