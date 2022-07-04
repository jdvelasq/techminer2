"""
Word Associations for All Items
===============================================================================


>>> from techminer2 import *
>>> directory = "data/"

>>> word_associations_for_all_items(
...     column='author_keywords',
...     directory=directory,
... ).head(10)
                    word_a                   word_b  CO_OCC
0                  fintech                  regtech      42
1                  regtech                  fintech      42
2               blockchain                  regtech      17
3                  regtech               blockchain      17
4               blockchain                  fintech      14
5                  fintech               blockchain      14
6               compliance                  regtech      12
7                  regtech               compliance      12
8  artificial intelligence                  regtech      10
9                  regtech  artificial intelligence      10


"""
from ._read_records import read_records


def word_associations_for_all_items(
    column,
    top_n=10,
    directory="./",
    database="documents",
):
    """Computes the co-occurrence matrix for a given column."""

    records = read_records(
        directory=directory,
        database=database,
        use_filter=True,
    )
    records = records[[column]]
    records = records.assign(word_b=records[column])
    records = records.dropna()

    records["word_b"] = records["word_b"].str.split(";")
    records = records.explode("word_b")
    records["word_b"] = records["word_b"].str.strip()

    records[column] = records[column].str.split(";")
    records = records.explode(column)
    records[column] = records[column].str.strip()

    records = records.assign(CO_OCC=1)
    records = records.groupby([column, "word_b"], as_index=False).agg({"CO_OCC": "sum"})
    records = records.rename(columns={column: "word_a"})
    records = records[records.word_a != records.word_b]
    records = records.sort_values(by=["CO_OCC", "word_a"], ascending=[False, True])
    if top_n is not None:
        records = records.head(top_n)
    records = records.reset_index(drop=True)

    return records
