"""Creates the project subdirectories and files."""

import os

from ..message import message

PROJECT_DIRECTORIES = [
    "databases",
    "my_keywords",
    "reports",
    "thesauri",
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
        +-- thesauri/

    """

    # Create working directories
    message("Creating working directories")
    for directory in PROJECT_DIRECTORIES:
        create_directory(os.path.join(root_dir, directory))

    # Create stopwords.txt file
    message("Creating stopwords.txt file")
    create_file(os.path.join(root_dir, "my_keywords/stopwords.txt"))

    # Create _DO_NOT_TOUCH_.txt file
    create_file(os.path.join(root_dir, "databases/_DO_NOT_TOUCH_.txt"))
