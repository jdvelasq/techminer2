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
>>> from techminer2.thesaurus.organizations import CreateThesaurus
>>> CreateThesaurus(root_directory="example/", quiet=True).run()


>>> from techminer2.thesaurus.organizations import SortByFuzzyKeyMatch
>>> (
...     SortByFuzzyKeyMatch()
...     # 
...     # THESAURUS:
...     .having_pattern("Texas")
...     .having_match_threshold(70)
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
            File : example/thesaurus/organizations.the.txt
       Keys like : Texas
  Match thresold : 70
  3 matching keys found
  Thesaurus sorting completed successfully
<BLANKLINE>
Printing thesaurus header
  File : example/thesaurus/organizations.the.txt
<BLANKLINE>
    Texas AandM Univ Sch of Law (USA)
      Texas AandM University School of Law, United States
    Univ of North Texas (USA)
      Department of Information Technology & Decision Sciences, University of N...
    Univ of Texas at Austin (USA)
      McCombs School of Business, University of Texas at Austin, United States
    Anhui Univ of Finan and Econ (CHN)
      School of Finance, Anhui University of Finance and Economics, Bengbu, 233...
    Baekseok Univ (KOR)
      Division of Tourism, Baekseok University, South Korea
    Baewha Women’s Univ (KOR)
      Department of Information Security, Baewha Women’s University, Seoul, Sou...
    Baylor Univ (USA)
      Baylor University, United States; Hankamer School of Business, Baylor Uni...
    Beihang Univ (CHN)
      School of Economics and Management, Beihang University, China
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
            .with_thesaurus_file("organizations.the.txt")
            .run()
        )


# =============================================================================
