from templatepy.demo import rich_demo
from unittest.mock import patch

def test_rich_demo():
    """Test that rich_demo function runs without errors"""
    with patch('rich.console.Console.print') as mock_print:
        rich_demo()
        # Verify that Console.print was called at least once
        assert mock_print.call_count >= 1 