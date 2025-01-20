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

>>> from techminer2.database.operations import HighlightNounAndPhrasesOperator
>>> (
...     HighlightNounAndPhrasesOperator()  # doctest: +SKIP 
...     .for_fields(
...         with_name="author_keywords",
...         to_name="author_keywords_copy",
...     ).for_data(
...         in_root_dir="example",
...     ).build()
... )


"""
from ...internals.set_params_mixin.set_params_mixin import SetParamsMixin
from ...internals.set_params_mixin.set_source_dest_params import SourceDestParams
from ..internals.field_operators.internal__highlight_nouns_and_phrases import (
    internal__highlight_nouns_and_phrases,
)
from .operators__protected_fields import PROTECTED_FIELDS


class HighlightNounAndPhrasesOperator(
    SetParamsMixin,
):
    """:meta private:"""

    def __init__(self):
        self.params = SourceDestParams()

    def build(self):

        if self.params.dest in PROTECTED_FIELDS:
            raise ValueError(f"Field `{self.params.dest}` is protected")

        internal__highlight_nouns_and_phrases(
            source=self.params.source,
            dest=self.params.dest,
            #
            # DATABASE PARAMS:
            root_dir=self.params.root_dir,
        )
