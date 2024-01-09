"""
Easy Logging

- if in notebook, use a simple colored logger
- if in terminal, use a more complex colored logger
"""

__version__ = "0.0.1"


import logging
import sys

import coloredlogs

from .format import get_log_fmt
from .patch import monkeypatched, patch_tqdm
from .logfile import setup_logfile_handlers
from .notebook import isnotebook, ColoredFormatter
from .wrapper import log_stdout
from .config import load_cfg


def setup_logging(logger=logging.root, cfg_file=None):
    """
    Setup logging for the given logger.

    :param logger: the logger to setup
    :param cfg_file: the path to the config file containing default overrides
    """
    user, fmts, style = load_cfg(cfg_file)
    log_fmt = user.get("log_fmt", "standard")

    if isnotebook() or log_fmt == "notebook":
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(ColoredFormatter())
        logger.handlers[:] = []
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        logger.info("Notebook logger initialized.")
    else:
        # display pretty colored logs to console at the info level
        clfmt = get_log_fmt(log_fmt, fmts=fmts)

        coloredlogs.install(
            logger=logger, level=logging.INFO, fmt=clfmt, field_styles=style
        )
        logger.setLevel(logging.DEBUG)
        logger.info(f"'{log_fmt}' logger initialized.")


# logging is setup for the root logger by default
root_logger = logging.root
setup_logging(root_logger)


__all__ = (
    "logger",
    "patch_tqdm",
    "monkeypatched",
    "setup_logfile_handlers",
    "log_stdout",
)
