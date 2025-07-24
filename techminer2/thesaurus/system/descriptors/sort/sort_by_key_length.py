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
        ABSTRACTIVE_SUMMARIZATION
          ABSTRACTIVE_TEXT_SUMMARIZATION; ABSTRACTIVE_TEXT_SUMMARIZATION_MODEL
        ARTIFICIAL_NEURAL_NETWORK
          ARTIFICIAL_NEURAL_NETWORK; ARTIFICIAL_NEURAL_NETWORKS; ARTIFICIAL_NEURONA...
        ARTIFICIAL_INTELLIGENCE
          ARTIFICIAL_INTELLIGENCE_APPROACH; ARTIFICIAL_INTELLIGENCE_MODEL; ARTIFICI...
        K_NEAREST_NEIGHBORS
          KNN_METHOD
        MACHINE_LEARNING
          ACTIVE_MACHINE_LEARNING; APPLIED_MACHINE_LEARNING; MACHINE_LEARNING_ALGOR...
        *BIBLIOMETRICS*
          BIBLIOMETRIC; BIBLIOMETRICS
        *ERROR_METRICS*
          ABSOLUTE_AVERAGE_DEVIATION; ABSOLUTE_AVERAGE_DEVIATIONS; ABSOLUTE_ERROR; ...
        CO_2_EMISSIONS
          CABBON_EMISSION; CABBON_EMISSIONS; CO2_EMISSION; CO2_EMISSIONS; CO_2_EMIS...
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
