# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Highlight Nouns and Noun Phrases
===============================================================================

>>> from techminer2.database.field_operators import HighlightNounAndPhrasesOperator
>>> (
...     HighlightNounAndPhrasesOperator()  # doctest: +SKIP 
...     #
...     # FIELDS:
...     .with_field("author_keywords")
...     .with_other_field("author_keywords_copy")
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     #
...     .build()
... )


"""
from ..._internals.mixins import ParamsMixin
from ..ingest._internals.operators.highlight_nouns_and_phrases import (
    internal__highlight_nouns_and_phrases,
)
from .protected_fields import PROTECTED_FIELDS


class HighlightNounAndPhrasesOperator(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):

        if self.params.other_field in PROTECTED_FIELDS:
            raise ValueError(f"Field `{self.params.other_field}` is protected")

        internal__highlight_nouns_and_phrases(
            source=self.params.field,
            dest=self.params.other_field,
            #
            # DATABASE PARAMS:
            root_dir=self.params.root_dir,
        )
