"""
Fuzzy Search in keywords
===============================================================================

Finds a string in the terms of the keywords thesaurus using fuzzy search.


>>> directory = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> vantagepoint.refine.fuzzy_search_in_keywords(
...     patterns='inteligencia',
...     threshold=80,
...     directory=directory,
... )


"""
from . import fuzzy_search


def fuzzy_search_in_keywords(
    patterns,
    threshold=80,
    directory="./",
):
    """Find the specified term and reorder the keywords thesaurus to reflect the search."""

    return fuzzy_search(
        thesaurus_file="keywords.txt",
        patterns=patterns,
        threshold=threshold,
        directory=directory,
    )
