# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Find String 
===============================================================================

Finds a string in the terms of a thesaurus.


# >>> from techminer2.thesaurus.references import find_string
# >>> find_string(
# ...     #
# ...     # SEARCH PARAMS:
# ...     contains='ARTIFICIAL_INTELLIGENCE',
# ...     startswith=None,
# ...     endswith=None,
# ...     #
# ...     # DATABASE PARAMS:
# ...     root_dir="example/", 
# ... )



"""
from .._core.find_string_in_thesaurus import find_string_in_thesaurus

THESAURUS_FILE = "thesauri/references.the.txt"


def find_string(
    #
    # SEARCH PARAMS:
    contains=None,
    startswith=None,
    endswith=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """:meta private:"""

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
