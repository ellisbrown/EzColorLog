"""
Logfile Handling

TODO: could compress logfiles after rollover
- https://stackoverflow.com/a/53288524/5487412
TODO: logfile rotation is not working correctly, rotating WAY too often...
- debug logs are <100KB ... X 100?
"""

import logging
import os
import os.path as osp
from typing import List, Union

from .format import get_log_fmt

root_logger = logging.root


def _add_logfile_handler(
    logdir: str,
    logger: logging.Logger = root_logger,
    level: Union[int, str] = logging.INFO,
):
    """Add a file handler to the logger.

    :param logger: the logging.Logger to add the handler to
    :param logdir: the directory in which to save the log file
    :param level: the logging level
    """

    level_int: int = logging._checkLevel(level)
    level_name: str = logging.getLevelName(level_int)

    # create log folder if it doesn't exist
    os.makedirs(logdir, exist_ok=True)
    logfile = osp.join(logdir, f"{level_name}.log")
    # use rotating file handler to save logs => max 10MB per file
    # fh = RotatingFileHandler(logfile, maxBytes=1e7, backupCount=1000)
    # check if file exists, if so, mark as version 2
    for i in range(1, 1000):  # HACK: come up with a better solution
        if not osp.exists(logfile):
            break
        logfile = osp.join(logdir, f"{level_name}_{i}.log")
    fh = logging.FileHandler(logfile)
    fh.setLevel(level_int)
    fmt = get_log_fmt("logfile")
    formatter = logging.Formatter(fmt, "%Y-%m-%d %H:%M:%S")
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    root_logger.info(
        f"Logfile handler (level {level_name}) added to "
        f"{logger.name} logger at '{logfile}'."
    )


def setup_logfile_handlers(
    logdir: str,
    logger: logging.Logger = root_logger,
    levels: List[Union[int, str]] = ["INFO", "DEBUG"],
):
    for level in levels:
        _add_logfile_handler(logdir, logger, level)


__all__ = ("setup_logfile_handlers",)
