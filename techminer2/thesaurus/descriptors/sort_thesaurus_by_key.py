# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort Thesaurus by Key
===============================================================================


>>> # with_keys_order_by: "alphabetical", "key_length", "word_length"
>>> from techminer2.thesaurus.descriptors import SortThesaurusByKey
>>> (
...     SortThesaurusByKey()
...     # 
...     # THESAURUS:
...     .having_keys_ordered_by("alphabetical")
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     #
...     .build()
... )
--INFO-- The thesaurus file 'examples/thesaurus/descriptors.the.txt' has been ordered alphabetically.

"""
# from ..user.sort_thesaurus_by_key import thesaurus__sort_on_disk as core_sort_thesaurus

THESAURUS_FILE = "thesauri/descriptors.the.txt"


def sort_thesaurus(
    #
    # SORT OPTIONS:
    order="alphabetical",
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """:meta private:"""

    core_sort_thesaurus(
        #
        # FILE PARAMS:
        thesaurus_file=THESAURUS_FILE,
        order=order,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
    )
