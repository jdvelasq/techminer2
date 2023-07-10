# flake8: noqa
# pylint: disable=line-too-long
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=missing-docstring
"""Format chatbot prompt for paragraphs."""

import textwrap

TEXTWRAP_WIDTH = 75


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
