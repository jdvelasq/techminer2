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

>>> from techminer2.database.operations import FillNAOperator
>>> (
...     FillNAOperator()  # doctest: +SKIP 
...     .set_params(
...         fill_field="author_keywords",
...         with_field="index_keywords",
...         #
...         # DATABASE PARAMS:
...         root_dir="example",
...     ).build()
... )

"""
from dataclasses import dataclass

from ..internals.field_operators.internal__fillna import internal__fillna
from .internals.set_params_mixin import SetParamsMixin
from .operators__protected_fields import PROTECTED_FIELDS


@dataclass
class Params:
    """:meta private:"""

    fill_field: str = ""
    with_field: str = ""
    root_dir: str = "./"


class FillNAOperator(
    SetParamsMixin,
):
    """:meta private:"""

    def __init__(self):
        self.params = Params()

    def build(self):

        if self.params.fill_field in PROTECTED_FIELDS:
            raise ValueError(f"Field `{self.params.fill_field}` is protected")

        internal__fillna(
            fill_field=self.params.fill_field,
            with_field=self.params.with_field,
            #
            # DATABASE PARAMS:
            root_dir=self.params.root_dir,
        )
