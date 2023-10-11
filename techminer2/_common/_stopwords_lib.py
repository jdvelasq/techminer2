"""
Stopwords
"""
import os
from os.path import dirname

import pkg_resources


def load_stopwords(root_dir):
    """Load user stopwords from the specified directory.

    Args:
        root_dir (str): the root directory of the database.

    Returns:
        list: list of user-defined stopwords.

    """

    stopwords_file_path = os.path.join(root_dir, "my_keywords/stopwords.txt")

    if not os.path.isfile(stopwords_file_path):
        raise FileNotFoundError(f"The file '{stopwords_file_path}' does not exist.")

    with open(stopwords_file_path, "r", encoding="utf-8") as file:
        stopwords = [line.strip() for line in file.readlines()]

    return stopwords


def load_generic_stopwords():
    """Loads system stopwords.

    :meta private:
    """
    file_path = pkg_resources.resource_filename(
        "techminer2", "word_lists/stopwords.txt"
    )

    ###  module_path = dirname(__file__)
    ### file_path = os.path.join(module_path, "word_lists/stopwords.txt")
    with open(file_path, "r", encoding="utf-8") as file:
        stopwords = file.read().split("\n")
    stopwords = [w.strip() for w in stopwords]
    stopwords = [w for w in stopwords if w != ""]
    return stopwords
