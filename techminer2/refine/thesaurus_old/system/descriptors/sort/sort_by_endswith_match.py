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


Smoke tests:
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.refine.thesaurus_old.system.descriptors import SortByEndsWithMatch

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Configure and run the sorter
    >>> (
    ...     SortByEndsWithMatch()
    ...     .having_pattern("BANKS")
    ...     .run()
    ... )

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Sorting thesaurus by endswith match...
         File : ...techminer2/_internals/package_data/thesaurus/system/descriptors.the.txt
      Pattern : BANKS
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
from techminer2.refine.thesaurus_old.user import (
    SortByEndsWithMatch as UserSortByEndsWithMatch,
)


class SortByEndsWithMatch(
    UserSortByEndsWithMatch,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def run(self):

        self.with_thesaurus_file("system/descriptors.the.txt")
        self.internal__build_system_thesaurus_path()
        self.internal__run()


# =============================================================================
