"""
CopyColumn
===============================================================================

Smoke Test:
    >>> from tm2p.enum import Field
    >>> from tm2p.ingest.oper import CopyColumn
    >>> (
    ...     CopyColumn()
    ...     .with_source_field(Field.AUTHKW_RAW)
    ...     .with_target_field(Field.USR0)
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .run()
    ... )

    >>> from tm2p.ingest.oper import Query
    >>> (
    ...     Query()
    ...     .with_query_expression("SELECT USR0 FROM database LIMIT 5;")
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )  # doctest: +SKIP
                                                    USR0
    0  audio classification; interpretability; state ...
    1  evolutionary computation; high-dimensional ben...
    2  convolutional neural network (cnn); hardware (...
    3         android; hdc; health monitoring; wearables
    4  adaptive modeling; geotechnical engineering; i...


"""

from tm2p._intern import ParamsMixin
from tm2p.ingest.datasrc._intern.oper.copy_col import copy_column
from tm2p.ingest.extr._helpers._protected_fields import PROTECTED_FIELDS


class CopyColumn(
    ParamsMixin,
):
    """:meta private:"""

    def run(self) -> None:

        if self.params.source_field == self.params.target_field:
            raise ValueError(
                f"Source and target fields must differ (got `{self.params.source_field}`)"
            )

        if self.params.target_field in PROTECTED_FIELDS:
            raise ValueError(
                f"Cannot overwrite protected field `{self.params.target_field}`"
            )

        copy_column(
            source=self.params.source_field,
            target=self.params.target_field,
            root_directory=self.params.root_directory,
        )
