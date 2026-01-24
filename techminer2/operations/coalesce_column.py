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
    >>> from techminer2.io import Query
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
    >>> from techminer2.io import Query
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
from techminer2.io._internals.operations.coalesce_column import coalesce_column
from techminer2.text.extract._helpers.protected_fields import PROTECTED_FIELDS


class CoalesceColumn(
    ParamsMixin,
):

    def run(self):

        if self.params.source_field == self.params.target_field:
            raise ValueError(
                f"Source and target fields must differ (got `{self.params.source_field}`)"
            )

        if self.params.target_field in PROTECTED_FIELDS:
            raise ValueError(
                f"Cannot fill a protected field `{self.params.target_field}`"
            )

        coalesce_column(
            source=self.params.source_field,
            target=self.params.target_field,
            root_directory=self.params.root_directory,
        )


#
