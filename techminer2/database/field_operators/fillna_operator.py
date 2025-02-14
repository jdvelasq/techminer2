# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-few-public-methods
"""
Fill NA
===============================================================================

>>> from techminer2.database.field_operators import FillNAOperator
>>> (
...     FillNAOperator()  # doctest: +SKIP 
...     #
...     # FIELDS:
...     .with_field("author_keywords")
...     .with_other_field("index_keywords")
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     #
...     .build()
... )

"""
from ...internals.mixins import ParamsMixin
from ..ingest.internals.operators.internal__fillna import internal__fillna
from .protected_fields import PROTECTED_FIELDS


class FillNAOperator(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):

        if self.params.other_field in PROTECTED_FIELDS:
            raise ValueError(f"Field `{self.params.other_field}` is protected")

        internal__fillna(
            fill_field=self.params.field,
            with_field=self.params.other_field,
            #
            # DATABASE PARAMS:
            root_dir=self.params.root_dir,
        )
