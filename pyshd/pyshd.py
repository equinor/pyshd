import contextlib
import os


@contextlib.contextmanager
def pushd(path):
    """pushd

    Change directory to the given path. This function is meant to be used with
    contextmanagers as in the example below.

    Parameters
    ----------
    path : str
        Path to the directory to enter

    Examples
    --------
    >>> from pyshd import pushd
    >>> import os
    >>> os.getcwd()
    '/private/user/projects/pyshd'
    >>> with pushd('/tmp'):
    ...     print(os.getcwd())
    '/tmp'
    >>> os.getcwd()
    '/private/user/projects/pyshd'
    """
    prev = os.getcwd()
    try:
        if path is not None:
            os.chdir(str(path))
        yield
    finally:
        os.chdir(prev)
