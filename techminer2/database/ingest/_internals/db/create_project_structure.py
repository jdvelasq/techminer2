"""Creates the project subdirectories and files."""

import os
import sys

from ....._internals.log_message import internal__log_message

PROJECT_DIRECTORIES = [
    "databases",
    "my_keywords",
    "reports",
    "rules",
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
        +-- rules/
        +-- thesaurus/

    """

    # Create working directories
    sys.stderr.write("INFO  Creating working directories\n")
    sys.stderr.flush()
    for directory in PROJECT_DIRECTORIES:
        create_directory(os.path.join(root_dir, directory))

    # Create cleaining thesaurus files
    create_file(os.path.join(root_dir, "rules/countries.the.txt"))
    create_file(os.path.join(root_dir, "rules/descriptors.the.txt"))
    create_file(os.path.join(root_dir, "rules/organizations.the.txt"))
    create_file(os.path.join(root_dir, "rules/references.the.txt"))

    # Create stopwords.txt file
    sys.stderr.write("INFO  Creating stopwords.txt file\n")
    sys.stderr.flush()
    create_file(os.path.join(root_dir, "my_keywords/stopwords.txt"))

    # Create _DO_NOT_TOUCH_.txt file
    create_file(os.path.join(root_dir, "databases/_DO_NOT_TOUCH_.txt"))
