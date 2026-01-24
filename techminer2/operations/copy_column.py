"""
Copy Column
===============================================================================


Smoke Test:
    >>> import shutil
    >>> shutil.copy("examples/fintech/database.csv.zip", "examples/fintech/data/processed/database.csv.zip")
    'examples/fintech/data/processed/database.csv.zip'


    >>> from techminer2.operations import CopyColumn
    >>> (
    ...     CopyColumn()
    ...     .with_source_field("author_keywords")
    ...     .with_target_field("author_keywords_copy")
    ...     .where_root_directory("examples/fintech/")
    ...     .run()
    ... )


    >>> # Query the database to test the operator
    >>> from techminer2.io import Query
    >>> (
    ...     Query()
    ...     .with_query_expression("SELECT author_keywords_copy FROM database LIMIT 5;")
    ...     .where_root_directory("examples/fintech/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     #
    ...     .run()
    ... )
                                    author_keywords_copy
    0  ELABORATION_LIKELIHOOD_MODEL; FINTECH; K_PAY; ...
    1  ACTOR_NETWORK_THEORY; CHINESE_TELECOM; FINTECH...
    2  FINANCIAL_INCLUSION; FINANCIAL_SCENARIZATION; ...
    3                 BANKING_INNOVATIONS; FINTECH; RISK
    4  BEHAVIOURAL_ECONOMICS; DIGITAL_TECHNOLOGIES; F...

    >>> # Deletes the field
    >>> from techminer2.database.operators import DeleteOperator
    >>> DeleteOperator(
    ...     field="author_keywords_copy",
    ...     root_directory="examples/fintech/",
    ... ).run()


"""

from techminer2._internals.mixins import ParamsMixin
from techminer2.io._internals.operations.copy_column import copy_column
from techminer2.text.extract._helpers.protected_fields import PROTECTED_FIELDS


class CopyColumn(
    ParamsMixin,
):

    def run(self) -> int:

        if self.params.source_field == self.params.target_field:
            raise ValueError(
                f"Source and target fields must differ (got `{self.params.source_field}`)"
            )

        if self.params.target_field in PROTECTED_FIELDS:
            raise ValueError(
                f"Cannot overwrite protected field `{self.params.target_field}`"
            )

        return copy_column(
            source=self.params.source_field,
            target=self.params.target_field,
            root_directory=self.params.root_directory,
        )


#
