"""Creates the project subdirectories and files."""

import os
import sys

from ....._internals.log_message import internal__log_message

PROJECT_DIRECTORIES = [
    "databases",
    "my_keywords",
    "reports",
    "thesaurus",
]


def create_directory(path):
    """Create a directory if it does not exist."""
    if not os.path.exists(path):
        os.makedirs(path)


def create_file(path):
    """Create a file if it does not exist."""
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8"):
            pass


def internal__create_project_structure(root_dir):
    """Create project working subdirectories.

    +-- root_dir/
        +-- raw-data/
        |   +-- cited_by/
        |   +-- main/
        |   +-- references/
        +-- databases/
        +-- my_keywords/
        +-- my_keywords/stopwords.txt
        +-- reports/
        +-- thesaurus/

    """

    # Create working directories
    sys.stderr.write("\nINFO  Creating working directories.")
    sys.stderr.flush()
    for directory in PROJECT_DIRECTORIES:
        create_directory(os.path.join(root_dir, directory))

    # Create stopwords.txt file
    sys.stderr.write("\nINFO  Creating stopwords.txt file")
    sys.stderr.flush()
    create_file(os.path.join(root_dir, "my_keywords/stopwords.txt"))

    # Create _DO_NOT_TOUCH_.txt file
    create_file(os.path.join(root_dir, "databases/_DO_NOT_TOUCH_.txt"))
