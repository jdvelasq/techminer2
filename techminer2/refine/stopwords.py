# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Stopwords
===============================================================================


>>> from techminer2.refine import Stopwords
>>> Stopwords(
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
... ).sort_stopwords()
--INFO-- The file example/my_keywords/stopwords.txt has been sorted.

"""
import os

from .._stopwords import StopwordsMixin


class Stopwords(StopwordsMixin):
    """:meta private:"""

    def __init__(
        self,
        #
        # DATABASE PARAMS:
        root_dir="./",
    ):
        # initialize mixins
        StopwordsMixin.__init__(
            self,
            #
            # DATABASE PARAMS:
            root_dir=root_dir,
        )

    def sort_stopwords(self):
        """:meta private:"""

        stopwords_file_path = os.path.join(self.root_dir, "my_keywords/stopwords.txt")

        if not os.path.isfile(stopwords_file_path):
            raise FileNotFoundError(f"The file '{stopwords_file_path}' does not exist.")

        with open(stopwords_file_path, "r", encoding="utf-8") as file:
            stopwords = [line.strip() for line in file.readlines()]

        stopwords = sorted(set(stopwords))
        with open(stopwords_file_path, "w", encoding="utf-8") as file:
            for word in stopwords:
                file.write(word + "\n")

        print(f"--INFO-- The file {stopwords_file_path} has been sorted.")
