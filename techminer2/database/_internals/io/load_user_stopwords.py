"""Loads user stopwords."""

import os

from .get_database_file_path import internal__get_database_file_path


def internal__load_user_stopwords(params):
    """:meta private:"""

    file_path = internal__get_database_file_path(params)

    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")

    with open(file_path, "r", encoding="utf-8") as file:
        stopwords = [line.strip() for line in file.readlines()]

    return stopwords
