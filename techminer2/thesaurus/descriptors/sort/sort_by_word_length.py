# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort by Word Length
===============================================================================


Example:
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.descriptors import CreateThesaurus, SortByWordLength

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create the thesaurus
    >>> CreateThesaurus(root_directory="example/", quiet=True).run()

    >>> # Configure and run the sorter
    >>> sorter = (
    ...     SortByWordLength()
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
    Sorting thesaurus by word length
      File : example/data/thesaurus/descriptors.the.txt
      Sorting process completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : example/data/thesaurus/descriptors.the.txt
    <BLANKLINE>
        DESIGN/METHODOLOGY/APPROACH
          DESIGN/METHODOLOGY/APPROACH
        RESEARCH_LIMITATIONS/IMPLICATIONS
          RESEARCH_LIMITATIONS/IMPLICATIONS
        COMPETITION (ECONOMICS)
          COMPETITION (ECONOMICS)
        FINANCIAL_TECHNOLOGY (FINTECH)
          FINANCIAL_TECHNOLOGY (FINTECH)
        A_WIDE_RANGING_RECONCEPTUALIZATION
          A_WIDE_RANGING_RECONCEPTUALIZATION
        NETWORKS (CIRCUITS)
          NETWORKS (CIRCUITS)
        THE_RECONCEPTUALIZATION
          THE_RECONCEPTUALIZATION
        CLASSIFICATION (OF_INFORMATION)
          CLASSIFICATION (OF_INFORMATION)
    <BLANKLINE>
    <BLANKLINE>



"""
from ...._internals.mixins import ParamsMixin
from ...user import SortByWordLength as UserSortByWordLength


class SortByWordLength(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def run(self):
        return (
            UserSortByWordLength()
            .update(**self.params.__dict__)
            .with_thesaurus_file("descriptors.the.txt")
            .run()
        )


# =============================================================================
