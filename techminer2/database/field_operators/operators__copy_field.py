# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Copy a Field
===============================================================================

>>> from techminer2.database.field_operators import CopyFieldOperator
>>> (
...     CopyFieldOperator()  # doctest: +SKIP
...     .select_field("author_keywords")
...     .as_field("author_keywords_copy")
...     .where_directory_is("example/")
...     .build()
... )

"""
from ...internals.mixins import InputFunctionsMixin
from ..ingest.internals.operators.internal__copy_field import internal__copy_field
from .operators__protected_fields import PROTECTED_FIELDS


class CopyFieldOperator(
    InputFunctionsMixin,
):
    """:meta private:"""

    def build(self):

        if self.params.dest_field in PROTECTED_FIELDS:
            raise ValueError(f"Field `{self.params.dest_field}` is protected")

        internal__copy_field(
            source=self.params.source_field,
            dest=self.params.dest_field,
            #
            # DATABASE PARAMS:
            root_dir=self.params.root_dir,
        )
