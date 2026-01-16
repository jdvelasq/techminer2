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


Example:
    >>> import shutil
    >>> shutil.copy("examples/fintech/database.csv.zip", "examples/fintech/data/processed/database.csv.zip")
    'examples/fintech/data/processed/database.csv.zip'

    >>> import shutil
    >>> shutil.copy("examples/fintech/database.csv.zip", "examples/fintech/data/processed/database.csv.zip")
    'examples/fintech/data/processed/database.csv.zip'

    >>> import pandas as pd
    >>> from techminer2.database.operators import TransformOperator
    >>> TransformOperator(
    ...     field="raw_index_keywords",
    ...     other_field="na_field",
    ...     root_directory="examples/fintech/",
    ...     transformation_function=lambda x: pd.NA,
    ... ).run()

    >>> # Query the database to obtain the number of NA values
    >>> from techminer2.database.tools import Query
    >>> query = (
    ...     Query()
    ...     .with_query_expression("SELECT na_field FROM database;")
    ...     .where_root_directory("examples/fintech/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ... )
    >>> df = query.run()
    >>> int(df.na_field.isna().sum())
    50

    >>> # Creates, configures, and runs the operator
    >>> from techminer2.database.operators import FillNAOperator
    >>> fillna_operator = (
    ...     FillNAOperator()
    ...     #
    ...     # FIELDS:
    ...     .with_field("na_field")
    ...     .with_other_field("raw_index_keywords")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("examples/fintech/")
    ... )
    >>> fillna_operator.run()

    >>> # Query the database to test the operator
    >>> from techminer2.database.tools import Query
    >>> query = (
    ...     Query()
    ...     .with_query_expression("SELECT na_field FROM database;")
    ...     .where_root_directory("examples/fintech/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ... )
    >>> df = query.run()
    >>> int(df.na_field.isna().sum())
    31

    >>> # Deletes the field
    >>> from techminer2.database.operators import DeleteOperator
    >>> DeleteOperator(
    ...     field="na_field",
    ...     root_directory="examples/fintech/",
    ... ).run()


"""
from techminer2._internals.mixins import ParamsMixin
from techminer2.database._internals.operators.fillna import internal__fillna
from techminer2.database._internals.protected_fields import PROTECTED_FIELDS


class FillNAOperator(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        if self.params.field in PROTECTED_FIELDS:
            raise ValueError(f"Field `{self.params.field}` is protected")

        internal__fillna(
            fill_field=self.params.field,
            with_field=self.params.other_field,
            #
            # DATABASE PARAMS:
            root_dir=self.params.root_directory,
        )


#
