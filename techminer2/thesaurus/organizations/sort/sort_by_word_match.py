# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort by Word Match
===============================================================================


Example:
    >>> # TEST PREPARATION
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.organizations import CreateThesaurus, SortByWordMatch

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create thesaurus
    >>> CreateThesaurus(root_directory="example/", quiet=True).run()


    >>> # Create and run the sorter
    >>> sorter = (
    ...     SortByWordMatch()
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
    Reducing thesaurus keys
      File : example/data/thesaurus/organizations.the.txt
      Keys reduced from 90 to 90
      Reduction process completed successfully
    <BLANKLINE>
    Sorting thesaurus by word match
      File : example/data/thesaurus/organizations.the.txt
      Word : Bank
      2 matching keys found
      Sorting process completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : example/data/thesaurus/organizations.the.txt
    <BLANKLINE>
        Fed Reserv Bank of Chicago (USA)
          Federal Reserve Bank of Chicago, Chicago, IL, United States; Federal Rese...
        Fed Reserv Bank of Philadelphia (USA)
          Federal Reserve Bank of Philadelphia, Philadelphia, PA, United States; Fe...
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
        [UKN] Johns Hopkins SAIS, Washington, DC, United States (USA)
          Johns Hopkins SAIS, Washington, DC, United States
    <BLANKLINE>
    <BLANKLINE>

"""
from ...._internals.mixins import ParamsMixin
from ...user import SortByWordMatch as UserSortByWordMatch


class SortByWordMatch(
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
