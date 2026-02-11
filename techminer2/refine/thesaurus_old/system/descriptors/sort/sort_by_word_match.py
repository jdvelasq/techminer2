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


Smoke tests:
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.refine.thesaurus_old.system.descriptors import SortByWordMatch

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Configure and run the sorter
    >>> (
    ...     SortByWordMatch()
    ...     .having_pattern("CREDIT")
    ...     .run()
    ... )

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)  # doctest: +SKIP
    Sorting thesaurus by word match...
      File : ...techminer2/_internals/package_data/thesaurus/system/descriptors.the.txt
      Word : CREDIT
      0 matching keys found
      Sorting process completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : /Volumes/GitHub/techminer2/techminer2/_internals/package_data/thesaurus/system/descriptors.the.txt
    <BLANKLINE>
        ANALYSIS
          ANALYZES
        APPLICATION
          APPLICATIONS
        APPROACH
          APPROACHES
        ARTICLE
          ARTICLES
        ARTIFICIAL_NEURAL_NETWORK
          ARTIFICIAL_NEURAL_NETWORKS; ARTIFICIAL_NEURAL_NETWORK_MODEL; ARTIFICIAL_N...
        AUTHOR
          AUTHORS
        BIBLIOMETRICS
          BIBLIOMETRIC
        BLOCK_CHAIN
          BLOCK_CHAINS; BLOCKCHAIN; BLOCKCHAINS
    <BLANKLINE>
    <BLANKLINE>




"""
from techminer2.refine.thesaurus_old.user import SortByWordMatch as UserSortByWordMatch


class SortByWordMatch(
    UserSortByWordMatch,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def run(self):

        self.with_thesaurus_file("system/descriptors.the.txt")
        self.internal__build_system_thesaurus_path()
        self.internal__run()


# =============================================================================
