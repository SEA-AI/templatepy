import click


@click.command()
def hello():
    """Say hello to the world"""
    click.echo("Hello, World!")
