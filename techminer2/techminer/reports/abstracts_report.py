"""
Abstracts Report 
===============================================================================

Generates a report for the records meeting the given criteria.

>>> root_dir = "data/regtech/"

>>> from techminer2 import techminer
>>> techminer.reports.abstracts_report(
...     criterion="author_keywords",
...     custom_topics=["regulatory technology", "regtech"],
...     root_dir=root_dir,
... )
--INFO-- The file 'data/regtech/reports/abstracts_report.txt' was created

"""
import os.path
import textwrap

import pandas as pd

from ...utils import records


# pylint: disable=too-many-arguments
def abstracts_report(
    criterion=None,
    custom_topics=None,
    file_name="abstracts_report.txt",
    use_textwrap=True,
    root_dir="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """
    Extracts abstracts of documents meeting the given criteria.

    Args:
        criterion (str): name of the column to be used as criterion.
        custom_topics (list): list of custom topics.
        file_name (str): name of the output file.
        use_textwrap (bool): if True, the text is wrapped.
        root_dir (str): root directory.
        database (str): name of the database.
        start_year (int): start year.
        end_year (int): end year.
        **filters: filters.

    Returns:
        None.

    """

    records = records.read_records(
        root_dir=root_dir,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    if criterion:
        records = _sort_by_custom_terms(criterion, custom_topics, records)
    else:
        records = _sort_by_default_criteria(records)

    _write_report(criterion, file_name, use_textwrap, root_dir, records)


def _sort_by_custom_terms(criterion, custom_topics, records):
    def _filter_records_by_custom_topics(records):
        records = records.copy()
        selected_records = records[["article", criterion]]
        selected_records[criterion] = selected_records[criterion].str.split(
            ";"
        )
        selected_records = selected_records.explode(criterion)
        selected_records[criterion] = selected_records[criterion].str.strip()
        selected_records = selected_records[
            selected_records[criterion].isin(custom_topics)
        ]
        return records[records["article"].isin(selected_records["article"])]

    def _convert_topics_to_list(records):
        records = records.copy()
        records["TOPICS"] = records[criterion].copy()
        records["TOPICS"] = records["TOPICS"].str.split(";")
        records["TOPICS"] = records["TOPICS"].map(
            lambda x: [y.strip() for y in x]
        )
        return records

    def _compute_points(records):
        records = records.copy()
        records["POINTS"] = records["TOPICS"].apply(
            lambda x: "".join(
                ["1" if topic in x else "0" for topic in custom_topics]
            )
        )
        return records

    def _sort_by_points(records):
        records = records.copy()
        records = records.sort_values(
            by=["POINTS", "global_citations", "local_citations"],
            ascending=[False, False, False],
        )
        return records

    def _reorder_terms(criterion, custom_topics, records):
        records = records.copy()
        records["TERMS"] = records[criterion].str.split(";")
        records["TERMS"] = records["TERMS"].map(
            lambda x: [y.strip() for y in x]
        )
        records["TERMS_1"] = records["TERMS"].map(
            lambda x: [
                "(*) " + custom_topic
                for custom_topic in custom_topics
                if custom_topic in x
            ],
            na_action="ignore",
        )
        records["TERMS_2"] = records["TERMS"].map(
            lambda x: [y for y in x if y not in custom_topics],
            na_action="ignore",
        )
        records["TERMS"] = records["TERMS_1"] + records["TERMS_2"]
        records[criterion] = records["TERMS"].str.join("; ")

        return records

    records = _filter_records_by_custom_topics(records)
    records = _convert_topics_to_list(records)
    records = _compute_points(records)
    records = _sort_by_points(records)
    records = _reorder_terms(criterion, custom_topics, records)
    return records


def _sort_by_default_criteria(records):
    records = records.sort_values(
        by=["global_citations", "local_citations"],
        ascending=[False, False],
    )
    return records


def _write_report(criterion, file_name, use_textwrap, directory, records):
    def format_text(text, use_textwrap):
        if pd.isna(text):
            return ""

        if use_textwrap:
            return textwrap.fill(
                text,
                width=87,
                initial_indent=" " * 0,
                subsequent_indent=" " * 3,
                fix_sentence_endings=True,
            )

        return text

    def print_field(field, text, out_file):
        if text:
            print(f"{field} {text}", file=out_file)

    file_path = os.path.join(directory, "reports", file_name)

    with open(file_path, "w", encoding="utf-8") as out_file:
        counter = 0

        for _, row in records.iterrows():
            text_article = format_text(row["article"], use_textwrap)
            text_title = format_text(row["title"], use_textwrap)
            if criterion:
                text_criterion = format_text(row[criterion], use_textwrap)
            else:
                text_criterion = None
            text_abstract = format_text(row.get("abstract", ""), use_textwrap)
            text_citation = str(row["global_citations"])

            print(f"-- {counter:03d} " + "-" * 83, file=out_file)
            print_field("AR", text_article, out_file)
            print_field("TI", text_title, out_file)
            if criterion:
                print_field("KW", text_criterion, out_file)
            print_field("TC", text_citation, out_file)
            print_field("AB", text_abstract, out_file)

            print("\n", file=out_file)

            counter += 1

    print(f"--INFO-- The file '{file_path}' was created")
