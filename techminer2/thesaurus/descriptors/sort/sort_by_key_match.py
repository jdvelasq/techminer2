# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort By Key Match
===============================================================================

>>> from techminer2.thesaurus.descriptors import CreateThesaurus
>>> CreateThesaurus(root_directory="example/", quiet=True).run()


>>> from techminer2.thesaurus.descriptors import SortByKeyMatch
>>> (
...     SortByKeyMatch()
...     # 
...     # THESAURUS:
...     .having_pattern("BLOCK")
...     .having_case_sensitive(False)
...     .having_regex_flags(0)
...     .having_regex_search(False)
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     #
...     .run()
... ) 
Sorting thesaurus file by key match
            File : example/thesaurus/descriptors.the.txt
         Pattern : BLOCK
  Case sensitive : False
     Regex Flags : 0
    Regex Search : False
  6 matching keys found
Thesaurus sorting by key match completed successfully
<BLANKLINE>
Printing thesaurus header
  File : example/thesaurus/descriptors.the.txt
<BLANKLINE>
    A_BLOCKCHAIN_IMPLEMENTATION_STUDY
      A_BLOCKCHAIN_IMPLEMENTATION_STUDY
    BLOCKCHAIN
      BLOCKCHAIN; BLOCKCHAINS
    BLOCKCHAIN_AND_FINTECH_INNOVATIONS
      BLOCKCHAIN_AND_FINTECH_INNOVATIONS
    BLOCKCHAIN_ENABLES
      BLOCKCHAIN_ENABLES
    BLOCKCHAIN_IMPLEMENTATION
      BLOCKCHAIN_IMPLEMENTATION
    BLOCKCHAIN_USE_CASES
      BLOCKCHAIN_USE_CASES
    A_A_)_THEORY
      A_A_)_THEORY
    A_A_THEORY
      A_A_THEORY
<BLANKLINE>


"""
from ...._internals.mixins import ParamsMixin
from ...user import SortByKeyMatch as UserSortByKeyMatch


class SortByKeyMatch(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def run(self):
        return (
            UserSortByKeyMatch()
            .update(**self.params.__dict__)
            .with_thesaurus_file("descriptors.the.txt")
            .run()
        )


# ===============================================================================
