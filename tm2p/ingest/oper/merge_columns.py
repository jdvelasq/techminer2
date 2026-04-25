"""
MergeColumns
===============================================================================

Smoke test:
    >>> from tm2p.enum import Field
    >>> from tm2p.ingest.oper import MergeColumns
    >>> (
    ...     MergeColumns()
    ...     .with_source_fields(
    ...         (
    ...             Field.AUTHKW_RAW,
    ...             Field.IDXKW_RAW,
    ...         )
    ...     )
    ...     .with_target_field(Field.USR0)
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .run()
    ... )

    >>> from tm2p.ingest.oper import Query
    >>> (
    ...     Query()
    ...     .with_query_expression("SELECT USR0 FROM database LIMIT 10;")
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     .run()
    ... )  # doctest: +SKIP
                                                    USR0
    0  audio classification; c++ (programming languag...
    1  artificial intelligence; arts computing; bench...
    2  cmos integrated circuits; convolutional neural...
    3  activity tracking; android; android (operating...
    4  adaptive learning; adaptive modeling; adaptive...
    5  cnns; comparatives studies; convolutional neur...
    6  animal images; animal motion; animals; compute...
    7  % reductions; alu; arithmetic logic unit; c (p...
    8  arts computing; digital watermarking; edge sys...
    9  activation energy; article; bioinformatics; bi...



"""

from tm2p._intern import ParamsMixin
from tm2p.ingest.datasrc._intern.oper.merge_col import merge_columns
from tm2p.ingest.extr._helpers._protected_fields import PROTECTED_FIELDS


class MergeColumns(
    ParamsMixin,
):
    """:meta private:"""

    def run(self) -> None:

        for source_field in self.params.source_fields:
            if source_field == self.params.target_field:
                raise ValueError(
                    f"Source and target fields must differ (got `{source_field}`)"
                )

        if self.params.target_field in PROTECTED_FIELDS:
            raise ValueError(
                f"Cannot overwrite protected field `{self.params.target_field}`"
            )

        merge_columns(
            sources=self.params.source_fields,
            target=self.params.target_field,
            root_directory=self.params.root_directory,
        )
