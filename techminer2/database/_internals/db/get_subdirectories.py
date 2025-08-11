"""Obtain a list of subdirectories in a directory."""
import os


def internal__get_subdirectories(directory):
    """:meta private:"""

    subdirectories = os.listdir(directory)
    subdirectories = [
        f for f in subdirectories if os.path.isdir(os.path.join(directory, f))
    ]
    return subdirectories
