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
    >>> import shutil
    >>> shutil.copy("examples/fintech/database.csv.zip", "examples/fintech/data/processed/database.csv.zip")
    'examples/fintech/data/processed/database.csv.zip'

    >>> # Creates, configures, and runs the operator
    >>> from techminer2.database.operators import CopyOperator
    >>> (
    ...     CopyOperator()
    ...     #
    ...     # FIELDS:
    ...     .with_field("author_keywords")
    ...     .with_other_field("author_keywords_copy")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("examples/fintech/")
    ...     #
    ...     .run()
    ... )

    >>> # Deletes the field
    >>> from techminer2.database.operators import DeleteOperator
    >>> (
    ...     DeleteOperator()
    ...     .with_field("author_keywords_copy")
    ...     .where_root_directory("examples/fintech/")
    ...     .run()
    ... )

    >>> # Query the database to test the operator
    >>> from techminer2.database.tools import Query
    >>> df = (
    ...     Query()
    ...     .with_query_expression("SELECT * FROM database LIMIT 5;")
    ...     .where_root_directory("examples/fintech/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .run()
    ... )
    >>> print("author_keywords_copy" in df.columns)
    False

"""
from techminer2._internals.mixins import ParamsMixin
from techminer2.database._internals.protected_fields import PROTECTED_FIELDS
from techminer2.scopus._internals.operators.delete_field import internal__delete_field


class DeleteOperator(
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


#
