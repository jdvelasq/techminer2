# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort by Key Length
===============================================================================


Example:
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.system.descriptors import SortByKeyLength

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Configure and run the sorter
    >>> SortByKeyLength(use_colorama=False).run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = StringIO()
    >>> print(output)
    Sorting thesaurus by key length...
      File : /Volumes/GitHub/techminer2/techminer2/package_data/thesaurus/system/descriptors.the.txt
      Sorting process completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : /Volumes/GitHub/techminer2/techminer2/package_data/thesaurus/system/descriptors.the.txt
    <BLANKLINE>
        MATHEMATICAL_AND_MACHINE_LEARNING_MODELS
          MATHEMATICAL_OR_MACHINE_LEARNING_MODELS
        ELMAN_RECURRENT_NEURAL_NETWORK
          ELMAN_NEURAL_NETWORK; ELMAN_NEURAL_NETWORKS; THE_ELMAN_NEURAL_NETWORK; EL...
        TEMPORAL_FUSION_TRANSFORMER
          TEMPORAL_FUSION_TRANSFORMER_METHODS; TEMPORAL_FUSION_TRANSFORMER_METHOD
        BLACK_SCHOLES_MERTON_MODEL
          BLACK_SCHOLES_MERTON; BLACK_SCHOLES_MERTON_EQUATION; BLACK_SCHOLE_MERTON_...
        ABSTRACTIVE_SUMMARIZATION
          ABSTRACTIVE_TEXT_SUMMARIZATION; ABSTRACTIVE_TEXT_SUMMARIZATION_MODEL
        ARTIFICIAL_NEURAL_NETWORK
          ARTIFICIAL_NEURAL_NETWORK; ARTIFICIAL_NEURAL_NETWORK_MODEL; ARTIFICIAL_NE...
        ECHO_STATE_NEURAL_NETWORK
          ECHO_STATE_NETWORK; ECHO_STATE_NETWORKS; ECHO_STATE_NEURAL_NETWORK; ECHO_...
        ENSEMBLE_MACHINE_LEARNING
          ENSEMBLE_MACHINE_LEARNING_APPROACHES
    <BLANKLINE>
    <BLANKLINE>




"""
from ....user import SortByKeyLength as UserSortByKeyLength


class SortByKeyLength(
    UserSortByKeyLength,
):
    """:meta private:"""

    def run(self):

        self.with_thesaurus_file("system/descriptors.the.txt")
        self.internal__build_system_thesaurus_path()
        self.internal__run()


# =============================================================================
