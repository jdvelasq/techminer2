# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort by Occurrences
===============================================================================


Example:
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.descriptors import CreateThesaurus, SortByOccurrences

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create the thesaurus
    >>> CreateThesaurus(root_directory="example/", quiet=True).run()

    ## >>> # Configure and run the sorter
    ## >>> sorter = (
    ## ...     SortByOccurrences()
    ## ...     .where_root_directory_is("example/")
    ## ... )
    ## >>> sorter.run()

    >>> # Configure and run the sorter
    >>> sorter = (
    ...     SortByOccurrences()
    ...     .where_root_directory_is("../tm2_genai_en_analytics/")
    ... )
    >>> sorter.run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = StringIO()
    >>> print(output)
    Reducing thesaurus keys
      File : example/thesaurus/descriptors.the.txt
      Keys reduced from 1736 to 1736
      Keys reduction completed successfully
    <BLANKLINE>
    Sorting thesaurus by occurrences
      File : example/thesaurus/descriptors.the.txt
      Thesaurus sorting completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : example/thesaurus/descriptors.the.txt
    <BLANKLINE>
        FINTECH
          FINTECH; FINTECHS
        FINANCE
          FINANCE
        FINANCIAL_TECHNOLOGIES
          FINANCIAL_TECHNOLOGIES; FINANCIAL_TECHNOLOGY
        INNOVATION
          INNOVATION; INNOVATIONS
        TECHNOLOGIES
          TECHNOLOGIES; TECHNOLOGY
        FINANCIAL_SERVICE
          FINANCIAL_SERVICE; FINANCIAL_SERVICES
        THIS_PAPER
          THIS_PAPER
        THIS_STUDY
          THIS_STUDY
    <BLANKLINE>
    <BLANKLINE>



"""
from ...._internals.mixins import ParamsMixin
from ...user import SortByOccurrences as UserSortByOccurrences


class SortByOccurrences(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        return (
            UserSortByOccurrences()
            .update(**self.params.__dict__)
            .with_thesaurus_file("descriptors.the.txt")
            .with_field("raw_descriptors")
            .run()
        )


def sort_by_occurrences():
    SortByOccurrences().where_root_directory_is("../").run()


# =============================================================================
