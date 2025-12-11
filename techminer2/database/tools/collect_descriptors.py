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
# >>> CollectDescriptors(root_directory="examples/fintech/").run()

Example:
    >>> from techminer2.database.tools import CollectDescriptors
    >>> CollectDescriptors(root_directory="../tm2_economics_of_wind_energy/").run()





"""
import sys

from techminer2._internals.mixins import ParamsMixin
from techminer2.database._internals.preprocessors import (
    internal__preprocess_abstract,
    internal__preprocess_acronyms,
    internal__preprocess_descriptors,
    internal__preprocess_document_title,
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

        from techminer2.thesaurus.descriptors import InitializeThesaurus

        sys.stderr.write("\nINFO  Collecting Descriptors\n")
        sys.stderr.flush()

        root_directory = self.params.root_directory

        internal__preprocess_abstract(root_directory)
        internal__preprocess_document_title(root_directory)
        internal__preprocess_raw_abstract_nouns_and_phrases(root_directory)
        internal__preprocess_raw_document_title_nouns_and_phrases(root_directory)
        internal__preprocess_raw_noun_and_phrases(root_directory)
        internal__preprocess_raw_descriptors(root_directory)
        internal__preprocess_descriptors(root_directory)
        internal__preprocess_acronyms(root_directory)

        InitializeThesaurus().update(**self.params.__dict__).run()
