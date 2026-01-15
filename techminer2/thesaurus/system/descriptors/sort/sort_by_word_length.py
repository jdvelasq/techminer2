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
    >>> from techminer2.thesaurus.system.descriptors import SortByWordLength

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Configure and run the sorter
    >>> SortByWordLength().run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)  # doctest: +SKIP
    Sorting thesaurus by word length...
      File : /Volumes/GitHub/techminer2/techminer2/_internals/package_data/thesaurus/system/descriptors.the.txt
      Sorting process completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : /Volumes/GitHub/techminer2/techminer2/_internals/package_data/thesaurus/system/descriptors.the.txt
    <BLANKLINE>
        BIBLIOMETRICS
          BIBLIOMETRIC
        ORGANIZATION
          BUSINESS; BUSINESSES; COMPANIES; COMPANY; ENTERPRISE; ENTERPRISES; FIRM; ...
        APPLICATION
          APPLICATIONS
        MULTI_TRANSFORMER
          MULTI_TRANSFORMERS
        SYNTHESIZER_TRANSFORMER
          SYNTHESIZER_TRANSFORMERS
        TEMPORAL_FUSION_TRANSFORMER
          TEMPORAL_FUSION_TRANSFORMERS
        TRANSFORMER_NETWORK
          TRANSFORMER_NETWORKS
        ARTIFICIAL_NEURAL_NETWORK
          ARTIFICIAL_NEURAL_NETWORKS; ARTIFICIAL_NEURAL_NETWORK_MODEL; ARTIFICIAL_N...
    <BLANKLINE>
    <BLANKLINE>




"""
from techminer2.thesaurus.user import SortByWordLength as UserSortByWordLength


class SortByWordLength(
    UserSortByWordLength,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def run(self):

        self.with_thesaurus_file("system/descriptors.the.txt")
        self.internal__build_system_thesaurus_path()
        self.internal__run()


# =============================================================================
