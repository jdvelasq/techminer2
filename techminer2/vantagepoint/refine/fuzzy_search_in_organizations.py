"""
Fuzzy Search in organizations
===============================================================================

Finds a string in the terms of the organizations thesaurus using fuzzy search.


>>> directory = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> vantagepoint.refine.fuzzy_search_in_organizations(
...     patterns='univesitat',
...     threshold=80,
...     directory=directory,
... )


"""
from . import fuzzy_search


def fuzzy_search_in_organizations(
    patterns,
    threshold=80,
    directory="./",
):
    """Find the specified term and reorder the organizations thesaurus to reflect the search."""

    return fuzzy_search(
        thesaurus_file="organizations.txt",
        patterns=patterns,
        threshold=threshold,
        directory=directory,
    )
