"""
This module provides a function for building a report file with a given subset
of bibliographic records.

The `build_records_report` function takes a directory path, a target directory
path, a pandas DataFrame of bibliographic records, a report filename, and
generates a report file that includes selected columns for each record. The
report is sorted by the number of global citations for each record, and the
number of records included in the report is limited to a specified length.

Example usage:

    import pandas as pd
    from build_records_report import build_records_report

    # Load bibliographic records into a pandas DataFrame
    records = pd.read_csv('records.csv')

    # Build a report of the top 10 records by global citations
    build_records_report(
        'project_directory',
        'target_directory',
        records,
        'report_filename.csv',
    )

"""

import os.path
import sys
import textwrap

from .create_directory import create_directory


def build_records_report(root_dir, target_dir, records, report_filename):
    """Builds a report file with a given records subset.

    Parameters
    ----------
    root_dir : str
        The root project directory.

    target_dir : str
        The target directory within the "processed" subdirectory.

    records : pandas.DataFrame
        The records to be reported.

    report_filename : str
        The report filename.

    Returns
    -------
    None

    """

    def get_reported_columns(records):
        """Obtains the columns present in the records."""

        column_list = []

        reported_columns = [
            "article",
            "title",
            "authors",
            "global_citations",
            "source_title",
            "year",
            "abstract",
            "author_keywords",
            "index_keywords",
            "raw_author_keywords",
            "raw_index_keywords",
        ]

        for criterion in reported_columns:
            if criterion in records.columns:
                column_list.append(criterion)

        return column_list

    def filter_columns(records, column_list):
        """Selects the columns to be reported."""

        records = records.copy()
        records = records[column_list]
        return records

    def sort_records(records):
        """Sorts the dataframe by global citations"""

        records = records.copy()

        columns = []

        if "global_citations" in records.columns:
            columns.append("global_citations")

        if "local_citations" in records.columns:
            columns.append("local_citations")

        if "year" in records.columns:
            columns.append("year")

        if columns:
            records = records.sort_values(by=columns, ascending=False)

        return records

    def write_report(records, directory, target_dir, report_filename):
        """Writes the report to the file."""

        file_path = os.path.join(
            directory, "processed", target_dir, report_filename
        )

        with open(file_path, "w", encoding="utf-8") as file:
            for index, row in records.iterrows():
                for criterion in reported_columns:
                    if criterion not in row.index:
                        continue

                    if row[criterion] is None:
                        continue

                    if criterion == "article":
                        print("AR ", end="", file=file)

                    if criterion == "title":
                        print("TI ", end="", file=file)

                    if criterion == "authors":
                        print("AU ", end="", file=file)

                    if criterion == "global_citations":
                        print("TC ", end="", file=file)

                    if criterion == "source_title":
                        print("SO ", end="", file=file)

                    if criterion == "year":
                        print("PY ", end="", file=file)

                    if criterion == "abstract":
                        print("AB ", end="", file=file)

                    if criterion == "raw_author_keywords":
                        print("de ", end="", file=file)

                    if criterion == "author_keywords":
                        print("DE ", end="", file=file)

                    if criterion == "raw_index_keywords":
                        print("id ", end="", file=file)

                    if criterion == "index_keywords":
                        print("ID ", end="", file=file)

                    print(
                        textwrap.fill(
                            str(row[criterion]),
                            width=79,
                            initial_indent=" " * 3,
                            subsequent_indent=" " * 3,
                            fix_sentence_endings=True,
                        )[3:],
                        file=file,
                    )

                if index != records.index[-1]:
                    print("-" * 79, file=file)

        sys.stdout.write(f"--INFO-- The file '{file_path}' was created.\n")

    create_directory(base_dir=root_dir, target_dir=target_dir)
    reported_columns = get_reported_columns(records)
    records = filter_columns(records, reported_columns)
    records = sort_records(records)
    write_report(records, root_dir, target_dir, report_filename)
