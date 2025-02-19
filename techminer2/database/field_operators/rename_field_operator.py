# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Rename a Field
===============================================================================

>>> from techminer2.database.field_operators import RenameFieldOperator
>>> (
...     RenameFieldOperator()  # doctest: +SKIP 
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
from ..ingest._internals.operators.rename_field import internal__rename_field
from .protected_fields import PROTECTED_FIELDS


class RenameFieldOperator(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):

        if self.params.dest_field in PROTECTED_FIELDS:
            raise ValueError(f"Field `{self.params.dest_field}` is protected")

        internal__rename_field(
            source=self.params.field,
            dest=self.params.dest_field,
            #
            # DATABASE PARAMS:
            root_dir=self.params.root_dir,
        )
