# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# mypy: ignore-errors
"""
Apply Thesaurus 
===============================================================================


>>> from techminer2.thesaurus.descriptors import ApplyThesaurus
>>> (
...     ApplyThesaurus()
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     #
...     .build()
... )
--INFO-- Applying `descriptors.the.txt` thesaurus to author/index keywords and abstract/title words

"""

from ...internals.mixins import ParamsMixin
from ..user.apply_thesaurus import ApplyThesaurus as ApplyUserThesaurus


class ApplyThesaurus(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):

        for raw_column, column in [
            (
                "raw_author_keywords",
                "author_keywords",
            ),
            (
                "raw_index_keywords",
                "index_keywords",
            ),
            (
                "raw_keywords",
                "keywords",
            ),
            (
                "raw_document_title_nouns_and_phrases",
                "document_title_nouns_and_phrases",
            ),
            (
                "raw_abstract_nouns_and_phrases",
                "abstract_nouns_and_phrases",
            ),
            (
                "raw_nouns_and_phrases",
                "nouns_and_phrases",
            ),
            (
                "raw_descriptors",
                "descriptors",
            ),
        ]:

            (
                ApplyUserThesaurus()
                .with_thesaurus_file("descriptors.the.txt")
                .with_field(raw_column)
                .with_other_field(column)
                .where_directory_is(self.params.root_dir)
                .build()
            )
