"""Loads user stopwords."""

import os
import pathlib


def internal__load_user_stopwords(params):
    """:meta private:"""

    file_path = pathlib.Path(params.root_directory) / "data/my_keywords/stopwords.txt"

    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")

    with open(file_path, "r", encoding="utf-8") as file:
        stopwords = [line.strip() for line in file.readlines()]

    return stopwords
