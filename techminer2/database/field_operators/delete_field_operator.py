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


Example:
    >>> from techminer2.database.field_operators import (
    ...     CopyFieldOperator,
    ...     DeleteFieldOperator,
    ... )
    >>> from techminer2.database.tools import Query

    >>> # Creates, configures, and runs the copy operator
    >>> copy_operator = (
    ...     CopyFieldOperator()
    ...     #
    ...     # FIELDS:
    ...     .with_field("author_keywords")
    ...     .with_other_field("author_keywords_copy")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory_is("example/")
    ... )
    >>> copy_operator.run()

    >>> # Deletes the field
    >>> delete_operator = (
    ...     DeleteFieldOperator()
    ...     .with_field("author_keywords_copy")
    ...     .where_root_directory_is("example/")
    ... )
    >>> delete_operator.run()

    >>> # Query the database to test the operator
    >>> query = (
    ...     Query()
    ...     .with_query_expression("SELECT * FROM database LIMIT 5;")
    ...     .where_root_directory_is("example/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ... )
    >>> df = query.run()
    >>> print("author_keywords_copy" in df.columns)
    False

"""

from ..._internals.mixins import ParamsMixin
from .._internals.protected_fields import PROTECTED_FIELDS
from ..ingest._internals.operators.delete_field import internal__delete_field


class DeleteFieldOperator(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        if self.params.field in PROTECTED_FIELDS:
            raise ValueError(f"Field `{self.params.field}` is protected")

        internal__delete_field(
            field=self.params.field,
            #
            # DATABASE PARAMS:
            root_dir=self.params.root_directory,
        )
