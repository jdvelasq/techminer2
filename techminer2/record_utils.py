"""Functions for reads (full/filtered) records of the documents.csv file."""

import os
import os.path
import sys
import textwrap

import pandas as pd

from .create_directory import create_directory


def create_records_report(root_dir, target_dir, records, report_filename):
    # pylint: disable=too-many-statements
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
            # "author_keywords",
            # "index_keywords",
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
                        print("DE ", end="", file=file)

                    # if criterion == "author_keywords":
                    #     print("DE ", end="", file=file)

                    if criterion == "raw_index_keywords":
                        print("ID ", end="", file=file)

                    # if criterion == "index_keywords":
                    #     print("ID ", end="", file=file)

                    if str(row[criterion]) == "nan":
                        continue

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


def read_records(
    root_dir="./",
    database="documents",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """loads and filter records of main database text files."""

    def _get_records_from_file(directory, database):
        """Read raw records from a file."""

        file_name = {
            "documents": "_documents.csv",
            "references": "_references.csv",
            "cited_by": "_cited_by.csv",
        }[database]
        file_path = os.path.join(directory, "processed", file_name)
        records = pd.read_csv(file_path, sep=",", encoding="utf-8")
        records = records.drop_duplicates()

        return records

    def _filter_records_by_year(records, year_filter):
        """Filter records by year."""

        if year_filter is None:
            return records

        if not isinstance(year_filter, tuple):
            raise TypeError(
                "The year_range parameter must be a tuple of two values."
            )

        if len(year_filter) != 2:
            raise ValueError(
                "The year_range parameter must be a tuple of two values."
            )

        start_year, end_year = year_filter

        if start_year is not None:
            records = records[records.year >= start_year]

        if end_year is not None:
            records = records[records.year <= end_year]

        return records

    def _filter_records_by_citations(records, cited_by_filter):
        """Filter records by year."""

        if cited_by_filter is None:
            return records

        if not isinstance(cited_by_filter, tuple):
            raise TypeError(
                "The cited_by_range parameter must be a tuple of two values."
            )

        if len(cited_by_filter) != 2:
            raise ValueError(
                "The cited_by_range parameter must be a tuple of two values."
            )

        cited_by_min, cited_by_max = cited_by_filter

        if cited_by_min is not None:
            records = records[records.global_citations >= cited_by_min]

        if cited_by_max is not None:
            records = records[records.global_citations <= cited_by_max]

        return records

    def _apply_filters_to_records(records, **filters):
        """Apply user filters in order."""

        for filter_name, filter_value in filters.items():
            # Split the filter value into a list of strings
            database = records[["article", filter_name]]
            database[filter_name] = database[filter_name].str.split(";")

            # Explode the list of strings into multiple rows
            database = database.explode(filter_name)

            # Remove leading and trailing whitespace from the strings
            database[filter_name] = database[filter_name].str.strip()

            # Keep only records that match the filter value
            database = database[database[filter_name].isin(filter_value)]
            records = records[records["article"].isin(database["article"])]

        return records

    records = _get_records_from_file(root_dir, database)
    records = _filter_records_by_year(records, year_filter)
    records = _filter_records_by_citations(records, cited_by_filter)
    records = _apply_filters_to_records(records, **filters)

    return records
