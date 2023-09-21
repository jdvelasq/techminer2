# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""Reporting module for records."""
import os.path
import textwrap


def format_report_for_records(root_dir, target_dir, records, report_filename):
    """Builds a report file with a given records subset."""

    def get_reported_columns(records):
        """Obtains the columns present in the records."""

        column_list = []

        reported_columns = [
            "art_no",
            "article",
            "title",
            "authors",
            "global_citations",
            "source_title",
            "year",
            "abstract",
            "raw_author_keywords",
            "raw_index_keywords",
            "raw_noun_phrases",
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

        file_path = os.path.join(directory, "reports", target_dir, report_filename)

        with open(file_path, "w", encoding="utf-8") as file:
            for i_record, (index, row) in enumerate(records.iterrows()):
                print(f"--- {i_record+1:>03d} ", "-" * 75, sep="", file=file)

                for criterion in reported_columns:
                    if criterion not in row.index:
                        continue

                    if row[criterion] is None:
                        continue

                    if criterion == "art_no":
                        print("Record-No: ", end="", file=file)

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

                    if criterion == "raw_noun_phrases":
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
