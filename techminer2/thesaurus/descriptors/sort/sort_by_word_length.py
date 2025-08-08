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
    >>> from techminer2.thesaurus.descriptors import InitializeThesaurus, SortByWordLength

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create the thesaurus
    >>> InitializeThesaurus(root_directory="examples/fintech/", quiet=True).run()

    >>> # Configure and run the sorter
    >>> sorter = (
    ...     SortByWordLength(use_colorama=False)
    ...     .where_root_directory_is("examples/fintech/")
    ... )
    >>> sorter.run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Sorting thesaurus by word length...
      File : examples/fintech/data/thesaurus/descriptors.the.txt
      Sorting process completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : examples/fintech/data/thesaurus/descriptors.the.txt
    <BLANKLINE>
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
        EXPLORE_INTERRELATIONSHIPS
          EXPLORE_INTERRELATIONSHIPS
        A_DISINTERMEDIATION_FORCE
          A_DISINTERMEDIATION_FORCE
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
