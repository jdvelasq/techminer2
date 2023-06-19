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
