# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

import glob
import os.path
import pathlib

import pandas as pd
from textblob import TextBlob  # type: ignore


def internal__stemming_with_and(
    df,
    field,
    #
    # DATABASE PARAMS:
    root_dir,
):
    """:meta private:"""

    stemmed_terms = get_stemmed_items(df)
    df = get_field_values_from_database(root_dir, field)
    df = create_keys_column(df)

    #
    # Checks if all stemmed words are in the list of stemmed words
    df = stemming_with_and(df, stemmed_terms)

    #
    # Extracts the selected terms
    df = sorted(set(df.loc[df["keys"], source].to_list()))

    #
    # Updates the databases
    files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
    for file in files:
        #
        # Loads data
        data = pd.read_csv(file, encoding="utf-8", compression="zip", dtype=DTYPES)
        #
        data[dest] = data[source].copy()
        #
        data[dest] = data[dest].map(lambda x: x.split("; "), na_action="ignore")
        data[dest] = data[dest].map(
            lambda x: [y for y in x if y in df], na_action="ignore"
        )
        data[dest] = data[dest].map(
            lambda x: pd.NA if x == [] else x, na_action="ignore"
        )
        data[dest] = data[dest].map(
            lambda x: "; ".join(x) if isinstance(x, list) else x
        )
        #
        data.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")


def stemming_with_and(df, stemmed_terms):
    """Checks if all stemmed terms are in the list of stemmed words."""

    df["selected"] = df["keys"].map(
        lambda words: any(
            all(stemmed_word in words for stemmed_word in stemmed_term)
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


def get_field_values_from_database(root_dir, field):
    """Returns a DataFrame with the content of the field in all databases."""

    database_file = pathlib.Path(root_dir) / "databases/database.csv.zip"

    dataframe = pd.read_csv(
        database_file,
        encoding="utf-8",
        compression="zip",
    )

    df = dataframe[[field]].dropna()

    df[field] = df[field].str.split("; ")
    df = df.explode(field)
    df[field] = df[field].str.strip()
    df = df.drop_duplicates()
    df = df.reset_index(drop=True)
    df = df.rename(columns={field: "term"})

    return df
