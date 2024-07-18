# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""Reporting module for records."""
import textwrap


def helper_records_for_reporting(
    #
    # RECORDS:
    records,
):
    """Builds a report file with a given records subset."""

    def get_reported_columns(records):
        """Obtains the columns present in the records."""

        column_list = []

        reported_columns = [
            "art_no",
            "article",
            "raw_docuemnt_title",
            "authors",
            "global_citations",
            "source_title",
            "year",
            "abstract",
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

    def format_records(
        records,
    ):

        # Mapping of criteria to the their prefixes
        criteria_prefix_mapping = {
            "art_no": "Record-No: ",
            "article": "AR ",
            "document_title": "TI ",
            "raw_document_title": "TI ",
            "authors": "AU ",
            "global_citations": "TC ",
            "source_title": "SO ",
            "year": "PY ",
            "abstract": "AB ",
            "raw_author_keywords": "DE ",
            "raw_index_keywords": "ID ",
            "raw_nlp_phrases": "** ",
        }

        formated_records = []

        for _, (_, row) in enumerate(records.iterrows()):

            text = ""

            for criterion in reported_columns:

                # Skip if the criterion is not in the records
                if criterion in row.index and row[criterion] is not None and str(row[criterion]) != "nan":

                    prefix = criteria_prefix_mapping.get(criterion, "")
                    text += prefix
                    text += textwrap.fill(
                        str(row[criterion]),
                        width=79,
                        initial_indent=" " * 3,
                        subsequent_indent=" " * 3,
                        fix_sentence_endings=True,
                    )[3:]
                    text += "\n"

            formated_records += [text]

        return formated_records

    reported_columns = get_reported_columns(records)
    filtered_records = filter_columns(records, reported_columns)
    formated_records = format_records(filtered_records)
    return formated_records
