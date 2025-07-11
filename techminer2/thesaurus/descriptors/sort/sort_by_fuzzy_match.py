# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort by Fuzzy Match
===============================================================================


Example:
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.descriptors import InitializeThesaurus, SortByFuzzyMatch

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create the thesaurus
    >>> InitializeThesaurus(root_directory="example/", quiet=True).run()

    >>> # Configure and run the sorter
    >>> sorter = (
    ...     SortByFuzzyMatch()
    ...     .having_pattern("INFORM")
    ...     .having_match_threshold(50)
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
    Sorting thesaurus by fuzzy match
                File : example/data/thesaurus/descriptors.the.txt
           Keys like : INFORM
      Match thresold : 50
      92 matching keys found
      Sorting process completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : example/data/thesaurus/descriptors.the.txt
    <BLANKLINE>
        A_DISINTERMEDIATION_FORCE
          A_DISINTERMEDIATION_FORCE
        A_FIRM
          A_FIRM
        A_FORM
          A_FORM
        A_NEW_INTERMEDIARY
          A_NEW_INTERMEDIARY
        A_PLATFORM
          A_PLATFORM
        BUSINESS_INFRASTRUCTURE
          BUSINESS_INFRASTRUCTURE; BUSINESS_INFRASTRUCTURES
        CHANGE_FINANCIAL_INTERMEDIATION_STRUCTURES
          CHANGE_FINANCIAL_INTERMEDIATION_STRUCTURES
        CLASSIFICATION (OF_INFORMATION)
          CLASSIFICATION (OF_INFORMATION)
    <BLANKLINE>
    <BLANKLINE>



"""
from ...._internals.mixins import ParamsMixin
from ...user import SortByFuzzyMatch as UserSortByFuzzyMatch


class SortByFuzzyMatch(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def run(self):
        return (
            UserSortByFuzzyMatch()
            .update(**self.params.__dict__)
            .with_thesaurus_file("descriptors.the.txt")
            .run()
        )


# =============================================================================
