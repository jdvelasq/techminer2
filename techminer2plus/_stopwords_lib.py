"""
Stopwords
"""
import os


def load_stopwords(root_dir):
    """Load user stopwords from the specified directory.

    Args:
        root_dir (str): the root directory of the database.

    Returns:
        list: list of user-defined stopwords.

    """

    stopwords_file_path = os.path.join(root_dir, "stopwords.txt")

    if not os.path.isfile(stopwords_file_path):
        raise FileNotFoundError(
            f"The file '{stopwords_file_path}' does not exist."
        )

    with open(stopwords_file_path, "r", encoding="utf-8") as file:
        stopwords = [line.strip() for line in file.readlines()]

    return stopwords
