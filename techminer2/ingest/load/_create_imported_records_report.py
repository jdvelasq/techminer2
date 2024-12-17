"""Create a text report with the imported records."""

from ...internals.read_filtered_database import read_filtered_database
from ...internals.utils.utils_format_report_for_records import (
    _utils_format_report_for_records,
)


def create_imported_records_report(root_dir):
    """:meta private:"""

    records = read_filtered_database(
        root_dir=root_dir,
        database="main",
        year_filter=(None, None),
        cited_by_filter=(None, None),
    )

    _utils_format_report_for_records(
        root_dir=root_dir,
        target_dir="",
        records=records,
        report_filename="../reports/records.txt",
    )
