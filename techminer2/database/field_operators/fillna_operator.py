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
    >>> import pandas as pd
    >>> from techminer2.database.field_operators import (
    ...     DeleteFieldOperator,
    ...     FillNAOperator,
    ...     TransformFieldOperator,
    ... )
    >>> from techminer2.database.tools import Query

    >>> # Copy the field to fill to avoid losing the original data
    >>> TransformFieldOperator(
    ...     field="raw_index_keywords",
    ...     other_field="na_field",
    ...     root_directory="example/",
    ...     transformation_function=lambda x: pd.NA,
    ... ).run()

    >>> # Query the database to obtain the number of NA values
    >>> query = (
    ...     Query()
    ...     .with_query_expression("SELECT na_field FROM database;")
    ...     .where_root_directory_is("example/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ... )
    >>> df = query.run()
    >>> df.na_field.isna().sum()
    np.int64(50)

    >>> # Creates, configures, and runs the operator
    >>> fillna_operator = (
    ...     FillNAOperator()
    ...     #
    ...     # FIELDS:
    ...     .with_field("na_field")
    ...     .with_other_field("raw_index_keywords")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory_is("example/")
    ... )
    >>> fillna_operator.run()

    >>> # Query the database to test the operator
    >>> query = (
    ...     Query()
    ...     .with_query_expression("SELECT na_field FROM database;")
    ...     .where_root_directory_is("example/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ... )
    >>> df = query.run()
    >>> df.na_field.isna().sum()
    np.int64(31)

    >>> # Deletes the field
    >>> DeleteFieldOperator(
    ...     field="na_field",
    ...     root_directory="example/",
    ... ).run()


"""
from ..._internals.mixins import ParamsMixin
from .._internals.protected_fields import PROTECTED_FIELDS
from ..ingest._internals.operators.fillna import internal__fillna


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
