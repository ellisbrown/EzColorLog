"""
Wrapper to redirect stdout to logger

This allows us to simply add the `@log_stdout` decorator to any function and
have all of its print statements redirected to the logger.
"""


import contextlib
import io
import logging
import os
import platform
import traceback
from functools import partial, wraps
from inspect import currentframe
from typing import Union

root_logger = logging.root


def log_stdout(
    func=None,
    *,
    stacklevel: int = 4,
    level: Union[str, int] = "INFO",
    logger: logging.Logger = root_logger,
):
    """Function decorator to redirect print statements to logger."""
    # https://pybit.es/articles/decorator-optional-argument/
    if func is None:
        return partial(log_stdout, stacklevel=stacklevel, level=level, logger=logger)

    @wraps(func)
    def wrapper(*args, **kwargs):
        # # also redirect console logging to tqdm.write -> prints logs above bars
        # with logging_redirect_tqdm(loggers=[logger]):
        with contextlib.redirect_stdout(
            StdOutLogger(logger=logger, stacklevel=stacklevel, level=level)
        ):
            return func(*args, **kwargs)

    return wrapper


class StdOutLogger:
    def __init__(
        self,
        logger: logging.Logger = root_logger,
        stacklevel: int = 4,
        level: Union[int, str] = logging.INFO,
    ):
        self.logger = logger
        self.stacklevel = stacklevel
        self.level = logging._checkLevel(level)

    def write(self, msg):
        if platform.sys.version_info.minor >= 8:
            return self._write_38(msg)
        return self._write_37(msg)

    def _log(self, msg, **kwargs):
        if msg and not msg.isspace():
            self.logger.log(self.level, msg, **kwargs)

    def _write_37(self, msg):
        caller = self.logger.findCaller
        self.logger.findCaller = partial(
            self.findCallerStackLevel, stacklevel=self.stacklevel
        )
        self._log(msg)
        self.logger.findCaller = caller

    def _write_38(self, msg):
        self._log(msg, stacklevel=self.stacklevel)

    def flush(self):
        pass

    def isatty(self):
        pass

    @staticmethod
    def findCallerStackLevel(stack_info=False, stacklevel: int = 4):
        """[Hack for Python < 3.8]
        Find the stack frame of the caller so that we can note the source
        file name, line number and function name.

        https://stackoverflow.com/a/13591151/5487412
        """
        f = currentframe()
        # On some versions of IronPython, currentframe() returns None if
        # IronPython isn't run with -X:Frames.
        if f is not None:
            f = f.f_back
        rv = "(unknown file)", 0, "(unknown function)", None
        while hasattr(f, "f_code") and (stacklevel > 0):
            co = f.f_code
            filename = os.path.normcase(co.co_filename)
            if filename == logging._srcfile or stacklevel > 1:
                f = f.f_back
                stacklevel -= 1
                continue
            sinfo = None
            if stack_info:
                sio = io.StringIO()
                sio.write("Stack (most recent call last):\n")
                traceback.print_stack(f, file=sio)
                sinfo = sio.getvalue()
                if sinfo[-1] == "\n":
                    sinfo = sinfo[:-1]
                sio.close()
            rv = (co.co_filename, f.f_lineno, co.co_name, sinfo)
            break
        return rv
