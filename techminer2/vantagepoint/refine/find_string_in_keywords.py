"""
Find String in keywords
===============================================================================

Finds a string in the terms of the keywords thesaurus.


>>> directory = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> vantagepoint.refine.find_string_in_keywords(
...     contains='states',
...     directory=directory,
... )
--INFO-- The file data/regtech/processed/keywords.txt has been reordered.

"""
from . import find_string


def find_string_in_keywords(
    contains=None,
    startswith=None,
    endswith=None,
    directory="./",
):
    """Find the specified keyword and reorder the keywords thesaurus to reflect the search."""

    return find_string(
        thesaurus_file="keywords.txt",
        contains=contains,
        startswith=startswith,
        endswith=endswith,
        directory=directory,
    )
