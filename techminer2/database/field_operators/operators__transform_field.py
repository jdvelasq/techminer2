# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-few-public-methods
"""
Process a Field
===============================================================================

>>> from techminer2.database.field_operators import TransformFieldOperator
>>> (
...     TransformFieldOperator()  # doctest: +SKIP 
...     .with_source_field("author_keywords")
...     .as_field("author_keywords_copy")
...     .transform_with(lambda x: x.str.lower())
...     .where_directory_is("example/")
...     .build()
... )

"""
from ...internals.mixins import InputFunctionsMixin
from ..internals.field_operators.internal__transform_field import (
    internal__transform_field,
)
from .operators__protected_fields import PROTECTED_FIELDS


class TransformFieldOperator(
    InputFunctionsMixin,
):
    """:meta private:"""

    def build(self):

        if self.params.dest_field in PROTECTED_FIELDS:
            raise ValueError(f"Field `{self.params.dest_field}` is protected")

        internal__transform_field(
            source=self.params.source_field,
            dest=self.params.dest_field,
            func=self.params.func,
            #
            # DATABASE PARAMS:
            root_dir=self.params.root_dir,
        )
