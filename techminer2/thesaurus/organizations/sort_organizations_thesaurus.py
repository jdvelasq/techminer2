# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort Organizations Thesaurus
===============================================================================


>>> from techminer2.refine.thesaurus.organizations import sort_organizations_thesaurus
>>> sort_organizations_thesaurus(
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
... )
--INFO-- The file example/thesauri/organizations.the.txt has been sorted.

"""
from .._core.sort_thesaurus import sort_thesaurus as core_sort_thesaurus

THESAURUS_FILE = "thesauri/organizations.the.txt"


def sort_organizations_thesaurus(
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """:meta private:"""

    core_sort_thesaurus(
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        #
        # FILE PARAMS:
        thesaurus_file=THESAURUS_FILE,
    )
