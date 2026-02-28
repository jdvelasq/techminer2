from textblob import TextBlob  # type: ignore

from tm2p._intern import Params
from tm2p.ingest.extr._helpers.values import extract_values


def extract_stemming_and(params: Params) -> list[str]:
    """:meta private:"""

    return _stemming(params.update(stemming_fn=_apply_stemming_and_operator))


def extract_stemming_or(params: Params) -> list[str]:
    """:meta private:"""

    return _stemming(params.update(stemming_fn=_apply_stemming_or_operator))


def _stemming(params: Params) -> list[str]:
    """:meta private:"""

    stemmed_terms = get_stemmed_items(params.pattern)
    df = extract_values(params)
    df = create_keys_column(df)

    #
    # Checks if all stemmed words are in the list of stemmed words
    df = params.stemming_fn(df, stemmed_terms)
    df = df[df.selected]
    df = df.sort_values("term", ascending=True)
    terms = df.term.to_list()
    return terms


def _apply_stemming_and_operator(
    df,
    stemmed_terms,
):
    """Checks if all stemmed terms are in the list of stemmed words."""

    df["selected"] = df["keys"].map(
        lambda words: any(
            all(stemmed_word in words for stemmed_word in stemmed_term)
            for stemmed_term in stemmed_terms
        )
    )

    return df


def _apply_stemming_or_operator(
    df,
    stemmed_terms,
):
    """Checks if all stemmed terms are in the list of stemmed words."""

    df["selected"] = df["keys"].map(
        lambda words: any(
            any(stemmed_word in words for stemmed_word in stemmed_term)
            for stemmed_term in stemmed_terms
        )
    )

    return df


def create_keys_column(df):
    """Createa column with stemmed terms."""

    df["keys"] = df["term"].copy()
    df["keys"] = df["keys"].str.replace("_", " ")
    df["keys"] = df["keys"].map(TextBlob)
    df["keys"] = df["keys"].map(lambda x: [word.stem() for word in x.words])

    return df


def get_stemmed_items(items):
    """Returns a list of stemmed terms from a list of items."""
    if isinstance(items, str):
        items = [items]

    item_blobs = [TextBlob(item.replace("_", " ")) for item in items]
    stemmed_terms = [
        [word.stem() for word in item_blob.words] for item_blob in item_blobs  # type: ignore
    ]

    return stemmed_terms
