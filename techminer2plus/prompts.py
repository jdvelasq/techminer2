"""
Functions for generating ChatGPT prompts.
"""
import textwrap

TEXTWRAP_WIDTH = 75


def format_prompt_for_tables(main_text, table_text):
    """Generate prompt for table analysis."""

    prompt = textwrap.fill(main_text, width=TEXTWRAP_WIDTH)
    prompt = prompt.replace("\n", " \\\n")
    return prompt + f"\n\nTable:\n```\n{table_text}\n```\n"


def format_prompt_for_matrices(main_text, matrix_text):
    """Generate prompt for table analysis."""

    prompt = textwrap.fill(main_text, width=TEXTWRAP_WIDTH)
    prompt = prompt.replace("\n", " \\\n")
    return prompt + f"\n\nMatrix:\n```\n{matrix_text}\n```\n"


def format_prompt_for_paragraphs(main_text, paragraphs):
    """Generate prompt for table analysis."""

    prompt = textwrap.fill(main_text, width=TEXTWRAP_WIDTH)
    prompt = prompt.replace("\n", " \\\n")
    prompt += "\n\n"

    text = ""
    for i_paragram, paragraph in enumerate(paragraphs):
        paragraph = textwrap.fill(paragraph, width=TEXTWRAP_WIDTH)
        paragraph = paragraph.replace("\n", " \\\n")
        text += f"Paragraph {i_paragram+1}:\n```\n{paragraph}\n```\n\n"

    return prompt + text


def format_prompt_for_records(main_text, records, weight=None):
    """Generate prompt for records."""

    records = records.copy()
    records = records.dropna(subset=["abstract"])

    prompt = textwrap.fill(main_text, width=TEXTWRAP_WIDTH)
    prompt = prompt.replace("\n", " \\\n")
    prompt += "\n\n"

    text = ""
    for i_record, (_, record) in enumerate(records.iterrows()):
        # Article ID
        record_id = record.article + " / " + record.title
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
        text += f"```\n{abstract}\n```\n\n"

    return prompt + text
