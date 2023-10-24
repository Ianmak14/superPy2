from rich.console import Console

# Main console for standard output
console = Console()

# Error console for standard error output with red bold style
err_console = Console(stderr=True, style="red bold")

# The purpose of this module is to provide instances of Console class for standard output and error output.
# These instances can be used throughout the application to print messages in a formatted and visually appealing way.
