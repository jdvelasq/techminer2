"""
CountColumnItems
===============================================================================

Smoke test:
    >>> from tm2p.enum import Field
    >>> from tm2p.ingest.oper import CountColumnItems
    >>> (
    ...     CountColumnItems()
    ...     .with_source_field(Field.AUTHKW_RAW)
    ...     .with_target_field(Field.USR0)
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .run()
    ... )

    >>> from tm2p.ingest.oper import Query
    >>> (
    ...     Query()
    ...     .with_query_expression("SELECT AUTHKW_RAW, USR0 FROM database LIMIT 5;")
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     .run()
    ... )  # doctest: +SKIP
                                              AUTHKW_RAW  USR0
    0  audio classification; interpretability; state ...     4
    1  evolutionary computation; high-dimensional ben...     6
    2  convolutional neural network (cnn); hardware (...     5
    3         android; hdc; health monitoring; wearables     4
    4  adaptive modeling; geotechnical engineering; i...     5




"""

from tm2p._intern import ParamsMixin
from tm2p.ingest.datasrc._intern.oper.count_col_item import count_column_items
from tm2p.ingest.extr._helpers._protected_fields import PROTECTED_FIELDS


class CountColumnItems(
    ParamsMixin,
):
    """:meta private:"""

    def run(self) -> None:

        if self.params.source_field.value == self.params.target_field.value:
            raise ValueError(
                f"Source and target fields must differ (got `{self.params.source_field.value}`)"
            )

        if self.params.target_field in PROTECTED_FIELDS:
            raise ValueError(
                f"Cannot overwrite protected field `{self.params.target_field}`"
            )

        count_column_items(
            source=self.params.source_field,
            target=self.params.target_field,
            root_directory=self.params.root_directory,
        )


#
