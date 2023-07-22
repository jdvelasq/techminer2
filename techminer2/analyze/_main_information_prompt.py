# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""Main Information Prompt."""

from ..format_prompt_for_dataframes import format_prompt_for_dataframes


def main_information_prompt(
    data_frame,
):
    main_text = (
        "Your task is to generate a short summary for a research paper of a "
        "table with record and field statistics for a dataset of scientific "
        "publications. The table below, delimited by triple backticks, "
        "provides data on the main characteristics of the records and fields "
        "of the bibliographic dataset. Use the the information in the table "
        "to draw conclusions. Limit your description to one paragraph in at "
        "most 100 words. "
    )

    table_text = data_frame.to_markdown()

    return format_prompt_for_dataframes(main_text, table_text)
