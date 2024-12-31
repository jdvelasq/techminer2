"""Obtain a list of subdirectories in a directory."""


import os


def get_subdirectories(directory):
    """
    Get a list of subdirectories in a directory.

    Args:
        directory (str): The directory to get the subdirectories from.

    Returns:
        A list of subdirectories.

    :meta private:
    """
    subdirectories = os.listdir(directory)
    subdirectories = [
        f for f in subdirectories if os.path.isdir(os.path.join(directory, f))
    ]
    return subdirectories
