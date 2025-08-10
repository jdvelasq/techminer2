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
    >>> from techminer2.database.operators import (
    ...     CountOperator,
    ...     DeleteOperator,
    ... )
    >>> from techminer2.database.tools import Query

    >>> # Creates, configure, and run the operator
    >>> counter = (
    ...     CountOperator()
    ...     #
    ...     # FIELDS:
    ...     .with_field("authors")
    ...     .with_other_field("num_authors_test")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory_is("examples/fintech/")
    ... )
    >>> counter.run()

    >>> # Query the database to test the operator
    >>> query = (
    ...     Query()
    ...     .with_query_expression("SELECT authors, num_authors_test FROM database LIMIT 5;")
    ...     .where_root_directory_is("examples/fintech/")
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
    >>> DeleteOperator(
    ...     field="num_authors_test",
    ...     root_directory="examples/fintech/",
    ... ).run()

"""
from techminer2._internals.mixins import ParamsMixin
from techminer2.database._internals.operators.count import internal__count
from techminer2.database._internals.protected_fields import PROTECTED_FIELDS


class CountOperator(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        if self.params.other_field in PROTECTED_FIELDS:
            raise ValueError(f"Field `{self.params.other_field}` is protected")

        internal__count(
            source=self.params.field,
            dest=self.params.other_field,
            #
            # DATABASE PARAMS:
            root_dir=self.params.root_directory,
        )


#
