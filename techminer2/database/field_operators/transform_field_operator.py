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
...     #
...     # FIELDS:
...     .with_field("author_keywords")
...     .with_other_field("author_keywords_copy")
...     #
...     # TRANSFORMATION:
...     .with_transformation(lambda x: x.str.lower())
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     #
...     .build()
... )

"""
from ...internals.mixins import InputFunctionsMixin
from ..ingest.internals.operators.internal__transform_field import (
    internal__transform_field,
)
from .protected_fields import PROTECTED_FIELDS


class TransformFieldOperator(
    InputFunctionsMixin,
):
    """:meta private:"""

    def build(self):

        if self.params.other_field in PROTECTED_FIELDS:
            raise ValueError(f"Field `{self.params.other_field}` is protected")

        internal__transform_field(
            #
            # FIELD:
            field=self.params.field,
            other_field=self.params.other_field,
            function=self.params.function,
            #
            # DATABASE:
            root_dir=self.params.root_dir,
        )
