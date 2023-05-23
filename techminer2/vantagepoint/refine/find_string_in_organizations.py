"""
Find String in organizations
===============================================================================

Finds a string in the terms of the organizations thesaurus.


>>> directory = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> vantagepoint.refine.find_string_in_organizations(
...     contains='China',
...     directory=directory,
... )
--INFO-- The file data/regtech/processed/organizations.txt has been reordered.

"""
from . import find_string


def find_string_in_organizations(
    contains=None,
    startswith=None,
    endswith=None,
    directory="./",
):
    """Find the specified keyword and reorder the organizations thesaurus to reflect the search."""

    return find_string(
        thesaurus_file="organizations.txt",
        contains=contains,
        startswith=startswith,
        endswith=endswith,
        directory=directory,
    )
