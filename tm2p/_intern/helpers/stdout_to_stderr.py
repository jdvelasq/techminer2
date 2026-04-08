"""Redirects stdout to stderr"""

import contextlib
import sys


@contextlib.contextmanager
def stdout_to_stderr():
    old_stdout = sys.stdout
    sys.stdout = sys.stderr
    try:
        yield
    finally:
        sys.stdout = old_stdout
