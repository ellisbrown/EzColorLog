from warnings import warn

from .config import load_cfg

# load the default config file
_, defaults, _ = load_cfg()


def get_log_fmt(log_fmt: str, fmts: dict = dict()) -> str:
    """
    Return a string to be used as a format string for logging.

    :param log_fmt: the name of the format to use
    :param fmts: a dictionary of format string overrides
    :return: a string to be used as a format string for logging
    """

    # override the defaults with the passed in formats
    defaults.update(fmts)
    fmts = defaults

    assert "standard" in fmts, "No 'standard' format found in config file."

    if log_fmt.lower() in fmts:
        return fmts[log_fmt]
    else:
        warn(
            f"Invalid log style: {log_fmt}. Check your config.\n"
            f"Valid styles: {list(fmts.keys())}\nDefaulting to 'standard'."
        )
        return get_log_fmt("standard")
