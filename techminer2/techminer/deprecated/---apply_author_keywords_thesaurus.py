"""
Apply 'author_keywords.txt' Thesaurus
===============================================================================

Transforms 'raw_author_keywords' column in 'author_keywords' using author_keywrords.txt thesaurus.

# >>> from techminer2 import *
# >>> directory = "data/regtech/"

# >>> apply_keywords_thesaurus(directory)


"""

import glob
import os
import os.path
import sys

import pandas as pd

from ..._lib._thesaurus import read_textfile


def apply_author_keywords_thesaurus(directory="./"):
    """Transforms 'raw_author_keywords' column in 'author_keywords' using author_keywrords.txt thesaurus."""

    sys.stdout.write("--INFO-- Applying `author_keywords.txt` thesaurus\n")

    thesaurus_file = os.path.join(directory, "processed", "author_keywords.txt")
    if os.path.isfile(thesaurus_file):
        thesaurus = read_textfile(thesaurus_file)
        thesaurus = thesaurus.compile_as_dict()
    else:
        raise FileNotFoundError(f"The file {thesaurus_file} does not exist.")
    #

    files = list(glob.glob(os.path.join(directory, "processed/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        #
        if "raw_author_keywords" in data.columns:
            data = data.assign(author_keywords=data.raw_author_keywords.str.split(";"))
            data = data.assign(
                author_keywords=data.author_keywords.map(
                    lambda x: [thesaurus.apply_as_dict(y.strip()) for y in x]
                    if isinstance(x, list)
                    else x
                )
            )
            data = data.assign(
                author_keywords=data.author_keywords.map(
                    lambda x: sorted(set(x)) if isinstance(x, list) else x
                )
            )
            data = data.assign(author_keywords=data.author_keywords.str.join("; "))

        #
        data.to_csv(file, sep=",", encoding="utf-8", index=False)
