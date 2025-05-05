from click.testing import CliRunner
from templatepy.cli import cli


def test_hello_command():
    """Test the hello command"""
    runner = CliRunner()
    result = runner.invoke(cli, ["hello"])
    assert result.exit_code == 0
    assert "Hello, World!" in result.output
