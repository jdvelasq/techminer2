# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Collect Descriptors
===============================================================================


Example:
    >>> from techminer2.database.tools import CollectDescriptors
    >>> CollectDescriptors(root_directory="../tm2_health_analytics/").run()

    ## >>> CollectDescriptors(root_directory="example/").run()



"""
import sys

from ..._internals.mixins import ParamsMixin
from ...database.ingest._internals.preprocessors import (  # type: ignore
    internal__preprocess_abbreviations,
    internal__preprocess_descriptors,
    internal__preprocess_raw_abstract_nouns_and_phrases,
    internal__preprocess_raw_descriptors,
    internal__preprocess_raw_document_title_nouns_and_phrases,
    internal__preprocess_raw_noun_and_phrases,
)


class CollectDescriptors(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        from ...thesaurus.descriptors import CreateThesaurus

        sys.stderr.write("\nINFO  Collecting Descriptors\n")
        sys.stderr.flush()

        root_directory = self.params.root_directory
        internal__preprocess_raw_abstract_nouns_and_phrases(root_directory)
        internal__preprocess_raw_document_title_nouns_and_phrases(root_directory)
        internal__preprocess_raw_noun_and_phrases(root_directory)
        internal__preprocess_raw_descriptors(root_directory)
        internal__preprocess_descriptors(root_directory)
        internal__preprocess_abbreviations(root_directory)

        CreateThesaurus().update(**self.params.__dict__).run()
