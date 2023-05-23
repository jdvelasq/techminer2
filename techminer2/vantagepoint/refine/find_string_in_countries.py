"""
Find String in countries
===============================================================================

Finds a string in the terms of the countries thesaurus.


>>> directory = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> vantagepoint.refine.find_string_in_countries(
...     contains='states',
...     directory=directory,
... )
--INFO-- The file data/regtech/processed/countries.txt has been reordered.

"""
from . import find_string


def find_string_in_countries(
    contains=None,
    startswith=None,
    endswith=None,
    directory="./",
):
    """Find the specified keyword and reorder the countries thesaurus to reflect the search."""

    return find_string(
        thesaurus_file="countries.txt",
        contains=contains,
        startswith=startswith,
        endswith=endswith,
        directory=directory,
    )
