# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Stemming AND
===============================================================================

>>> from techminer2.refine.fields import stemming_and, delete_field
>>> stemming_and(
...     item="ARTIFICIAL_INTELLIGENCE",
...     src_field="author_keywords",
...     dst_field="stemming",
...     #
...     # DATABASE PARAMS:
...     root_dir="example",
... )

>>> # TEST:  
>>> from techminer2.analyze import performance_metrics
>>> performance_metrics(
...     field='stemming',
...     metric='OCC',
...     top_n=10,
...     root_dir="example/", 
... ).df_['OCC'].head(10)
stemming
ARTIFICIAL_INTELLIGENCE            4
ARTIFICIAL_INTELLIGENCE_AND_LAW    1
Name: OCC, dtype: int64


>>> delete_field(
...     field="stemming",
...     #
...     # DATABASE PARAMS:
...     root_dir="example",
... )


"""
import glob
import os.path

import pandas as pd
from textblob import TextBlob

from .protected_fields import PROTECTED_FIELDS


def stemming_and(
    item,
    src_field,
    dst_field,
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """
    :meta private:
    """
    if dst_field in PROTECTED_FIELDS:
        raise ValueError(f"Field `{dst_field}` is protected")

    item_blob = TextBlob(item.replace("_", " "))
    stemmed = [word.stem() for word in item_blob.words]

    #
    # Computes the intersection per database
    files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
    column = []
    for file in files:
        #
        # Loads data
        data = pd.read_csv(file, encoding="utf-8", compression="zip")
        if src_field in data.columns:
            column.append(data[[src_field]])

    items = pd.concat(column, ignore_index=True)
    items = items.dropna()
    items[src_field] = items[src_field].str.split("; ")
    items = items.explode(src_field)
    items[src_field] = items[src_field].str.strip()
    items["keys"] = items[src_field].copy()
    items["keys"] = items["keys"].str.replace("_", " ")
    items["keys"] = items["keys"].map(TextBlob)
    items["keys"] = items["keys"].map(lambda x: [word.stem() for word in x.words])
    items["keys"] = items["keys"].map(lambda x: all(t in x for t in stemmed))

    items = sorted(set(items.loc[items["keys"], src_field].to_list()))

    files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
    for file in files:
        #
        # Loads data
        data = pd.read_csv(file, encoding="utf-8", compression="zip")
        #
        data[dst_field] = data[src_field].copy()
        #
        data[dst_field] = data[dst_field].map(lambda x: x.split("; "), na_action="ignore")
        data[dst_field] = data[dst_field].map(
            lambda x: [y for y in x if y in items], na_action="ignore"
        )
        data[dst_field] = data[dst_field].map(lambda x: pd.NA if x == [] else x, na_action="ignore")
        data[dst_field] = data[dst_field].map(lambda x: "; ".join(x) if isinstance(x, list) else x)
        #
        data.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")
