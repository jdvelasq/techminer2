# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Reset Thesaurus
===============================================================================


>>> from techminer2.refine.thesaurus.words import reset_thesaurus
>>> reset_thesaurus(
...     #
...     # DATABASE PARAMS:
...     # ...     root_dir="example/", 
...     root_dir="/Volumes/GitHub/tm2_fintech_test",
... )
--INFO-- The file example/thesauri/words.the.txt has been reseted.

"""
import os

THESAURUS_FILE = "thesauri/words.the.txt"


def reset_thesaurus(
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """:meta private:"""

    thesaurus_path = os.path.join(root_dir, THESAURUS_FILE)

    terms = []
    with open(thesaurus_path, "r", encoding="utf-8") as file:
        for line in file:
            if line.startswith(" "):
                key = line.strip()
                terms.append(key)

    with open(thesaurus_path, "w", encoding="utf-8") as file:
        for term in sorted(terms):
            file.write(term + "\n")
            file.write("    " + term + "\n")
