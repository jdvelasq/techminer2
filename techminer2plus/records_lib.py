"""
Read records from database

"""

import os
import os.path
import textwrap

import pandas as pd


def read_records(
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """loads and filter records of main database text files."""

    def _get_records_from_file(directory, database):
        """Read raw records from a file."""

        file_name = None

        if database.startswith("_CLUSTER_"):
            file_name = database + ".csv"
        if database.startswith("_CLUSTERS_"):
            file_name = database + ".csv"

        if file_name is None:
            file_name = {
                "main": "_main.csv",
                "references": "_references.csv",
                "cited_by": "_cited_by.csv",
            }[database]

        file_path = os.path.join(directory, "databases", file_name)
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


def create_records_report(root_dir, target_dir, records, report_filename):
    # pylint: disable=too-many-statements
    """Builds a report file with a given records subset."""

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
            "raw_nlp_phrases",
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

    def write_report_to_file(records, directory, target_dir, report_filename):
        """Writes the report to the file."""

        file_path = os.path.join(
            directory, "reports", target_dir, report_filename
        )

        with open(file_path, "w", encoding="utf-8") as file:
            for i_record, (index, row) in enumerate(records.iterrows()):
                print(f"--- {i_record+1:>03d} ", "-" * 75, sep="", file=file)

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

                    if criterion == "raw_index_keywords":
                        print("ID ", end="", file=file)

                    if criterion == "raw_nlp_phrases":
                        print("** ", end="", file=file)

                    if str(row[criterion]) == "nan":
                        print("", file=file)
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
                    print("", file=file)

        print(f"--INFO-- The file '{file_path}' was created.")

    reported_columns = get_reported_columns(records)
    records = filter_columns(records, reported_columns)
    write_report_to_file(records, root_dir, target_dir, report_filename)
