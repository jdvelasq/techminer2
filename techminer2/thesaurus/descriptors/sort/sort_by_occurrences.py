# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort by Occurrences
===============================================================================


Example:
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.descriptors import CreateThesaurus, SortByOccurrences

    >>> # Redirecting stderr to avoid messages
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Create the thesaurus
    >>> CreateThesaurus(root_directory="example/", quiet=True).run()

    ## >>> # Configure and run the sorter
    ## >>> sorter = (
    ## ...     SortByOccurrences()
    ## ...     .where_root_directory_is("example/")
    ## ... )
    ## >>> sorter.run()

    >>> # Configure and run the sorter
    >>> sorter = (
    ...     SortByOccurrences()
    ...     .where_root_directory_is("../tm2_genai_en_analytics/")
    ... )
    >>> sorter.run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = StringIO()
    >>> print(output)
    Reducing thesaurus keys
      File : ../tm2_genai_en_analytics/thesaurus/descriptors.the.txt
      Keys reduced from 8383 to 8383
      Keys reduction completed successfully
    <BLANKLINE>
    Sorting thesaurus by occurrences
      File : ../tm2_genai_en_analytics/thesaurus/descriptors.the.txt
      Thesaurus sorting completed successfully
    <BLANKLINE>
    Printing thesaurus header
      File : ../tm2_genai_en_analytics/thesaurus/descriptors.the.txt
    <BLANKLINE>
        LARGE_LANGUAGE_MODELS
          ADVANCED_LARGE_LANGUAGE_MODELS; ADVANCED_LLMS; ALL_LLMS; AN_ADVANCED_LANG...
        NATURAL_LANGUAGE_PROCESSING
          ADVANCED_NATURAL_LANGUAGE_PROCESSING_MODELS; ADVANCED_NATURAL_LANGUAGE_PR...
        SENTIMENT_ANALYSIS
          ABSA; ACCURATE_SENTIMENT_ANALYSIS; ADVANCED_SENTIMENT_ANALYSIS; ASPECT_BA...
        MODELS
          ADVANCED_MODELS; ALL_MODELS; ALTERNATIVE_MODELS; A_HYBRID_MODEL; A_MODEL;...
        GENERATIVE_ADVERSARIAL_NETWORKS
          ADVANCED_GENERATIVE_ADVERSARIAL_NETWORKS; ALL_THE_PROPOSED_GAN_MODELS; AN...
        GENERATIVE_ARTIFICIAL_INTELLIGENCE
          ANALYZE_GENERATIVE_ARTIFICIAL_INTELLIGENCE; A_GAI; GAI; GAI_DIFFERS; GENA...
        ARTIFICIAL_INTELLIGENCE
          ADVANCED_AI; ADVANCED_AI_TECHNIQUE; ADVANCED_AI_TECHNIQUES; ADVANCED_ARTI...
        DATA
          ADDITIONAL_DATA; ADDRESS_DATA; ALL_THE_DATA; ANALYSE_DATA; ANALYZE_THESE_...
    <BLANKLINE>
    <BLANKLINE>


"""
from ...._internals.mixins import ParamsMixin
from ...user import SortByOccurrences as UserSortByOccurrences


class SortByOccurrences(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        return (
            UserSortByOccurrences()
            .update(**self.params.__dict__)
            .with_thesaurus_file("descriptors.the.txt")
            .with_field("raw_descriptors")
            .run()
        )


def sort_by_occurrences():
    SortByOccurrences().where_root_directory_is("../").run()


# =============================================================================
