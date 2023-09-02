# flake8: noqa
# pylint: disable=line-too-long
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=missing-docstring
"""Format chatbot prompt for paragraphs."""

import textwrap

TEXTWRAP_WIDTH = 75


def format_prompt_for_records(main_text, records, weight=None):
    """Generate prompt for records."""

    if "abstract" not in records.columns:
        return "No abstracts found."

    records = records.copy()
    records = records.dropna(subset=["abstract"])

    prompt = textwrap.fill(main_text, width=TEXTWRAP_WIDTH)
    prompt = prompt.replace("\n", " \\\n")
    prompt += "\n\n"

    text = ""
    for i_record, (_, record) in enumerate(records.iterrows()):
        # Article ID
        record_id = str(record.article) + " / " + str(record.title)
        record_id = textwrap.fill(record_id, width=TEXTWRAP_WIDTH)
        record_id = record_id.replace("\n", " \\\n")

        # Abstract
        abstract = textwrap.fill(record.abstract, width=TEXTWRAP_WIDTH)
        abstract = abstract.replace("\n", " \\\n")

        # Weight
        if weight is not None:
            text += f"Record {i_record+1} ({weight.replace('_', ' ').title()}={record[weight]}):\n"
        else:
            text += f"Record {i_record+1}:\n"

        text += f"{record_id}\n"
        text += f"Abstract:\n```\n{abstract}\n```\n\n"

    return prompt + text
