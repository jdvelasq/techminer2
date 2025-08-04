# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort by Last Words
===============================================================================


Example:
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.descriptors import InitializeThesaurus, SortByLastWords

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create the thesaurus
    >>> InitializeThesaurus(root_directory="example/", quiet=True).run()

    >>> # Configure and run the sorter
    >>> sorter = (
    ...     SortByLastWords(use_colorama=False)
    ...     .where_root_directory_is("examples/fintech/")
    ... )
    >>> sorter.run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Sorting thesaurus by common last words...
      File : example/data/thesaurus/descriptors.the.txt
      12 matching keys found
      Sorting process completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : example/data/thesaurus/descriptors.the.txt
    <BLANKLINE>
        AGRICULTURE_PLAYS
          AGRICULTURE_PLAYS
        CONTINUANCE_INTENTION_DIFFERS
          CONTINUANCE_INTENTION_DIFFERS
        ENTREPRENEURIAL_ENDEAVOURS
          ENTREPRENEURIAL_ENDEAVOURS
        FOUR_SPECIFIC_INCREASES
          FOUR_SPECIFIC_INCREASES
        LENDINGCLUB_LOANS_INCREASES
          LENDINGCLUB_LOANS_INCREASES
        POSITIVE_RELATIONSHIP_EXISTS
          POSITIVE_RELATIONSHIP_EXISTS
        RESIDENTIAL_MORTGAGE_ORIGINATION
          RESIDENTIAL_MORTGAGE_ORIGINATION
        TAXONOMY_CONTRIBUTES
          TAXONOMY_CONTRIBUTES
    <BLANKLINE>
    <BLANKLINE>

"""
from ...._internals.mixins import ParamsMixin
from ...user import SortByLastWords as UserSortByLastWords


class SortByLastWords(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def run(self):
        return (
            UserSortByLastWords()
            .update(**self.params.__dict__)
            .with_thesaurus_file("descriptors.the.txt")
            .run()
        )


# =============================================================================
