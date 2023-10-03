# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Sort Stopwords
===============================================================================


>>> from techminer2.refine import sort_stopwords
>>> sort_stopwords(
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
... )
--INFO-- The file data/regtech/stopwords.txt has been sorted.

"""
import os


def sort_stopwords(
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """
    :meta private:
    """

    stopwords_file_path = os.path.join(root_dir, "stopwords.txt")

    if not os.path.isfile(stopwords_file_path):
        raise FileNotFoundError(f"The file '{stopwords_file_path}' does not exist.")

    with open(stopwords_file_path, "r", encoding="utf-8") as file:
        stopwords = [line.strip() for line in file.readlines()]

    stopwords = sorted(set(stopwords))
    with open(stopwords_file_path, "w", encoding="utf-8") as file:
        for word in stopwords:
            file.write(word + "\n")

    print(f"--INFO-- The file {stopwords_file_path} has been sorted.")
