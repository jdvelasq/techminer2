# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort Countries Thesaurus
===============================================================================


>>> from techminer2.refine.thesaurus.countries import sort_countries_thesaurus
>>> sort_countries_thesaurus(
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
... )
--INFO-- The file example/thesauri/countries.the.txt has been sorted.

"""
from ...core.thesaurus.sort_thesaurus import sort_thesaurus

THESAURUS_FILE = "thesauri/countries.the.txt"


def sort_countries_thesaurus(
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """:meta private:"""

    sort_thesaurus(
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        #
        # FILE PARAMS:
        thesaurus_file=THESAURUS_FILE,
    )
