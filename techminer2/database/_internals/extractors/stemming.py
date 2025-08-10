# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

from typing import Dict, List, Optional, Tuple

from textblob import TextBlob  # type: ignore

from .get_values_from_field import internal__get_values_from_field


def internal__stemming_and(params):
    """:meta private:"""

    return stemming(params.update(stemming_fn=apply_stemming_and_operator))


def internal__stemming_or(params):
    """:meta private:"""

    return stemming(params.update(stemming_fn=apply_stemming_or_operator))


def stemming(params):
    """:meta private:"""

    stemmed_terms = get_stemmed_items(params.pattern)
    data_frame = internal__get_values_from_field(params)
    data_frame = create_keys_column(data_frame)

    #
    # Checks if all stemmed words are in the list of stemmed words
    data_frame = params.stemming_fn(data_frame, stemmed_terms)
    data_frame = data_frame[data_frame.selected]
    data_frame = data_frame.sort_values("term", ascending=True)
    terms = data_frame.term.to_list()
    return terms


def apply_stemming_and_operator(
    data_frame,
    stemmed_terms,
):
    """Checks if all stemmed terms are in the list of stemmed words."""

    data_frame["selected"] = data_frame["keys"].map(
        lambda words: any(
            all(stemmed_word in words for stemmed_word in stemmed_term)
            for stemmed_term in stemmed_terms
        )
    )

    return data_frame


def apply_stemming_or_operator(
    data_frame,
    stemmed_terms,
):
    """Checks if all stemmed terms are in the list of stemmed words."""

    data_frame["selected"] = data_frame["keys"].map(
        lambda words: any(
            any(stemmed_word in words for stemmed_word in stemmed_term)
            for stemmed_term in stemmed_terms
        )
    )

    return data_frame


def create_keys_column(data_frame):
    """Createa column with stemmed terms."""

    data_frame["keys"] = data_frame["term"].copy()
    data_frame["keys"] = data_frame["keys"].str.replace("_", " ")
    data_frame["keys"] = data_frame["keys"].map(TextBlob)
    data_frame["keys"] = data_frame["keys"].map(
        lambda x: [word.stem() for word in x.words]
    )

    return data_frame


def get_stemmed_items(items):
    """Returns a list of stemmed terms from a list of items."""
    if isinstance(items, str):
        items = [items]

    item_blobs = [TextBlob(item.replace("_", " ")) for item in items]
    stemmed_terms = [
        [word.stem() for word in item_blob.words] for item_blob in item_blobs
    ]

    return stemmed_terms
