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

## >>> from techminer2.prepare.thesaurus.countries import find_string
## >>> find_string(
## ...     #
## ...     # SEARCH PARAMS:
## ...     contains='Colombia',
## ...     startswith=None,
## ...     endswith=None,
## ...     #
## ...     # DATABASE PARAMS:
## ...     root_dir="example/", 
## ... )
--INFO-- The file example/thesauri/countries.the.txt has been reordered.

"""
# from ..user.sort_thesaurus_by_match import thesaurus__sort_by_match

THESAURUS_FILE = "thesauri/countries.the.txt"


def sort_thesaurus_by_match(
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

    return thesaurus__sort_by_match(
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
