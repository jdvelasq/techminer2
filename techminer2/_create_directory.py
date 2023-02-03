"""Create a directory."""
import glob
import os.path


def create_directory(base_directory, target_directory):
    """Createa an empty target directory."""

    path = os.path.join(base_directory, "reports", target_directory)
    if os.path.exists(path):
        _remove_dir(path)
    os.makedirs(path)


def _remove_dir(directory):
    files = glob.glob(directory + "/*")
    for file in files:
        if os.path.isdir(file):
            _remove_dir(file)
        else:
            os.remove(file)
    os.rmdir(directory)
