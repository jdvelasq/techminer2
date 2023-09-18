# flake8: noqa
# pylint: disable=line-too-long
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=missing-docstring
"""Format chatbot prompt for paragraphs."""

import textwrap

TEXTWRAP_WIDTH = 73


def format_prompt_for_records(main_text, secondary_text, records, weight=None):
    """Generate prompt for records."""

    if "abstract" not in records.columns:
        return "No abstracts found."

    records = records.copy()
    records = records.dropna(subset=["abstract"])

    # main_prompt = textwrap.fill(main_text, width=TEXTWRAP_WIDTH)
    # main_prompt = main_prompt.replace("\n", " \\\n")
    # main_prompt += "\n\n"

    # secondary_prompt = textwrap.fill(secondary_text, width=TEXTWRAP_WIDTH)
    # secondary_prompt = secondary_prompt.replace("\n", " \\\n")
    # secondary_prompt += "\n\n"

    text = ""
    counter = 0
    for i_record, (_, record) in enumerate(records.iterrows()):
        #
        # Header counter
        counter += 1
        if counter > 10:
            counter = 1
            if i_record < len(records) - 1:
                text += secondary_text

        #
        # Article ID
        record_id = str(record.article)
        record_id = textwrap.fill(record_id, width=TEXTWRAP_WIDTH)
        record_id = record_id.replace("\n", " \\\n")

        #
        # Article title
        record_title = str(record.title)
        record_title = textwrap.fill(record_title, width=TEXTWRAP_WIDTH)
        record_title = record_title.replace("\n", " \\\n")

        #
        # Abstract
        abstract = textwrap.fill(record.abstract, width=TEXTWRAP_WIDTH)
        abstract = abstract.replace("\n", " \\\n")

        #
        # Text:
        # text += "\nBelow appears the following records: \n\n"

        text += f"##: {i_record+1}\n"
        text += f"Record-No: {record.art_no}\n"

        # Weight
        if weight is not None:
            text += f"Citations: {record[weight]}\n"

        text += f"Record-ID: {record_id}\n"
        text += f"Title: {record_title}\n"
        text += f"Abstract:\n```\n{abstract}\n```\n\n"
        text += "--\n\n"

    return main_text + text
