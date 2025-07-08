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


Example:
    >>> from techminer2.database.field_operators import (
    ...     CountTermsPerRecordOperator,
    ...     DeleteFieldOperator,
    ... )
    >>> from techminer2.database.tools import Query

    >>> # Creates, configure, and run the operator
    >>> counter = (
    ...     CountTermsPerRecordOperator()
    ...     #
    ...     # FIELDS:
    ...     .with_field("authors")
    ...     .with_other_field("num_authors_test")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory_is("example/")
    ... )
    >>> counter.run()

    >>> # Query the database to test the operator
    >>> query = (
    ...     Query()
    ...     .with_query_expression("SELECT authors, num_authors_test FROM database LIMIT 5;")
    ...     .where_root_directory_is("example/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ... )
    >>> df = query.run()
    >>> df
                                    authors  num_authors_test
    0  Kim Y.; Choi J.; Park Y.-J.; Yeon J.                 4
    1                   Shim Y.; Shin D.-H.                 2
    2                               Chen L.                 1
    3              Romanova I.; Kudinska M.                 2
    4                   Gabor D.; Brooks S.                 2



    >>> # Deletes the field
    >>> DeleteFieldOperator(
    ...     field="num_authors_test",
    ...     root_directory="example/",
    ... ).run()

"""
from ..._internals.mixins import ParamsMixin
from .._internals.protected_fields import PROTECTED_FIELDS
from ..ingest._internals.operators.count_terms_per_record import (
    internal__count_terms_per_record,
)


class CountTermsPerRecordOperator(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        if self.params.other_field in PROTECTED_FIELDS:
            raise ValueError(f"Field `{self.params.other_field}` is protected")

        internal__count_terms_per_record(
            source=self.params.field,
            dest=self.params.other_field,
            #
            # DATABASE PARAMS:
            root_dir=self.params.root_directory,
        )
