"""
Sort by Key Length
===============================================================================


Smoke tests:
    >>> import sys
    >>> from io import StringIO
    >>> from tm2p.refine.thesaurus_old.system.descriptors import SortByKeyLength

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Configure and run the sorter
    >>> SortByKeyLength().run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = StringIO()
    >>> print(output)  # doctest: +SKIP
    Sorting thesaurus by key length...
      File : /Volumes/GitHub/tm2p/tm2p/_internals/package_data/thesaurus/system/descriptors.the.txt
      Sorting process completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : /Volumes/GitHub/tm2p/tm2p/_internals/package_data/thesaurus/system/descriptors.the.txt
    <BLANKLINE>
        ELMAN_RECURRENT_NEURAL_NETWORK
          ELMAN_NEURAL_NETWORK; ELMAN_NEURAL_NETWORKS
        TEMPORAL_FUSION_TRANSFORMER
          TEMPORAL_FUSION_TRANSFORMERS
        ARTIFICIAL_NEURAL_NETWORK
          ARTIFICIAL_NEURAL_NETWORKS; ARTIFICIAL_NEURAL_NETWORK_MODEL; ARTIFICIAL_N...
        ECHO_STATE_NEURAL_NETWORK
          ECHO_STATE_NETWORK; ECHO_STATE_NETWORKS; ECHO_STATE_NEURAL_NETWORKS
        SYNTHESIZER_TRANSFORMER
          SYNTHESIZER_TRANSFORMERS
        GRAPH_NEURAL_NETWORK
          GRAPH_NEURAL_NETWORKS
        K_NEAREST_NEIGHBORS
          KNN_METHOD
        TRANSFORMER_NETWORK
          TRANSFORMER_NETWORKS
    <BLANKLINE>
    <BLANKLINE>


"""

from tm2p.refine.thesaurus_old.user import SortByKeyLength as UserSortByKeyLength


class SortByKeyLength(
    UserSortByKeyLength,
):
    """:meta private:"""

    def run(self):

        self.with_thesaurus_file("system/descriptors.the.txt")
        self.internal__build_system_thesaurus_path()
        self.internal__run()


# =============================================================================
