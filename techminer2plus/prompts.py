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
