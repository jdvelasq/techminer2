"""Create a text report with the imported records."""


from .._common.format_report_for_records import format_report_for_records
from ..read_records import read_records


def create_imported_records_report(root_dir):
    """:meta private:"""

    records = read_records(
        root_dir=root_dir,
        database="main",
        year_filter=(None, None),
        cited_by_filter=(None, None),
    )

    format_report_for_records(
        root_dir=root_dir,
        target_dir="",
        records=records,
        report_filename="../report/records.txt",
    )
