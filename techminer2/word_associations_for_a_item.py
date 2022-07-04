"""
Word Associations for a Item
===============================================================================


>>> from techminer2 import *
>>> directory = "data/"

>>> word_associations_for_a_item(
...     'regtech',
...     'author_keywords',
...     directory=directory,
... ).head()
word
fintech                    42
blockchain                 17
compliance                 12
artificial intelligence    10
financial regulation        8
Name: OCC, dtype: int64

"""
from .word_associations_for_all_items import word_associations_for_all_items


def word_associations_for_a_item(
    item,
    column,
    top_n=10,
    directory="./",
    database="documents",
):
    """Computes the co-occurrence matrix for a given column."""

    word_associations = word_associations_for_all_items(
        column=column,
        top_n=None,
        directory=directory,
        database=database,
    )

    word_associations = word_associations[
        (word_associations.word_a == item) | (word_associations.word_b == item)
    ]
    word_associations = word_associations[["word_a", "CO_OCC"]]
    word_associations = word_associations[word_associations.word_a != item]
    word_associations = word_associations.sort_values(
        by=["CO_OCC", "word_a"], ascending=[False, True]
    )
    word_associations = word_associations.rename(
        columns={"CO_OCC": "OCC", "word_a": "word"}
    )
    word_associations = word_associations.set_index("word")
    if top_n is not None:
        word_associations = word_associations.head(top_n)
    return word_associations.OCC
