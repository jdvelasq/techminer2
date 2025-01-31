# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort Common Starting Words
===============================================================================


## >>> from techminer2.prepare.thesaurus.default import sort_common_starting_words
## >>> sort_common_starting_words()
--INFO-- The common_starting_words.txt thesaurus has been sorted.

"""
import os.path

import pkg_resources  # type: ignore


def sort_common_starting_words():
    """:meta private:"""

    file_path = pkg_resources.resource_filename(
        "techminer2",
        "thesaurus/_data/common_starting_words.txt",
    )

    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    with open(file_path, "r", encoding="utf-8") as file:
        words = [word.strip() for word in file.readlines() if word.strip() != ""]

    words = [word.replace(",", "") for word in words]
    words = [word.replace(".", "") for word in words]
    words = [word.replace(";", "") for word in words]
    words = [word.replace(")", "") for word in words]
    words = [word.replace("(", "") for word in words]
    words = set(words)
    words = sorted(words)

    #
    # Saves the sorted thesaurus to the file
    with open(file_path, "w", encoding="utf-8") as file:
        for word in words:
            file.write(word + "\n")

    print("--INFO-- The common_starting_words.txt thesaurus has been sorted.")
