# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort by Starts With Key Match
===============================================================================


Example:
    >>> # TEST PREPARATION
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.organizations import CreateThesaurus, SortByStartsWithKeyMatch

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create thesaurus
    >>> CreateThesaurus(root_directory="example/", quiet=True).run()

    >>> # Create and run the sorter
    >>> sorter = (
    ...     SortByStartsWithKeyMatch()
    ...     #
    ...     # THESAURUS:
    ...     .having_pattern("Univ")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory_is("example/")
    ... )
    >>> sorter.run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Sorting thesaurus file by key match
         File : example/thesaurus/organizations.the.txt
      Pattern : Univ
      25 matching keys found
      Thesaurus sorting by key match completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : example/thesaurus/organizations.the.txt
    <BLANKLINE>
        Univ di Padova (ITA)
          Università di Padova, Italy
        Univ Gadjah Mada (IDN)
          Department of Management, Faculty of Economics and Business, Universitas ...
        Univ Koblenz-Landau (DEU)
          Institute for Software Technology IST, Universität Koblenz-Landau, Koblen...
        Univ of Augsburg (DEU)
          FIM Research Center, University of Augsburg, Augsburg, 86135, Germany
        Univ of Bremen (DEU)
          Faculty of Business Studies and Economics, University of Bremen, Wilhelm-...
        Univ of Chicago (USA)
          University of Chicago, United States
        Univ of Delaware (USA)
          Lerner College of Business and Economics, University of Delaware, United ...
        Univ of Groningen (NLD)
          Faculty of Economics and Business, University of Groningen, Nettelbosje 2...
    <BLANKLINE>
    <BLANKLINE>

"""
from ...._internals.mixins import ParamsMixin
from ...user import SortByStartsWithKeyMatch as UserSortByStartsWithKeyMatch


class SortByStartsWithKeyMatch(
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
