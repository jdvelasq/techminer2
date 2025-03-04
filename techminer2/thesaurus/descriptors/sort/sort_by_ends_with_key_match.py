# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort By Ends With Key Match
===============================================================================


>>> # TEST PREPARATION:
>>> import sys
>>> from io import StringIO
>>> old_stderr = sys.stderr
>>> sys.stderr = StringIO()
>>> #
>>> from techminer2.thesaurus.descriptors import CreateThesaurus
>>> CreateThesaurus(root_directory="example/", quiet=True).run()


>>> from techminer2.thesaurus.descriptors import SortByEndsWithKeyMatch
>>> (
...     SortByEndsWithKeyMatch()
...     # 
...     # THESAURUS:
...     .having_pattern("BANKS")
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     #
...     .run()
... ) 


>>> # TEST EXECUTION:
>>> output = sys.stderr.getvalue()
>>> sys.stderr = old_stderr
>>> print(output)
Sorting thesaurus file by key match
     File : example/thesaurus/descriptors.the.txt
  Pattern : BANKS
  14 matching keys found
  Thesaurus sorting by key match completed successfully
<BLANKLINE>
Printing thesaurus header
  File : example/thesaurus/descriptors.the.txt
<BLANKLINE>
    BANKS
      BANKS
    CITY_COMMERCIAL_BANKS
      CITY_COMMERCIAL_BANKS
    COMMERCIAL_BANKS
      COMMERCIAL_BANKS
    ENABLE_BANKS
      ENABLE_BANKS
    FIVE_MAJOR_COMMERCIAL_BANKS
      FIVE_MAJOR_COMMERCIAL_BANKS
    INCUMBENT_RETAIL_BANKS
      INCUMBENT_RETAIL_BANKS
    LEADING_EUROPEAN_AND_US_BANKS
      LEADING_EUROPEAN_AND_US_BANKS
    MOST_BANKS
      MOST_BANKS
<BLANKLINE>
<BLANKLINE>


"""
from ...._internals.mixins import ParamsMixin
from ...user import SortByEndsWithKeyMatch as UserSortByStartsWithKeyMatch


class SortByEndsWithKeyMatch(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def run(self):
        return (
            UserSortByStartsWithKeyMatch()
            .update(**self.params.__dict__)
            .with_thesaurus_file("descriptors.the.txt")
            .run()
        )


# =============================================================================
