# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Clean text
===============================================================================

>>> from techminer2.database.field_operators import CleanTextOperator
>>> (
...     CleanTextOperator()  # doctest: +SKIP 
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
from ...internals.mixins import ParamsMixin
from ..ingest.internals.operators.clean_text import internal__clean_text
from .protected_fields import PROTECTED_FIELDS


class CleanTextOperator(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):

        if self.params.other_field in PROTECTED_FIELDS:
            raise ValueError(f"Field `{self.params.other_field}` is protected")

        internal__clean_text(
            source=self.params.field,
            dest=self.params.other_field,
            #
            # DATABASE PARAMS:
            root_dir=self.params.root_dir,
        )
