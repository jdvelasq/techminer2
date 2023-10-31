"""Creates the project subdirectories and files."""

import os
import shutil

import pkg_resources

from ._message import message

PROJECT_WORKING_DIRECTORIES = [
    "databases",
    "reports",
    "my_keywords",
    "thesauri",
]


def create_working_subdirectories_and_files(root_dir):
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

    #
    # Create working directories
    message("Creating working directories")
    for directory in PROJECT_WORKING_DIRECTORIES:
        directory_path = os.path.join(root_dir, directory)
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

    #
    # Create stopwords.txt file
    message("Creating stopwords.txt file")
    file_path = os.path.join(root_dir, "my_keywords/stopwords.txt")
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8"):
            pass

    #
    # Copy thesauri files
    src_dir = pkg_resources.resource_filename("techminer2", "thesauri_data/")
    dst_dir = os.path.join(root_dir, "thesauri/")
    for filename in os.listdir(src_dir):
        src_file_path = os.path.join(src_dir, filename)
        dst_file_path = os.path.join(dst_dir, filename)
        if not os.path.exists(dst_file_path):
            shutil.copy2(src_file_path, dst_file_path)

    #
    # Create replacements.the.txt file
    message("Creating abbreviations.the.txt file")
    file_path = os.path.join(root_dir, "thesauri/abbreviations.the.txt")
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8"):
            pass

    #
    # Create replacements.the.txt file
    message("Creating replacements.the.txt file")
    file_path = os.path.join(root_dir, "thesauri/replacements.the.txt")
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8"):
            pass
