"""
Apply `'index_keywords.txt'` Thesaurus
===============================================================================

Transforms 'raw_index_keywords' column in 'index_keywords' using index_keywrords.txt thesaurus.

>>> from techminer2 import *
>>> directory = "data/"

>>> apply_index_keywords_thesaurus(directory)


"""

import glob
import os
import os.path
import sys

import pandas as pd

from .thesaurus import read_textfile


def apply_index_keywords_thesaurus(directory="./"):
    """Transforms 'raw_index_keywords' column in 'index_keywords' using index_keywrords.txt thesaurus."""

    sys.stdout.write("--INFO-- Applying `index_keywords.txt` thesaurus\n")

    thesaurus_file = os.path.join(directory, "processed", "index_keywords.txt")
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
        if "raw_index_keywords" in data.columns:
            data = data.assign(index_keywords=data.raw_index_keywords.str.split(";"))
            data = data.assign(
                index_keywords=data.index_keywords.map(
                    lambda x: [thesaurus.apply_as_dict(y.strip()) for y in x]
                    if isinstance(x, list)
                    else x
                )
            )
            data = data.assign(
                index_keywords=data.index_keywords.map(
                    lambda x: sorted(set(x)) if isinstance(x, list) else x
                )
            )
            data = data.assign(index_keywords=data.index_keywords.str.join("; "))

        #
        data.to_csv(file, sep=",", encoding="utf-8", index=False)
