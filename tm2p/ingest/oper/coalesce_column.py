"""
CoalesceColumn
===============================================================================

Smoke test:
    >>> from tm2p.enum import Field
    >>> from tm2p.ingest.oper import CopyColumn
    >>> (
    ...     CopyColumn()
    ...     .with_source_field(Field.SRC_ISO4)
    ...     .with_target_field(Field.USR0)
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .run()
    ... )


    >>> from tm2p.ingest.oper import TransformColumn
    >>> (
    ...     TransformColumn()
    ...     .with_source_field(Field.USR0)
    ...     .with_target_field(Field.USR1)
    ...     .with_transformation_function(lambda x: None)
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .run()
    ... )

    >>> from tm2p.ingest.oper import CoalesceColumn
    >>> (
    ...     CoalesceColumn()
    ...     .with_source_field(Field.SRC_ISO4)
    ...     .with_target_field(Field.USR1)
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .with_transformation_function(lambda x: pd.NA)
    ...     .run()
    ... )

    >>> from tm2p.ingest.oper import Query
    >>> (
    ...     Query()
    ...     .with_query_expression("SELECT USR1 FROM database LIMIT 5;")
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     .run()
    ... )  # doctest: +SKIP
                             USR1
    0                  MACH LEARN
    1            INTELL SYST APPL
    2              IEEE SENSORS J
    3  MIDWEST SYMP CIRCUITS SYST
    4           COMPUT ELECTR ENG


"""

from tm2p._intern import ParamsMixin
from tm2p.ingest.datasrc._intern.oper.coalesc_col import coalesce_column
from tm2p.ingest.extr._helpers._protected_fields import PROTECTED_FIELDS


class CoalesceColumn(
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
                f"Cannot fill a protected field `{self.params.target_field}`"
            )

        coalesce_column(
            source=self.params.source_field,
            target=self.params.target_field,
            root_directory=self.params.root_directory,
        )
