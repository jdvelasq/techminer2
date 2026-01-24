# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Rename Column
===============================================================================


Example:
    >>> import shutil
    >>> shutil.copy("examples/fintech/database.csv.zip", "examples/fintech/data/processed/database.csv.zip")
    'examples/fintech/data/processed/database.csv.zip'

    >>> # Creates, configures, and runs the operator to copy the field
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

    >>> # Creates, configures, and runs the operator to rename the field
    >>> from techminer2.database.operators import RenameOperator
    >>> (
    ...     RenameOperator()
    ...     #
    ...     # FIELDS:
    ...     .with_field("author_keywords_copy")
    ...     .with_other_field("author_keywords_renamed")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("examples/fintech/")
    ...     .run()
    ... )


    >>> # Query the database to test the operator
    >>> from techminer2.io import Query
    >>> (
    ...     Query()
    ...     .with_query_expression("SELECT author_keywords_renamed FROM database LIMIT 5;")
    ...     .where_root_directory("examples/fintech/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .run()
    ... )
                                 author_keywords_renamed
    0  ELABORATION_LIKELIHOOD_MODEL; FINTECH; K_PAY; ...
    1  ACTOR_NETWORK_THEORY; CHINESE_TELECOM; FINTECH...
    2  FINANCIAL_INCLUSION; FINANCIAL_SCENARIZATION; ...
    3                 BANKING_INNOVATIONS; FINTECH; RISK
    4  BEHAVIOURAL_ECONOMICS; DIGITAL_TECHNOLOGIES; F...

    >>> # Deletes the field
    >>> from techminer2.database.operators import DeleteOperator
    >>> DeleteOperator(
    ...     field="author_keywords_renamed",
    ...     root_directory="examples/fintech/",
    ... ).run()


"""
from techminer2._internals.mixins import ParamsMixin
from techminer2.io._internals.operations.rename_column import rename_column
from techminer2.text.extract._helpers.protected_fields import PROTECTED_FIELDS


class RenameColumn(
    ParamsMixin,
):

    def run(self) -> int:

        if self.params.source_field == self.params.target_field:
            raise ValueError(
                f"Source and target fields must differ (got `{self.params.source_field}`)"
            )

        if self.params.target_field in PROTECTED_FIELDS:
            raise ValueError(
                f"Cannot rename a protected field `{self.params.target_field}`"
            )

        return rename_column(
            source=self.params.source_field,
            target=self.params.target_field,
            root_directory=self.params.root_directory,
        )
