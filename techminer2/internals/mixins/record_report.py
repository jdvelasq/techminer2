# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-few-public-methods
"Record Report Mixin."

import textwrap


def step_01_get_existent_columns(records, candiate_columns):
    columns_to_report = []
    for criterion in candiate_columns:
        if criterion in records.columns:
            columns_to_report.append(criterion)
    return columns_to_report


def step_02_filter_columns(records, selected_columns):
    records = records[selected_columns]
    return records


def step_03_rename_columns(records, names_mapping):
    records = records.rename(columns=names_mapping)
    return records


def step_04_build_record_mapping(records):
    return records.to_dict(orient="records")


class RecordMappingMixin:
    """:meta private:"""

    def build_record_mapping(self, records):

        names_mapping = {
            "record_no": "UT",
            "record_id": "AR",
            "raw_document_title": "TI",
            "authors": "AU",
            "global_citations": "TC",
            "source_title": "SO",
            "year": "PY",
            "abstract": "AB",
            "raw_author_keywords": "DE",
            "raw_index_keywords": "ID",
        }

        candiate_columns = names_mapping.keys()

        records = records.copy()

        columns = step_01_get_existent_columns(records, candiate_columns)
        records = step_02_filter_columns(records, columns)
        records = step_03_rename_columns(records, names_mapping)
        mapping = step_04_build_record_mapping(records)

        return mapping


class RecordViewerMixin:
    """:meta private:"""

    def build_record_viewer(self, mapping):

        field_order = [
            "UT",
            "AR",
            "TI",
            "AU",
            "TC",
            "SO",
            "PY",
            "AB",
            "DE",
            "ID",
        ]

        formated_records = []

        for record in mapping:
            text = ""
            for field in field_order:
                if record[field] is not None and str(record[field]) != "nan":
                    text += field + " "
                    text += textwrap.fill(
                        str(record[field]),
                        width=79,
                        initial_indent=" " * 3,
                        subsequent_indent=" " * 3,
                        fix_sentence_endings=True,
                    )[3:]
                    text += "\n"

            formated_records += [text]

        return formated_records
