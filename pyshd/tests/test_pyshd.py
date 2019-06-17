from pathlib import Path
from pyshd import pushd
import os


def cwd():
    return Path(os.getcwd())


def test_pushd(tmpdir):
    prev = Path(os.getcwd())
    root = Path(str(tmpdir)) # Pytest provides a pathlib2 instance
    path = root / 'some' / 'dir'
    path.mkdir(parents=True)

    assert cwd() == prev
    with pushd(root):
        assert cwd() == root

        with pushd(path):
            assert cwd() == path

        assert cwd() == root
    assert cwd() == prev
