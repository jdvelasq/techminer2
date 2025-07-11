# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort By EndsWith Match
===============================================================================


Example:
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.descriptors import InitializeThesaurus, SortByEndsWithMatch

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create the thesaurus
    >>> InitializeThesaurus(root_directory="example/", quiet=True).run()

    >>> # Configure and run the sorter
    >>> sorter = (
    ...     SortByEndsWithMatch()
    ...     .having_pattern("BANKS")
    ...     .where_root_directory_is("example/")
    ... )
    >>> sorter.run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Reducing thesaurus keys
      File : example/data/thesaurus/descriptors.the.txt
      Keys reduced from 1726 to 1726
      Reduction process completed successfully
    <BLANKLINE>
    Sorting thesaurus by endswith match
         File : example/data/thesaurus/descriptors.the.txt
      Pattern : BANKS
      14 matching keys found
      Sorting process completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : example/data/thesaurus/descriptors.the.txt
    <BLANKLINE>
        BANKS
          BANKS
        CITY_COMMERCIAL_BANKS
          CITY_COMMERCIAL_BANKS
        COMMERCIAL_BANKS
          COMMERCIAL_BANKS
        ENABLE_BANKS
          ENABLE_BANKS
        FINTECH_AND_FINANCIAL_INNOVATIONS_THE_BANKS
          FINTECH_AND_FINANCIAL_INNOVATIONS_THE_BANKS
        FIVE_MAJOR_COMMERCIAL_BANKS
          FIVE_MAJOR_COMMERCIAL_BANKS
        INCUMBENT_RETAIL_BANKS
          INCUMBENT_RETAIL_BANKS
        LEADING_EUROPEAN_AND_US_BANKS
          LEADING_EUROPEAN_AND_US_BANKS
    <BLANKLINE>
    <BLANKLINE>


"""
from ...._internals.mixins import ParamsMixin
from ...user import SortByEndsWithMatch as UserSortByEndsWithMatch


class SortByEndsWithMatch(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def run(self):
        return (
            UserSortByEndsWithMatch()
            .update(**self.params.__dict__)
            .with_thesaurus_file("descriptors.the.txt")
            .run()
        )


# =============================================================================
