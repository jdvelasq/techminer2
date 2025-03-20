# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort by Word Key Match
===============================================================================


Example:
    >>> # TEST PREPARATION
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.organizations import CreateThesaurus, SortByWordKeyMatch

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create thesaurus
    >>> CreateThesaurus(root_directory="example/", quiet=True).run()


    >>> # Create and run the sorter
    >>> sorter = (
    ...     SortByWordKeyMatch()
    ...     #
    ...     # THESAURUS:
    ...     .having_pattern("Bank")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory_is("example/")
    ... )
    >>> sorter.run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Sorting thesaurus file by word match
      File : example/thesaurus/organizations.the.txt
      Word : Bank
      2 matching keys found
      Thesaurus sorting by word match completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : example/thesaurus/organizations.the.txt
    <BLANKLINE>
        Fed Reserv Bank of Chicago (USA)
          Federal Reserve Bank of Chicago, Chicago, IL, United States; Federal Rese...
        Fed Reserv Bank of Philadelphia (USA)
          Federal Reserve Bank of Philadelphia, Philadelphia, PA, United States; Fe...
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
        Brussels, Belgium (BEL)
          Brussels, Belgium
    <BLANKLINE>
    <BLANKLINE>


"""
from ...._internals.mixins import ParamsMixin
from ...user import SortByWordKeyMatch as UserSortByWordMatch


class SortByWordKeyMatch(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def run(self):
        return (
            UserSortByWordMatch()
            .update(**self.params.__dict__)
            .with_thesaurus_file("organizations.the.txt")
            .run()
        )


# =============================================================================
