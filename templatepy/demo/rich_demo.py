from rich.console import Console
from rich.panel import Panel
from rich.text import Text

def rich_demo():
    """Demonstrate some cool Rich features"""
    console = Console()

    # Create styled text
    title = Text("Welcome to Rich Demo!", style="bold magenta")
    
    # Create a fancy panel
    message = Text.assemble(
        ("✨ Rich", "yellow"),
        " makes it easy to add ",
        ("color", "green"),
        " and ",
        ("style", "bold blue"),
        " to your terminal output!"
    )
    
    panel = Panel(
        message,
        title=title,
        border_style="bright_blue",
        padding=(1, 2)
    )
    
    # Display the panel
    console.print(panel)
    
    # Show a progress bar
    with console.status("[bold green]Working on something..."):
        import time
        time.sleep(2)
        console.print("[bold green]Done! ✓") 