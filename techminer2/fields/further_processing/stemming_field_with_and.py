# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Stemming Field with AND
===============================================================================

>>> from techminer2.fields.further_processing import stemming_field_with_and
>>> stemming_field_with_and(  # doctest: +SKIP
...     items="ARTIFICIAL_INTELLIGENCE",
...     source="author_keywords",
...     dest="stemming",
...     #
...     # DATABASE PARAMS:
...     root_dir="example",
... )

"""
import glob
import os.path

import pandas as pd
from textblob import TextBlob

from ..._dtypes import DTYPES
from ..protected_fields import PROTECTED_FIELDS


def stemming_field_with_and(
    items,
    source,
    dest,
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """
    :meta private:
    """
    if dest in PROTECTED_FIELDS:
        raise ValueError(f"Field `{dest}` is protected")

    _stemming_field_with_and(
        items=items,
        source=source,
        dest=dest,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
    )


def _stemming_field_with_and(
    items,
    source,
    dest,
    #
    # DATABASE PARAMS:
    root_dir,
):
    if isinstance(items, str):
        items = [items]

    item_blobs = [TextBlob(item.replace("_", " ")) for item in items]
    stemmed_terms = [[word.stem() for word in item_blob.words] for item_blob in item_blobs]

    #
    # Collects the terms in all databases to compute the intersection
    files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
    column = []
    for file in files:
        #
        # Loads data
        data = pd.read_csv(file, encoding="utf-8", compression="zip", dtype=DTYPES)
        if source in data.columns:
            column.append(data[[source]])
    items = pd.concat(column, ignore_index=True)
    items = items.dropna()

    #
    # Explode multiple terms in a single cell
    items[source] = items[source].str.split("; ")
    items = items.explode(source)
    items[source] = items[source].str.strip()

    #
    # Stemming all words in each cell
    items["keys"] = items[source].copy()
    items["keys"] = items["keys"].str.replace("_", " ")
    items["keys"] = items["keys"].map(TextBlob)
    items["keys"] = items["keys"].map(lambda x: [word.stem() for word in x.words])

    #
    # Checks if all stemmed words are in the list of stemmed words
    items["keys"] = items["keys"].map(
        lambda words: any(
            all(stemmed_word in words for stemmed_word in stemmed_term)
            for stemmed_term in stemmed_terms
        )
    )

    #
    # Extracts the selected terms
    items = sorted(set(items.loc[items["keys"], source].to_list()))

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
        data[dest] = data[dest].map(lambda x: [y for y in x if y in items], na_action="ignore")
        data[dest] = data[dest].map(lambda x: pd.NA if x == [] else x, na_action="ignore")
        data[dest] = data[dest].map(lambda x: "; ".join(x) if isinstance(x, list) else x)
        #
        data.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")
