"""
Merge Columns
===============================================================================

Smoke test:
    >>> from techminer2 import CorpusField
    >>> from techminer2.ingest.operations import MergeColumns
    >>> (
    ...     MergeColumns()
    ...     .with_source_fields(
    ...         (
    ...             CorpusField.AUTH_KEY_RAW,
    ...             CorpusField.IDX_KEY_RAW,
    ...         )
    ...     )
    ...     .with_target_field(CorpusField.USER_0)
    ...     .where_root_directory("tests/data/")
    ...     .run()
    ... )
    26

    >>> from techminer2.ingest.operations import Query
    >>> (
    ...     Query()
    ...     .with_query_expression("SELECT USER_0 FROM database LIMIT 10;")
    ...     .where_root_directory("tests/data/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .run()
    ... )
                                                  USER_0
    0  Banking; Financial institution; Financial serv...
    1  Bank; Block-chain; Blockchain; Cryptocurrency;...
    2  Actor network theory; Chinese telecom; Converg...
    3  Content analysis; Digitalization; FinTech; Inn...
    4  Elaboration likelihood model; Fintech; K pay; ...
    5                Banking innovations; FinTech; Risks
    6  Fintech; financial inclusion; financial scenar...
    7  Conceptual frameworks; Content analysis; Digit...
    8  Bank 3.0; Co-opetition Theory; FinTech; Invest...
    9  Asset managers; Commerce; Cutting edges; Explo...




"""

from techminer2._internals import ParamsMixin
from techminer2.ingest.extract._helpers._protected_fields import PROTECTED_FIELDS
from techminer2.ingest.sources._internals.operations.merge_columns import merge_columns


class MergeColumns(
    ParamsMixin,
):

    def run(self) -> int:

        for source_field in self.params.source_fields:
            if source_field == self.params.target_field:
                raise ValueError(
                    f"Source and target fields must differ (got `{source_field}`)"
                )

        if self.params.target_field in PROTECTED_FIELDS:
            raise ValueError(
                f"Cannot overwrite protected field `{self.params.target_field}`"
            )

        return merge_columns(
            sources=self.params.source_fields,
            target=self.params.target_field,
            root_directory=self.params.root_directory,
        )
