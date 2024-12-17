# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort Thesaurus
===============================================================================


>>> from techminer2.thesaurus.countries import sort_thesaurus
>>> sort_thesaurus(
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
... )
--INFO-- The file example/thesauri/countries.the.txt has been sorted.

"""
from ..internals.thesaurus__sort_on_disk import (
    thesaurus__sort_on_disk as _sort_thesaurus,
)

THESAURUS_FILE = "thesauri/countries.the.txt"


def sort_thesaurus(
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """:meta private:"""

    _sort_thesaurus(
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        #
        # FILE PARAMS:
        thesaurus_file=THESAURUS_FILE,
    )
