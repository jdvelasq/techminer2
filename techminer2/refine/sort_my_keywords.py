# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Sort My Keywords
===============================================================================


>>> from techminer2.refine import sort_my_keywords
>>> sort_my_keywords(
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
... )
--INFO-- The file example/my_keywords/keywords.txt has been sorted.

"""
import glob
import os


def sort_my_keywords(
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """
    :meta private:
    """

    dir_path = os.path.join(root_dir, "my_keywords")
    if not os.path.isdir(dir_path):
        raise FileNotFoundError(f"The directory '{dir_path}' does not exist.")

    for file in glob.glob(os.path.join(dir_path, "*.txt")):
        #
        with open(file, "r", encoding="utf-8") as in_file:
            keywords = [line.strip() for line in in_file.readlines()]
        keywords = sorted(set(keywords))
        #
        with open(file, "w", encoding="utf-8") as out_file:
            out_file.write("\n".join(keywords))

        print(f"--INFO-- The file {file} has been sorted.")
