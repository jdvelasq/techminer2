"""
Sort by Fuzzy Match
===============================================================================


Smoke tests:
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.refine.thesaurus_old.system.descriptors import SortByFuzzyMatch

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Configure and run the sorter
    >>> (
    ...     SortByFuzzyMatch()
    ...     .having_text_matching("INFORM")
    ...     .using_match_threshold(50)
    ...     .run()
    ... )

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)  # doctest: +SKIP
    Sorting thesaurus by fuzzy match...
                File : /Volumes/GitHub/techminer2/techminer2/_internals/package_data/thesaurus/system/descriptors.the.txt
           Keys like : INFORM
      Match thresold : 50
      5 matching keys found
      Sorting process completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : /Volumes/GitHub/techminer2/techminer2/_internals/package_data/thesaurus/system/descriptors.the.txt
    <BLANKLINE>
        BI_LSTM_TRANSFORMER
          BILSTM_TRANSFORMER_MODELS; BILSTM_TRANSFORMER_MODEL
        MULTI_TRANSFORMER
          MULTI_TRANSFORMER_MODELS; MULTI_TRANSFORMER_MODEL
        SYNTHESIZER_TRANSFORMER
          SYNTHESIZER_TRANSFORMER_MODELS; SYNTHESIZER_TRANSFORMER_MODEL
        TEMPORAL_FUSION_TRANSFORMER
          TEMPORAL_FUSION_TRANSFORMER_METHODS; TEMPORAL_FUSION_TRANSFORMER_METHOD
        TRANSFORMER_NETWORK
          TRANSFORMER_NETWORK_ARCHITECTURE
        *ARTICLE*
          ACADEMIC_ARTICLE; ACADEMIC_ARTICLES; ARTICLE; ARTICLES
        *AUTHOR*
          AUTHOR; AUTHORS
        *BIBLIOMETRICS*
          BIBLIOMETRIC; BIBLIOMETRICS
    <BLANKLINE>
    <BLANKLINE>



"""

from tm2p.refine.thesaurus_old.user import SortByFuzzyMatch as UserSortByFuzzyMatch


class SortByFuzzyMatch(
    UserSortByFuzzyMatch,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def run(self):

        self.with_thesaurus_file("system/descriptors.the.txt")
        self.internal__build_system_thesaurus_path()
        self.internal__run()


# =============================================================================
