"""Stopwords."""

import os

import pkg_resources

from ._parameters import RootDirMixin


class StopwordsMixin(RootDirMixin):
    """Mixin class for stopwords management."""

    def __init__(
        self,
        #
        # DATABASE PARAMS
        root_dir: str = "./",
    ):
        super().__init__(root_dir=root_dir)

    def load_stopwords(self):
        """Load user stopwords from the project directory."""

        stopwords_file_path = os.path.join(self.root_dir, "my_keywords/stopwords.txt")

        if not os.path.isfile(stopwords_file_path):
            raise FileNotFoundError(f"The file '{stopwords_file_path}' does not exist.")

        with open(stopwords_file_path, "r", encoding="utf-8") as file:
            stopwords = [line.strip() for line in file.readlines()]

        return stopwords

    def load_package_stopwords(self):
        """:meta private:"""

        file_path = pkg_resources.resource_filename("techminer2", "word_lists/stopwords.txt")
        with open(file_path, "r", encoding="utf-8") as file:
            stopwords = file.read().split("\n")
        stopwords = [w.strip() for w in stopwords]
        stopwords = [w for w in stopwords if w != ""]
        return stopwords


def load_package_stopwords():
    """Loads system stopwords.

    :meta private:
    """
    file_path = pkg_resources.resource_filename("techminer2", "word_lists/stopwords.txt")

    ###  module_path = dirname(__file__)
    ### file_path = os.path.join(module_path, "word_lists/stopwords.txt")
    with open(file_path, "r", encoding="utf-8") as file:
        stopwords = file.read().split("\n")
    stopwords = [w.strip() for w in stopwords]
    stopwords = [w for w in stopwords if w != ""]
    return stopwords
