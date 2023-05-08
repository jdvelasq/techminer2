"""Create a directory."""
import os


def create_directory(base_dir, target_dir):
    """
    Create an empty target directory.

    Args:
        base_dir (str): The base directory.
        target_dir (str): The target directory to create.
    """
    path = os.path.join(base_dir, "reports", target_dir)
    if os.path.exists(path):
        remove_directory(path)
    os.makedirs(path)


def remove_directory(directory):
    """
    Remove a directory and all its files.

    Args:
        directory (str): The directory to remove.
    """
    try:
        for file in os.scandir(directory):
            if file.is_dir():
                remove_directory(file.path)
            else:
                os.remove(file.path)
        os.rmdir(directory)
    except FileNotFoundError as exc:
        print(f"Directory {directory} not found: {exc}")
    except PermissionError as exc:
        print(f"Permission denied when trying to remove {directory}: {exc}")
    except OSError as exc:
        print(f"Error while removing directory {directory}: {exc}")
