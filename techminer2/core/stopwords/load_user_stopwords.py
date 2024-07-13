"""
Loads user stopwords.

"""

import os


def load_user_stopwords(root_dir):
    """:meta private:"""

    stopwords_file_path = os.path.join(root_dir, "my_keywords/stopwords.txt")

    if not os.path.isfile(stopwords_file_path):
        raise FileNotFoundError(f"The file '{stopwords_file_path}' does not exist.")

    with open(stopwords_file_path, "r", encoding="utf-8") as file:
        stopwords = [line.strip() for line in file.readlines()]

    return stopwords
