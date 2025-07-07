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


Example:
    >>> # TEST PREPARATION
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.organizations import CreateThesaurus, SortByKeyMatch

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create thesaurus
    >>> CreateThesaurus(root_directory="example/", quiet=True).run()

    >>> # Create and run the sorter
    >>> sorter = (
    ...     SortByKeyMatch()
    ...     #
    ...     # THESAURUS:
    ...     .having_pattern("Sch")
    ...     .having_case_sensitive(False)
    ...     .having_regex_flags(0)
    ...     .having_regex_search(False)
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
      Keys reduction completed successfully
    <BLANKLINE>
    Sorting thesaurus file by key match
                File : example/data/thesaurus/organizations.the.txt
             Pattern : Sch
      Case sensitive : False
         Regex Flags : 0
        Regex Search : False
      12 matching keys found
      Thesaurus sorting by key match completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : example/data/thesaurus/organizations.the.txt
    <BLANKLINE>
        [UKN] CESifo, Poschingerstr. 5, Munich, 81679, Germany (DEU)
          CESifo, Poschingerstr. 5, Munich, 81679, Germany
        [UKN] Hochschule für Wirtschaft Fribourg, Switzerland (CHE)
          Hochschule für Wirtschaft Fribourg, Switzerland
        Columbia Grad Sch of Bus (USA)
          Columbia Graduate School of Business, United States
        Copenhagen Bus Sch (DNK)
          Copenhagen Business School, Department of IT Management, Howitzvej 60, Fr...
        Harvard Law Sch (USA)
          Harvard Law School, United States
        Henley Bus Sch (GBR)
          Henley Business School, United Kingdom
        Kingston Bus Sch (GBR)
          Kingston Business School, Department of Accounting, Finance and Informati...
        London Sch of Econ (GBR)
          London School of Economics, United Kingdom
    <BLANKLINE>
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
            .with_thesaurus_file("organizations.the.txt")
            .run()
        )


# ===============================================================================
