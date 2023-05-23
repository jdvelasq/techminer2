"""
Find Abbreviations in keywords
===============================================================================

Finds string abbreviations in the keywords of a thesaurus.

>>> directory = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> vantagepoint.refine.find_abbreviations_in_keywords(directory=directory)
--INFO-- The file data/regtech/processed/keywords.txt has been reordered.


"""
from . import find_abbreviations


def find_abbreviations_in_keywords(directory="./"):
    """Find abbreviations and reorder the thesaurus to reflect the search."""

    return find_abbreviations(
        thesaurus_file="keywords.txt",
        directory=directory,
    )
