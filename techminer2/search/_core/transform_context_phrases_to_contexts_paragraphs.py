# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals

import pandas as pd


def _transform_context_phrases_to_contexts_paragraphs(
    context_phrases: pd.Series,
):
    #
    # Returns the context paragraphs, one for each abstract
    #
    context_paragraphs = context_phrases.groupby(level=0).agg(list)
    context_paragraphs = context_paragraphs.str.join(".  ")
    return context_paragraphs
