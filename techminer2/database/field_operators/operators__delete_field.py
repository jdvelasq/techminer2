# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-few-public-methods
"""
Delete a Field
===============================================================================

>>> from techminer2.database.operations import DeleteFieldOperator
>>> (
...     DeleteFieldOperator()  # doctest: +SKIP 
...     .set_params(
...         field="author_keywords_copy",
...         #
...         # DATABASE PARAMS:
...         root_dir="example",
...     ).build()
... )

"""

from dataclasses import dataclass

from ..internals.field_operators.internal__delete_field import internal__delete_field
from .internals.set_params_mixin import SetParamsMixin
from .operators__protected_fields import PROTECTED_FIELDS


@dataclass
class Params:
    """:meta private:"""

    field: str = ""
    root_dir: str = "./"


class DeleteFieldOperator(
    SetParamsMixin,
):
    """:meta private:"""

    def __init__(self):
        self.params = Params()

    def build(self):

        if self.params.field in PROTECTED_FIELDS:
            raise ValueError(f"Field `{self.params.field}` is protected")

        internal__delete_field(
            field=self.params.field,
            #
            # DATABASE PARAMS:
            root_dir=self.params.root_dir,
        )
