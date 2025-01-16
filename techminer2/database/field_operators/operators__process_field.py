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

>>> from techminer2.database.operations import ProcessFieldOperator
>>> (
...     ProcessFieldOperator()  # doctest: +SKIP 
...     .set_params(
...         source="author_keywords",
...         dest="author_keywords_copy",
...         func=lambda x: x.str.lower(),
...         #
...         # DATABASE PARAMS:
...         root_dir="example",
...     ).build()
... )

"""
from dataclasses import dataclass
from typing import Optional

from ..internals.field_operators.internal__process_field import internal__process_field
from .internals.set_params_mixin import SetParamsMixin
from .operators__protected_fields import PROTECTED_FIELDS


@dataclass
class Params:
    """:meta private:"""

    source: Optional[str] = None
    dest: Optional[str] = None
    func = None
    root_dir: str = "./"


class ProcessFieldOperator(
    SetParamsMixin,
):
    """:meta private:"""

    def __init__(self):
        self.params = Params()

    def build(self):

        if self.params.dest in PROTECTED_FIELDS:
            raise ValueError(f"Field `{self.params.dest}` is protected")

        internal__process_field(
            source=self.params.source,
            dest=self.params.dest,
            func=self.params.func,
            #
            # DATABASE PARAMS:
            root_dir=self.params.root_dir,
        )
