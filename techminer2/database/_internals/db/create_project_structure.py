"""Creates the project subdirectories and files."""

import os
import sys

PROJECT_DIRECTORIES = [
    "data",
    "outputs",
    "src",
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
        +-- data/
        |   +-- scopus/
        |   +-- raw/
        |   |   +-- cited_by/
        |   |   +-- main/
        |   |   +-- references/
        |   +-- processed/
        |   +-- my_keywords/
        |   +-- my_keywords/stopwords.txt
        |   +-- thesaurus/
        +-- outputs/
        |   +-- tables/
        |   +-- figures/
        |   +-- texts/
        +-- src/

    """

    # Create working directories
    sys.stderr.write("INFO: Creating working directories\n")
    sys.stderr.flush()

    create_directory(os.path.join(root_dir, "data"))

    create_directory(os.path.join(root_dir, "data/scopus"))
    create_directory(os.path.join(root_dir, "data/raw"))
    create_directory(os.path.join(root_dir, "data/raw/cited_by"))
    create_directory(os.path.join(root_dir, "data/raw/main"))
    create_directory(os.path.join(root_dir, "data/raw/references"))

    create_directory(os.path.join(root_dir, "data/processed"))
    create_file(os.path.join(root_dir, "data/processed/_do_not_touch_.txt"))
    create_directory(os.path.join(root_dir, "data/my_keywords"))
    create_file(os.path.join(root_dir, "data/my_keywords/stopwords.txt"))
    create_directory(os.path.join(root_dir, "data/thesaurus"))

    create_directory(os.path.join(root_dir, "outputs"))
    create_directory(os.path.join(root_dir, "outputs/tables"))
    create_directory(os.path.join(root_dir, "outputs/figures"))
    create_directory(os.path.join(root_dir, "outputs/texts"))

    create_directory(os.path.join(root_dir, "src"))

    sys.stderr.flush()

    # Create _DO_NOT_TOUCH_.txt file
