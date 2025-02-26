# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Merge Fields
===============================================================================

>>> from techminer2.database.field_operators import MergeFieldsOperator
>>> (
...     MergeFieldsOperator()  # doctest: +SKIP
...     #
...     # FIELDS:
...     .with_field["author_keywords", "index_keywords"])
...     .with_other_field("merged_keywords")
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     #
...     .build()
... )

"""
from ..._internals.mixins import ParamsMixin
from ..ingest._internals.operators.merge_fields import internal__merge_fields
from .protected_fields import PROTECTED_FIELDS


class MergeFieldsOperator(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):

        if self.params.dest_field in PROTECTED_FIELDS:
            raise ValueError(f"Field `{self.params.dest_field}` is protected")

        internal__merge_fields(
            source=self.params.field,
            dest=self.params.dest_field,
            #
            # DATABASE PARAMS:
            root_dir=self.params.root_directory,
        )
