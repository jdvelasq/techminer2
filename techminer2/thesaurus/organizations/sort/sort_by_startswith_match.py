# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort by Starts With Match
===============================================================================


Example:
    >>> # TEST PREPARATION
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.organizations import InitializeThesaurus, SortByStartsWithMatch

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create thesaurus
    >>> InitializeThesaurus(root_directory="example/", quiet=True).run()

    >>> # Create and run the sorter
    >>> sorter = (
    ...     SortByStartsWithMatch(use_colorama=False)
    ...     #
    ...     # THESAURUS:
    ...     .having_pattern("Univ")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory_is("examples/fintech/")
    ... )
    >>> sorter.run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Sorting thesaurus by startswith match...
         File : example/data/thesaurus/organizations.the.txt
      Pattern : Univ
      26 matching keys found
      Sorting process completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : example/data/thesaurus/organizations.the.txt
    <BLANKLINE>
        Univ Brunei Darussalam (BRN)
          Universiti Brunei Darussalam, School of Business and Economics, Jln Tungk...
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
    <BLANKLINE>
    <BLANKLINE>


"""
from ...._internals.mixins import ParamsMixin
from ...user import SortByStartsWithMatch as UserSortByStartsWithMatch


class SortByStartsWithMatch(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def run(self):
        return (
            UserSortByStartsWithMatch()
            .update(**self.params.__dict__)
            .with_thesaurus_file("organizations.the.txt")
            .run()
        )


# =============================================================================
