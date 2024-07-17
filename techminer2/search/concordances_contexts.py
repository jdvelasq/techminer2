# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Concordances Contexts
=========================================================================================

Abstract concordances exploration tool.


>>> from techminer2.search import concordances_contexts
>>> contexts = concordances_contexts( # doctest: +SKIP
...     search_for='FINTECH',
...     top_n=2,
...     root_dir="example/",
... )
>>> print(contexts) # doctest: +SKIP


"""
import pandas as pd

from .._core.read_filtered_database import read_filtered_database
from .concordances_lib import get_context_phrases_from_records


def concordances_contexts(
    #
    # FUNCTION PARAMS:
    search_for: str,
    top_n: int,
    #
    # DATABASE PARAMS:
    root_dir: str = "./",
    database: str = "main",
    year_filter: tuple = (None, None),
    cited_by_filter: tuple = (None, None),
    **filters,
):
    """Checks the occurrence contexts of a given text in the abstract's phrases."""

    def create_contexts_table(
        context_phrases: pd.Series,
    ):
        """Extracts the contexts table."""

        regex = r"\b" + search_for + r"\b"
        contexts = context_phrases.str.extract(r"(?P<left_context>[\s \S]*)" + regex + r"(?P<right_context>[\s \S]*)")

        contexts["left_context"] = contexts["left_context"].fillna("")
        contexts["left_context"] = contexts["left_context"].str.strip()

        contexts["right_context"] = contexts["right_context"].fillna("")
        contexts["right_context"] = contexts["right_context"].str.strip()

        contexts = contexts[contexts["left_context"].map(lambda x: x != "") | contexts["right_context"].map(lambda x: x != "")]

        return contexts

    def transform_context_table_to_contexts(
        contexts: pd.DataFrame,
    ):
        """Transforms the contexts table to a text."""

        contexts = contexts.copy()

        contexts["left_r"] = contexts["left_context"].str[::-1]

        contexts = contexts.sort_values(["left_r", "right_context"])

        contexts["left_context"] = contexts["left_context"].map(lambda x: "<<< " + x[-56:] if len(x) > 60 else x)
        contexts["right_context"] = contexts["right_context"].map(lambda x: x[:56] + " >>>" if len(x) > 60 else x)

        texts = []
        for _, row in contexts.iterrows():
            text = f"{row['left_context']:>60} {search_for.upper()} {row['right_context']}"
            texts.append(text)

        return "\n".join(texts)

    records = read_filtered_database(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    context_phrases = get_context_phrases_from_records(search_for=search_for, records=records, top_n=top_n)
    context_table = create_contexts_table(context_phrases)
    contexts = transform_context_table_to_contexts(context_table)

    return contexts
