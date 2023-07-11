# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""Concordances Prompt from Records"""

import pandas as pd

from .concordances_lib import (
    get_context_phrases_from_records,
    transform_context_phrases_to_contexts_paragraphs,
)
from .format_prompt_for_paragraphs import format_prompt_for_paragraphs


def concordances_prompt_from_records(
    #
    # FUNCTION PARAMS:
    search_for: str,
    top_n: int,
    records: pd.DataFrame,
):
    """Checks the occurrence contexts of a given text in the abstract's phrases."""

    #
    # MAIN CODE:
    #
    context_phrases = get_context_phrases_from_records(
        search_for=search_for, records=records, top_n=top_n
    )
    context_paragraphs = transform_context_phrases_to_contexts_paragraphs(
        context_phrases
    )

    main_text = (
        "Your task is to generate a short summary of a term for a research "
        "paper. Summarize the paragraphs below, delimited by triple backticks, "
        "in one unique paragraph, in at most 30 words, focusing on the any aspect contributing "
        f"to the definition and characteristics of the term '{search_for.upper()}'."
    )

    paragraphs_list = context_paragraphs.to_list()

    return format_prompt_for_paragraphs(main_text, paragraphs_list)
