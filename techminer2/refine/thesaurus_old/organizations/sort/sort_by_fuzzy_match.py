# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort by Fuzzy Match
===============================================================================


Example:
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.refine.thesaurus_old.organizations import InitializeThesaurus, SortByFuzzyMatch

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create thesaurus
    >>> InitializeThesaurus(root_directory="examples/fintech/", quiet=True).run()

    >>> # Create and run the sorter
    >>> sorter = (
    ...     SortByFuzzyMatch()
    ...     #
    ...     # THESAURUS:
    ...     .having_pattern("Texas")
    ...     .using_match_threshold(70)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("examples/small/")
    ... )
    >>> sorter.run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Sorting thesaurus by fuzzy match...
                File : examples/fintech/data/thesaurus/organizations.the.txt
           Keys like : Texas
      Match thresold : 70
      3 matching keys found
      Sorting process completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : examples/fintech/data/thesaurus/organizations.the.txt
    <BLANKLINE>
        Texas AandM Univ Sch of Law (USA)
          Texas AandM University School of Law, United States
        Univ of North Texas (USA)
          Department of Information Technology & Decision Sciences, University of N...
        Univ of Texas at Austin (USA)
          McCombs School of Business, University of Texas at Austin, United States
        [UKN] Brussels, Belgium (BEL)
          Brussels, Belgium
        [UKN] CESifo, Poschingerstr. 5, Munich, 81679, Germany (DEU)
          CESifo, Poschingerstr. 5, Munich, 81679, Germany
        [UKN] FinTech HK, Hong Kong (HKG)
          FinTech HK, Hong Kong
        [UKN] Hochschule für Wirtschaft Fribourg, Switzerland (CHE)
          Hochschule für Wirtschaft Fribourg, Switzerland
        [UKN] Information Technol, Univeril, Germany (DEU)
          Information Technology, Univeril, Germany
    <BLANKLINE>
    <BLANKLINE>


"""
from techminer2._internals import ParamsMixin
from techminer2.refine.thesaurus_old.user import (
    SortByFuzzyMatch as UserSortByFuzzyMatch,
)


class SortByFuzzyMatch(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def run(self):
        return (
            UserSortByFuzzyMatch()
            .update(**self.params.__dict__)
            .with_thesaurus_file("organizations.the.txt")
            .run()
        )


# =============================================================================
