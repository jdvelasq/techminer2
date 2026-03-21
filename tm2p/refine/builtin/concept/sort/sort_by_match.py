"""
Sort By Match
===============================================================================


Smoke tests:
    >>> import sys
    >>> from io import StringIO
    >>> from tm2p.refine.thesaurus_old.system.descriptors import SortByMatch

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Configure and run the sorter
    >>> (
    ...     SortByMatch()
    ...     .having_text_matching("BLOCK")
    ...     .having_case_sensitive(False)
    ...     .having_regex_flags(0)
    ...     .having_regex_search(False)
    ...     .run()
    ... )

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)  # doctest: +SKIP
    Sorting thesaurus by match...
                File : ...tm2p/_internals/package_data/thesaurus/system/descriptors.the.txt
             Pattern : BLOCK
      Case sensitive : False
         Regex Flags : 0
        Regex Search : False
      1 matching keys found
      Sorting process completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : /Volumes/GitHub/tm2p/tm2p/_internals/package_data/thesaurus/system/descriptors.the.txt
    <BLANKLINE>
        BLOCK_CHAIN
          BLOCK_CHAINS; BLOCKCHAIN; BLOCKCHAINS
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
    <BLANKLINE>
    <BLANKLINE>


"""

from tm2p.refine.thesaurus_old.user import SortByMatch as UserSortByMatch


class SortByMatch(
    UserSortByMatch,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def run(self):

        self.with_thesaurus_file("system/descriptors.the.txt")
        self.internal__build_system_thesaurus_path()
        self.internal__run()


# ===============================================================================
