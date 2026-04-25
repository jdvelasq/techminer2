"""
SummarySheet
===============================================================================

Smoke tests:
    >>> from tm2p.ingest.rec import SummarySheet
    >>> df = (
    ...     SummarySheet()
    ...     #
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> assert df.shape[0] > 0
    >>> assert set(df.columns) == {"Col.FIELD", "Col.NUM_REC", "Col
    >>> print(df.head(5).to_string(index=True))  # doctest: +SKIP






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
