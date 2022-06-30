"""
Clean Keywords
===============================================================================

Cleans the keywords columns using the `keywords.txt`file.

>>> from techminer2 import *
>>> directory = "data/"

>>> clean_keywords(directory)
- INFO - Applying thesaurus to 'raw_author_keywords' column ...
- INFO - Applying thesaurus to 'raw_index_keywords' column...
- INFO - Applying thesaurus to 'raw_nlp_document_title' column...
- INFO - Applying thesaurus to 'raw_nlp_abstract' column...
- INFO - Applying thesaurus to 'raw_nlp_phrases' column...
- INFO - The thesaurus was applied to all keywords.


"""
# pylint: disable=no-member
# pylint: disable=invalid-name

import glob
import os
import os.path
import sys

import pandas as pd

from .thesaurus import read_textfile


def clean_keywords(directory="./"):
    """Clean all keywords columns in the records using a thesaurus (keywrords.txt)."""

    sys.stdout.write("--INFO-- Cleaning keywords in database files\n")

    thesaurus_file = os.path.join(directory, "processed", "keywords.txt")
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
                    lambda x: set(x) if isinstance(x, list) else x
                )
            )
            data = data.assign(author_keywords=data.author_keywords.str.join("; "))

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
                    lambda x: set(x) if isinstance(x, list) else x
                )
            )
            data = data.assign(index_keywords=data.index_keywords.str.join("; "))

        #
        data.to_csv(file, sep=",", encoding="utf-8", index=False)
