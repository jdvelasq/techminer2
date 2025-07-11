# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort by Alphabet
===============================================================================


Example:
    >>> # TEST PREPARATION
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.organizations import InitializeThesaurus, SortByAlphabet

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create thesaurus
    >>> InitializeThesaurus(root_directory="example/", quiet=True).run()

    >>> # Create and run the sorter
    >>> sorter = (
    ...     SortByAlphabet()
    ...     .having_keys_ordered_by("alphabetical")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory_is("example/")
    ... )
    >>> sorter.run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Reducing thesaurus keys
      File : example/data/thesaurus/organizations.the.txt
      Keys reduced from 90 to 90
      Reduction process completed successfully
    <BLANKLINE>
    Sorting thesaurus alphabetically
      File : example/data/thesaurus/organizations.the.txt
      Sorting process completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : example/data/thesaurus/organizations.the.txt
    <BLANKLINE>
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
        Cent for Law (AUS)
          Centre for Law, Markets & Regulation, UNSW Australia, Australia
        Charles Sturt Univ Melbourne Study Group Cent (AUS)
          Charles Sturt University Melbourne Study Group Centre, Melbourne, VIC, Au...
        Chung-ang Univ (KOR)
          School of Business, Chung-ang University, Seoul, South Korea
    <BLANKLINE>
    <BLANKLINE>





"""
from ...._internals.mixins import ParamsMixin
from ...user import SortByAlphabet as UserSortByAlphabet


class SortByAlphabet(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        return (
            UserSortByAlphabet()
            .update(**self.params.__dict__)
            .with_thesaurus_file("organizations.the.txt")
            .run()
        )
