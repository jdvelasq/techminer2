# flake8: noqa
# pylint: disable=line-too-long
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=missing-docstring
"""Format chatbot prompt for paragraphs."""

import textwrap

TEXTWRAP_WIDTH = 73


def format_prompt_for_paragraphs(main_text, paragraphs):
    """Generate prompt for table analysis."""

    prompt = textwrap.fill(main_text, width=TEXTWRAP_WIDTH)
    prompt = prompt.replace("\n", " \\\n")
    prompt += "\n\n"

    text = ""
    for i_paragraph, (paragraph, title) in enumerate(zip(paragraphs, paragraphs.index)):
        paragraph_text = textwrap.fill(paragraph, width=TEXTWRAP_WIDTH)
        paragraph_text = paragraph_text.replace("\n", " \\\n")
        text += f"Record-No: {i_paragraph+1}\n"
        text += f"Artile: {title}\n"
        text += f"Text:```\n{paragraph_text}\n```\n\n--\n\n"

    return prompt + text
