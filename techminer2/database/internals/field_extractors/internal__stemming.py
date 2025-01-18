# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

from textblob import TextBlob  # type: ignore

from .internal__get_field_values_from_database import (
    internal__get_field_values_from_database,
)


def internal__stemming_and(
    custom_items,
    source_field,
    #
    # DATABASE PARAMS:
    root_dir,
    database: str,
    year_filter: tuple,
    cited_by_filter: tuple,
    sort_by: str,
    **filters,
):
    """:meta private:"""

    return stemming(
        custom_items=custom_items,
        source_field=source_field,
        stemming_fn=apply_stemming_and_operator,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        sort_by=sort_by,
        **filters,
    )


def internal__stemming_or(
    custom_items,
    source_field,
    #
    # DATABASE PARAMS:
    root_dir,
    database: str,
    year_filter: tuple,
    cited_by_filter: tuple,
    sort_by: str,
    **filters,
):
    """:meta private:"""

    return stemming(
        custom_items=custom_items,
        source_field=source_field,
        stemming_fn=apply_stemming_or_operator,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        sort_by=sort_by,
        **filters,
    )


def stemming(
    custom_items,
    source_field,
    stemming_fn,
    #
    # DATABASE PARAMS:
    root_dir: str,
    database: str,
    year_filter: tuple,
    cited_by_filter: tuple,
    sort_by: str,
    **filters,
):
    """:meta private:"""

    stemmed_terms = get_stemmed_items(custom_items)
    df = internal__get_field_values_from_database(
        field=source_field,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        sort_by=sort_by,
        **filters,
    )
    df = create_keys_column(df)

    #
    # Checks if all stemmed words are in the list of stemmed words
    df = stemming_fn(df, stemmed_terms)
    df = df[df.selected]
    df = df.sort_values("term", ascending=True)
    terms = df.term.to_list()
    return terms


def apply_stemming_and_operator(df, stemmed_terms):
    """Checks if all stemmed terms are in the list of stemmed words."""

    df["selected"] = df["keys"].map(
        lambda words: any(
            all(stemmed_word in words for stemmed_word in stemmed_term)
            for stemmed_term in stemmed_terms
        )
    )

    return df


def apply_stemming_or_operator(df, stemmed_terms):
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
        [word.stem() for word in item_blob.words] for item_blob in item_blobs
    ]

    return stemmed_terms
