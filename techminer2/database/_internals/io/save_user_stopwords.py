"""Loads user stopwords."""

import os
import pathlib

from techminer2.database._internals.io.get_database_file_path import (
    internal__get_database_file_path,
)


def internal__save_user_stopwords(params, stopwords):
    """:meta private:"""

    file_path = pathlib.Path(params.root_directory) / "data/my_keywords/stopwords.txt"

    with open(file_path, "w", encoding="utf-8") as file:
        for stopword in stopwords:
            file.write(f"{stopword}\n")

    return stopwords
