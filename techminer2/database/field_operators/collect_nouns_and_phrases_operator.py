# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Collect Nouns and Phrases
===============================================================================

>>> from techminer2.database.field_operators import CollectNounAndPhrasesOperator
>>> (
...     CollectNounAndPhrasesOperator()  # doctest: +SKIP 
....    #
...     .with_field("author_keywords")
...     .with_target_field("author_keywords_copy")
....    #
...     .where_directory_is("example/")
...     .build()
... )

"""
from ...internals.mixins import InputFunctionsMixin
from ..ingest.internals.operators.internal__collect_nouns_and_phrases import (
    internal__collect_nouns_and_phrases,
)
from .protected_fields import PROTECTED_FIELDS


class CollectNounAndPhrasesOperator(
    InputFunctionsMixin,
):
    """:meta private:"""

    def build(self):

        if self.params.dest_field in PROTECTED_FIELDS:
            raise ValueError(f"Field `{self.params.dest_field}` is protected")

        internal__collect_nouns_and_phrases(
            source=self.params.field,
            dest=self.params.dest_field,
            #
            # DATABASE PARAMS:
            root_dir=self.params.root_dir,
        )
