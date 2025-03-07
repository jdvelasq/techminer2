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


Example:
    >>> # TEST PREPARATION
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.organizations import CreateThesaurus, SortByEndsWithKeyMatch

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create thesaurus
    >>> CreateThesaurus(root_directory="example/", quiet=True).run()

    >>> # Create and run the sorter
    >>> sorter = (
    ...     SortByEndsWithKeyMatch()
    ...     .having_pattern("(AUS)")
    ...     .where_root_directory_is("example/")
    ... )
    >>> sorter.run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Sorting thesaurus file by key match
         File : example/thesaurus/organizations.the.txt
      Pattern : (AUS)
      4 matching keys found
      Thesaurus sorting by key match completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : example/thesaurus/organizations.the.txt
    <BLANKLINE>
        Cent for Law, Markets & Regulation, UNSW Australia, Australia (AUS)
          Centre for Law, Markets & Regulation, UNSW Australia, Australia
        Charles Sturt Univ Melbourne Study Group Cent (AUS)
          Charles Sturt University Melbourne Study Group Centre, Melbourne, VIC, Au...
        Univ of New South Wales (AUS)
          UNSW Business School, University of New South Wales, Australia; Universit...
        Univ of Sydney (AUS)
          The University of Sydney, The University of Sydney Business School, Rm407...
        Anhui Univ of Finan and Econ (CHN)
          School of Finance, Anhui University of Finance and Economics, Bengbu, 233...
        Baekseok Univ (KOR)
          Division of Tourism, Baekseok University, South Korea
        Baewha Women’s Univ (KOR)
          Department of Information Security, Baewha Women’s University, Seoul, Sou...
        Baylor Univ (USA)
          Baylor University, United States; Hankamer School of Business, Baylor Uni...
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
            .with_thesaurus_file("organizations.the.txt")
            .run()
        )


# =============================================================================
