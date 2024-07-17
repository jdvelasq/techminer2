# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Find String in Organizations Thesaurus
===============================================================================

Finds a string in the terms of a thesaurus.


>>> from techminer2.refine.thesaurus.organizations import find_string_in_organizations_thesaurus
>>> find_string_in_organizations_thesaurus(
...     #
...     # SEARCH PARAMS:
...     contains='ABES',
...     startswith=None,
...     endswith=None,
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
... )
--INFO-- The file example/thesauri/organizations.the.txt has been reordered.

"""
from ...core.thesaurus.find_string_in_thesaurus import find_string_in_thesaurus

THESAURUS_FILE = "thesauri/organizations.the.txt"


def find_string_in_organizations_thesaurus(
    #
    # SEARCH PARAMS:
    contains=None,
    startswith=None,
    endswith=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """Find the specified keyword and reorder the thesaurus file.

    :meta private:
    """

    return find_string_in_thesaurus(
        #
        # THESAURUS FILE:
        thesaurus_file=THESAURUS_FILE,
        #
        # SEARCH PARAMS:
        contains=contains,
        startswith=startswith,
        endswith=endswith,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
    )
