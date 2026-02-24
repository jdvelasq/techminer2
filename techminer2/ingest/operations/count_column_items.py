"""
CountColumnItems
===============================================================================

Smoke test:
    >>> from techminer2 import CorpusField
    >>> from techminer2.ingest.operations import CountColumnItems
    >>> (
    ...     CountColumnItems()
    ...     .with_source_field(CorpusField.AUTH_KEY_RAW)
    ...     .with_target_field(CorpusField.USER_0)
    ...     .where_root_directory("tests/fintech/")
    ...     .run()
    ... )
    37

    >>> from techminer2.ingest.operations import Query
    >>> (
    ...     Query()
    ...     .with_query_expression("SELECT AUTH_KEY_RAW, USER_0 FROM database LIMIT 5;")
    ...     .where_root_directory("tests/fintech/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .run()
    ... )
                                            AUTH_KEY_RAW  USER_0
    0  Banking; Financial institution; Financial serv...       7
    1  Bank; Blockchain; Cryptocurrency; Payment; Tec...       6
    2  Actor network theory; Chinese telecom; Fintech...       4
    3  Content analysis; Digitalization; FinTech; Inn...       5
    4  Elaboration likelihood model; Fintech; K pay; ...       4




"""

from techminer2._internals import ParamsMixin
from techminer2.ingest.data_sources._internals.operations.count_column_items import (
    count_column_items,
)
from techminer2.ingest.extract._helpers._protected_fields import PROTECTED_FIELDS


class CountColumnItems(
    ParamsMixin,
):
    """:meta private:"""

    def run(self) -> int:

        if self.params.source_field.value == self.params.target_field.value:
            raise ValueError(
                f"Source and target fields must differ (got `{self.params.source_field.value}`)"
            )

        if self.params.target_field in PROTECTED_FIELDS:
            raise ValueError(
                f"Cannot overwrite protected field `{self.params.target_field}`"
            )
        return count_column_items(
            source=self.params.source_field,
            target=self.params.target_field,
            root_directory=self.params.root_directory,
        )


#
