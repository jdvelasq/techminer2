# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Rename a Field
===============================================================================


Example:
    >>> # Creates, configures, and runs the operator to copy the field
    >>> from techminer2.database.field_operators import CopyFieldOperator
    >>> (
    ...     CopyFieldOperator()
    ...     #
    ...     # FIELDS:
    ...     .with_field("author_keywords")
    ...     .with_other_field("author_keywords_copy")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory_is("examples/fintech/")
    ...     #
    ...     .run()
    ... )

    >>> # Creates, configures, and runs the operator to rename the field
    >>> from techminer2.database.field_operators import RenameFieldOperator
    >>> (
    ...     RenameFieldOperator()
    ...     #
    ...     # FIELDS:
    ...     .with_field("author_keywords_copy")
    ...     .with_other_field("author_keywords_renamed")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory_is("examples/fintech/")
    ...     .run()
    ... )


    >>> # Query the database to test the operator
    >>> from techminer2.tools import Query
    >>> (
    ...     Query()
    ...     .with_query_expression("SELECT author_keywords_renamed FROM database LIMIT 5;")
    ...     .where_root_directory_is("examples/fintech/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ...     .run()
    ... )
                                 author_keywords_renamed
    0  ELABORATION_LIKELIHOOD_MODEL; FINTECH; K_PAY; ...
    1  ACTOR_NETWORK_THEORY; CHINESE_TELECOM; FINTECH...
    2  FINANCIAL_INCLUSION; FINANCIAL_SCENARIZATION; ...
    3                 BANKING_INNOVATIONS; FINTECH; RISK
    4  BEHAVIOURAL_ECONOMICS; DIGITAL_TECHNOLOGIES; F...

    >>> # Deletes the field
    >>> from techminer2.database.field_operators import DeleteFieldOperator
    >>> DeleteFieldOperator(
    ...     field="author_keywords_renamed",
    ...     root_directory="examples/fintech/",
    ... ).run()


"""
from techminer2._internals.mixins import ParamsMixin

from .._internals.protected_fields import PROTECTED_FIELDS
from ..ingest._internals.operators.rename_field import internal__rename_field


class RenameFieldOperator(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        if self.params.other_field in PROTECTED_FIELDS:
            raise ValueError(f"Field `{self.params.other_field}` is protected")

        internal__rename_field(
            source=self.params.field,
            dest=self.params.other_field,
            #
            # DATABASE PARAMS:
            root_dir=self.params.root_directory,
        )
