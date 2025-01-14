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

>>> from techminer2.database.operations import CollectNounAndPhrasesOperator
>>> (
...     CollectNounAndPhrasesOperator()  # doctest: +SKIP 
...     .set_params(
...         source="author_keywords",
...         dest="author_keywords_copy",
...         root_dir="example",
...     ).build()
... )

"""
from ..internals.field_operations.internal__collect_nouns_and_phrases import (
    internal__collect_nouns_and_phrases,
)
from .internals.set_params_mixin import SetParamsMixin
from .internals.source_dest_params import SourceDestParams
from .operations__protected_fields import PROTECTED_FIELDS


class CollectNounAndPhrasesOperator(
    SetParamsMixin,
):
    """:meta private:"""

    def __init__(self):
        self.params = SourceDestParams()

    def build(self):

        if self.params.dest in PROTECTED_FIELDS:
            raise ValueError(f"Field `{self.params.dest}` is protected")

        internal__collect_nouns_and_phrases(
            source=self.params.source,
            dest=self.params.dest,
            #
            # DATABASE PARAMS:
            root_dir=self.params.root_dir,
        )
