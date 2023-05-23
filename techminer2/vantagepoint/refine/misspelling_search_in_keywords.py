"""
Misspelling search in keywords
===============================================================================

Look for misspeling mistakes in the keywords thesaurus.

>>> directory = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> vantagepoint.refine.misspelling_search(directory=directory)
--INFO-- The file data/regtech/processed/misspelled.txt has been generated.


"""
from . import misspelling_search


def misspelling_search_in_keywods(directory="./"):
    """Look for misspeling mistakes in the "keywords.txt" thesaurus."""

    return misspelling_search(
        thesaurus_file="keywords.txt",
        directory=directory,
    )
