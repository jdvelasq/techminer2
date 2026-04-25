"""
Query
===============================================================================

Smoke test:
    >>> from tm2p.ingest.oper import Query
    >>> df = (
    ...     Query()
    ...     #
    ...     .with_query_expression("SELECT SRC_ISO4 FROM database LIMIT 5;")
    ...     #
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> assert df.shape[0] > 0
    >>> assert set(df.columns) == {"SRC_ISO4"}
    >>> df
                         SRC_ISO4
    0                  MACH LEARN
    1            INTELL SYST APPL
    2              IEEE SENSORS J
    3  MIDWEST SYMP CIRCUITS SYST
    4           COMPUT ELECTR ENG

"""

import duckdb

from tm2p._intern import ParamsMixin
from tm2p._intern.data_access import load_filtered_main_csv_zip


class Query(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        database = load_filtered_main_csv_zip(params=self.params)
        duckdb.register("database", database)
        if self.params.query_expression is None:
            raise ValueError(
                "Query expression cannot be None. Use .with_query_expression() to set it."
            )
        return duckdb.query(self.params.query_expression).df()
