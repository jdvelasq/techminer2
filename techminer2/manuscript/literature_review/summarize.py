# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches

import os

from techminer2._internals.load_aims_and_scope import internal_load_aims_and_scope
from techminer2._internals.load_core_area import internal_load_core_area
from techminer2._internals.load_template import internal_load_template
from techminer2.database.metrics.records import DataFrame  # type: ignore
from techminer2.database.tools import RecordViewer  # type: ignore
from techminer2.shell.colorized_input import colorized_input


def internal_load_records():

    frame = (
        DataFrame()
        #
        .where_root_directory_is("./")
        .where_database_is("main")
        .where_record_years_range_is(None, None)
        .where_record_citations_range_is(None, None)
        .where_records_match(None)
        .where_records_ordered_by(None)
    ).run()

    frame = frame[
        (frame.document_type == "Review")
        | (frame.raw_document_title.str.lower().str.contains("review"))
    ]
    frame = frame.reset_index(drop=True)

    return frame


def internal_get_documents(frame):

    titles = frame.raw_document_title.to_list()

    documents = (
        RecordViewer()
        #
        .where_root_directory_is("./")
        .where_database_is("main")
        .where_record_years_range_is(None, None)
        .where_record_citations_range_is(None, None)
        .where_records_ordered_by(None)
        .where_records_match(
            {
                "raw_document_title": titles,
            }
        )
    ).run()

    return documents


def internal_create_folder():

    folder = "./outputs/sec_2_literature_review/"
    os.makedirs(folder, exist_ok=True)
    return folder


def execute_summarize_command():

    internal_create_folder()

    word_length = colorized_input(". Paragraph word length > ").strip()

    core_area = internal_load_core_area()
    aims_and_scope = internal_load_aims_and_scope()
    template = internal_load_template("shell.manuscript.review.summarize.txt")
    records = internal_load_records()
    documents = internal_get_documents(records)

    for i, document in enumerate(documents):

        prompt = template.format(
            core_area=core_area,
            aims_and_scope=aims_and_scope,
            word_length=word_length,
            record=document,
        )

        with open(
            f"./outputs/sec_2_literature_review/record_{i+1:03}.txt",
            "w",
            encoding="utf-8",
        ) as file:
            file.write(prompt)
