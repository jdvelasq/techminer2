"""
SummarySheet
===============================================================================

Smoke tests:
    >>> from tm2p.ingest.records import SummarySheet
    >>> df = (
    ...     SummarySheet()
    ...     #
    ...     .where_root_directory("tests/scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     #
    ...     .run()
    ... )
    >>> print(df.head(5).to_string(index=True))
            COLUMN  NUM_REC COVERAGE
    0    ABSTR_RAW      180  100.00%
    1    ABSTR_TOK      180  100.00%
    2  ABSTR_UPPER      180  100.00%
    3        AFFIL      176   97.78%
    4       ART_NO       69   38.33%





"""

import pandas as pd  # type: ignore

from tm2p._intern import ParamsMixin
from tm2p._intern.data_access import load_filtered_main_csv_zip
from tm2p.enum import Col

COVERAGE = Col.COVERAGE
FIELD = Col.FIELD
NUM_REC = Col.NUM_REC


class SummarySheet(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        records = load_filtered_main_csv_zip(params=self.params)

        #
        # Compute stats per column
        columns = sorted(records.columns)

        n_documents = len(records)

        report = pd.DataFrame({FIELD: columns})

        report[NUM_REC] = [n_documents - records[col].isnull().sum() for col in columns]

        report[COVERAGE] = [
            f"{100*(float(n_documents) - records[col].isnull().sum()) / n_documents:5.2f}%"
            for col in columns
        ]

        return report
