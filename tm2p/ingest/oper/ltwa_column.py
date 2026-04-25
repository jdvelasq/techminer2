"""
LTWAColumn
===============================================================================

Smoke test:
    >>> from tm2p.enum import Field
    >>> from tm2p.ingest.oper import LTWAColumn
    >>> (
    ...     LTWAColumn()
    ...     .with_source_field(Field.SRC)
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
    0                                         MACH LEARN
    1                                   INTELL SYST APPL
    2                                     IEEE SENSORS J
    3                         MIDWEST SYMP CIRCUITS SYST
    4                                  COMPUT ELECTR ENG
    5  S3 2025 - PROC 2025 16TH ACM WORK WIREL STUD S...
    6  MOBISYS 2025 - PROC 23RD ACM INT CONF MOB SYST...
    7  9TH INT CONF RECENT ADV INNOV ENG ADV TECHNOL ...
    8                             ELECTRON (SWITZERLAND)
    9                              FRONT COMPUT NEUROSCI



"""

from tm2p._intern import ParamsMixin
from tm2p.ingest.datasrc._intern.oper.ltwa_col import ltwa_column
from tm2p.ingest.extr._helpers._protected_fields import PROTECTED_FIELDS


class LTWAColumn(
    ParamsMixin,
):
    """:meta private:"""

    def run(self) -> None:

        if self.params.source_field == self.params.target_field:
            raise ValueError(
                f"Source and target fields must differ (got `{self.params.source_field}`)"
            )

        if self.params.target_field in PROTECTED_FIELDS:
            raise ValueError(f"Field `{self.params.target_field}` is protected")

        ltwa_column(
            source=self.params.source_field,
            target=self.params.target_field,
            root_directory=self.params.root_directory,
        )


#
