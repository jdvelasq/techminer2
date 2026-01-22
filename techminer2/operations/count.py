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
    >>> import shutil
    >>> shutil.copy("examples/fintech/database.csv.zip", "examples/fintech/data/processed/database.csv.zip")
    'examples/fintech/data/processed/database.csv.zip'

    >>> # Creates, configure, and run the operator
    >>> from techminer2.database.operators import CountOperator
    >>> (
    ...     CountOperator()
    ...     #
    ...     # FIELDS:
    ...     .with_field("authors")
    ...     .with_other_field("num_authors_test")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("examples/fintech/")
    ...     #
    ...     .run()
    ... )

    >>> # Query the database to test the operator
    >>> from techminer2.io import Query
    >>> (
    ...     Query()
    ...     .with_query_expression("SELECT authors, num_authors_test FROM database LIMIT 5;")
    ...     .where_root_directory("examples/fintech/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .run()
    ... )
                                    authors  num_authors_test
    0  Kim Y.; Choi J.; Park Y.-J.; Yeon J.                 4
    1                   Shim Y.; Shin D.-H.                 2
    2                               Chen L.                 1
    3              Romanova I.; Kudinska M.                 2
    4                   Gabor D.; Brooks S.                 2



    >>> # Deletes the field
    >>> from techminer2.database.operators import DeleteOperator
    >>> DeleteOperator(
    ...     field="num_authors_test",
    ...     root_directory="examples/fintech/",
    ... ).run()

"""
from techminer2._internals.mixins import ParamsMixin
from techminer2.io._internals.extractors.protected_fields import PROTECTED_FIELDS
from techminer2.io._internals.operators.count_items import count_items


class CountOperator(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        if self.params.other_field in PROTECTED_FIELDS:
            raise ValueError(f"Field `{self.params.other_field}` is protected")

        count_items(
            source=self.params.field,
            target=self.params.other_field,
            #
            # DATABASE PARAMS:
            root_directory=self.params.root_directory,
        )


#
