# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort by Fuzzy Key Match
===============================================================================


>>> # TEST PREPARATION
>>> import sys
>>> from io import StringIO
>>> old_stderr = sys.stderr
>>> sys.stderr = StringIO()
>>> #
>>> from techminer2.thesaurus.descriptors import CreateThesaurus
>>> CreateThesaurus(root_directory="example/", quiet=True).run()


>>> from techminer2.thesaurus.descriptors import SortByFuzzyKeyMatch
>>> (
...     SortByFuzzyKeyMatch()
...     # 
...     # THESAURUS:
...     .having_pattern("INFORM")
...     .having_match_threshold(50)
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     #
...     .run()
... ) 


>>> # TEST EXECUTION
>>> output = sys.stderr.getvalue()
>>> sys.stderr = old_stderr
>>> print(output)
Sorting thesaurus by fuzzy match
            File : example/thesaurus/descriptors.the.txt
       Keys like : INFORM
  Match thresold : 50
  95 matching keys found
  Thesaurus sorting completed successfully
<BLANKLINE>
Printing thesaurus header
  File : example/thesaurus/descriptors.the.txt
<BLANKLINE>
    A_DISINTERMEDIATION_FORCE
      A_DISINTERMEDIATION_FORCE
    A_FIRM
      A_FIRM
    A_FORM
      A_FORM
    A_NEW_INTERMEDIARY
      A_NEW_INTERMEDIARY
    A_PLATFORM
      A_PLATFORM
    ANY_FORM
      ANY_FORM
    BUSINESS_INFRASTRUCTURE
      BUSINESS_INFRASTRUCTURE; BUSINESS_INFRASTRUCTURES
    CLASSIFICATION (OF_INFORMATION)
      CLASSIFICATION (OF_INFORMATION)
<BLANKLINE>
<BLANKLINE>


"""
from ...._internals.mixins import ParamsMixin
from ...user import SortByFuzzyKeyMatch as UserSortByFuzzyKeyMatch


class SortByFuzzyKeyMatch(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def run(self):
        return (
            UserSortByFuzzyKeyMatch()
            .update(**self.params.__dict__)
            .with_thesaurus_file("descriptors.the.txt")
            .run()
        )


# =============================================================================
