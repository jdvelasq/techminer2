"""Check if file exists"""
import os
import sys


def check_references_csv(directory):
    """Check if file exists"""

    file_path = os.path.join(directory, "processed", "_references.csv")
    if not os.path.exists(file_path):
        sys.stderr.write(
            f"--ERROR-- File '{file_path}' not found. Unable to run the command.\n"
        )
        return False
    return True
