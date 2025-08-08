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
    >>> from techminer2.thesaurus.descriptors import InitializeThesaurus, SortByOccurrences

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create the thesaurus
    >>> InitializeThesaurus(root_directory="examples/fintech/", quiet=True).run()

    >>> # Configure and run the sorter
    >>> sorter = (
    ...     SortByOccurrences(use_colorama=False)
    ...     .where_root_directory_is("examples/fintech/")
    ... )
    >>> sorter.run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = StringIO()
    >>> print(output)
    Sorting thesaurus by occurrences...
      File : examples/fintech/data/thesaurus/descriptors.the.txt
      Sorting process completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : examples/fintech/data/thesaurus/descriptors.the.txt
    <BLANKLINE>
        FINTECH
          FINTECH; FINTECHS
        FINANCE
          FINANCE
        TECHNOLOGIES
          TECHNOLOGIES; TECHNOLOGY
        INNOVATION
          INNOVATION; INNOVATIONS
        FINANCIAL_SERVICE
          FINANCIAL_SERVICE; FINANCIAL_SERVICES
        FINANCIAL_TECHNOLOGIES
          FINANCIAL_TECHNOLOGIES; FINANCIAL_TECHNOLOGY
        BANKS
          BANKS
        THE_DEVELOPMENT
          THE_DEVELOPMENT; THE_DEVELOPMENTS
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


# =============================================================================
