"""
TQDM Monkey Patch

this allows us to pass in arguments to tqdm for subpackages that use tqdm
e.g., torchvision.datasets


inspiration: https://github.com/tqdm/tqdm/issues/614#issuecomment-939321390
"""

import contextlib
from functools import partialmethod


@contextlib.contextmanager
def monkeypatched(obj, name, patch):
    """Temporarily monkeypatch."""
    old_attr = getattr(obj, name)
    setattr(obj, name, patch(old_attr))
    try:
        yield
    finally:
        setattr(obj, name, old_attr)


@contextlib.contextmanager
def patch_tqdm(**kwargs):
    """Context manager to disable tqdm."""

    def _patch(old_init):
        return partialmethod(old_init, **kwargs)

    import tqdm

    with monkeypatched(tqdm.std.tqdm, "__init__", _patch):
        yield


__all__ = (
    "monkeypatched",
    "patch_tqdm",
)
