# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Count Terms per Record
===============================================================================

>>> from techminer2.database.field_operators import CountTermsPerRecordOperator
>>> (
...     CountTermsPerRecordOperator()
...     #
...     .with_field("authors")
...     .with_target_field("test_num_authors")
...     #
...     .where_directory_is("example/")
...     #
...     .build()
... )

# >>> from techminer2.database.tools import Query
# >>> (
# ...     Query()
# ...     .set_analysis_params(
# ...         expr="SELECT authors, test_num_authors FROM database LIMIT 5;",
# ...     ).set_database_params(
# ...         root_dir="example/",
# ...         database="main",
# ...         year_filter=(None, None),
# ...         cited_by_filter=(None, None),
# ...     ).build()
# ... )
                                authors  test_num_authors
0  Kim Y.; Choi J.; Park Y.-J.; Yeon J.                 4
1                   Shim Y.; Shin D.-H.                 2
2                             Chen L./1                 1
3              Romanova I.; Kudinska M.                 2
4                   Gabor D.; Brooks S.                 2

"""
from ...internals.mixins import InputFunctionsMixin
from ..ingest.internals.operators.internal__count_terms_per_record import (
    internal__count_terms_per_record,
)
from .protected_fields import PROTECTED_FIELDS


class CountTermsPerRecordOperator(
    InputFunctionsMixin,
):
    """:meta private:"""

    def build(self):

        if self.params.other_field in PROTECTED_FIELDS:
            raise ValueError(f"Field `{self.params.other_field}` is protected")

        internal__count_terms_per_record(
            source=self.params.field,
            dest=self.params.other_field,
            #
            # DATABASE PARAMS:
            root_dir=self.params.root_dir,
        )
