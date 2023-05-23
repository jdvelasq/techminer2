"""
Fuzzy Search in countries
===============================================================================

Finds a string in the terms of the countries thesaurus using fuzzy search.


>>> directory = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> vantagepoint.refine.fuzzy_search_in_countries(
...     patterns='china',
...     threshold=80,
...     directory=directory,
... )


"""
from . import fuzzy_search


def fuzzy_search_in_countries(
    patterns,
    threshold=80,
    directory="./",
):
    """Find the specified term and reorder the countries thesaurus to reflect the search."""

    return fuzzy_search(
        thesaurus_file="countries.txt",
        patterns=patterns,
        threshold=threshold,
        directory=directory,
    )
