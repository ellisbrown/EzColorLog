import logging

from colorama import Back, Fore, Style

from .format import get_log_fmt


def isnotebook() -> bool:
    # https://stackoverflow.com/a/39662359/5487412
    try:
        from IPython import get_ipython

        shell = get_ipython().__class__.__name__
        if shell == "ZMQInteractiveShell":
            return True  # Jupyter notebook or qtconsole
        elif shell == "TerminalInteractiveShell":
            return False  # Terminal running IPython
        else:
            return False  # Other type (?)
    except NameError:
        return False  # Probably standard Python interpreter


class ColoredFormatter(logging.Formatter):
    """Colored log formatter.

    https://gist.github.com/joshbode/58fac7ababc700f51e2a9ecdebe563ad
    """

    DEFAULT_COLORS = {
        "DEBUG": Fore.CYAN,
        "INFO": Fore.GREEN,
        "WARNING": Fore.YELLOW,
        "ERROR": Fore.RED,
        "CRITICAL": Fore.RED + Back.WHITE + Style.BRIGHT,
    }
    DEFAULT_FMT = get_log_fmt("notebook")
    DEFAULT_DATEFMT = "%H:%M:%S"

    def __init__(
        self,
        fmt=DEFAULT_FMT,
        datefmt=DEFAULT_DATEFMT,
        style="{",
        validate=True,
        colors=DEFAULT_COLORS,
    ):
        """Initialize the formatter with specified format strings."""
        super().__init__(fmt, datefmt, style, validate)
        self.colors = colors if colors else {}

    def format(self, record) -> str:
        """Format the specified record as text."""

        record.color = self.colors.get(record.levelname, "")
        record.reset = Style.RESET_ALL

        return super().format(record)


__all__ = (
    "ColoredFormatter",
    "isnotebook",
)
