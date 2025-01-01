"""Create a text report with the imported records."""

# from ...._core.read_filtered_database import read_filtered_database
# from ....helpers.helper_format_report_for_records import helper_format_report_for_records


# def create_imported_records_report(root_dir):
#     """:meta private:"""

#     records = read_filtered_database(
#         root_dir=root_dir,
#         database="main",
#         year_filter=(None, None),
#         cited_by_filter=(None, None),
#     )

#     helper_format_report_for_records(
#         root_dir=root_dir,
#         target_dir="",
#         records=records,
#         report_filename="../reports/records.txt",
#     )
