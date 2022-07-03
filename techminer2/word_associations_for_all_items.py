"""
Word Associations for All Items
===============================================================================


>>> from techminer2 import *
>>> directory = "data/"

>>> word_associations_for_all_items(
...     column='author_keywords',
...     directory=directory,
... ).head(10)
                    word_A                   word_B  co_occ
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
    records = records.assign(word_B=records[column])
    records = records.dropna()

    records["word_B"] = records["word_B"].str.split(";")
    records = records.explode("word_B")
    records["word_B"] = records["word_B"].str.strip()

    records[column] = records[column].str.split(";")
    records = records.explode(column)
    records[column] = records[column].str.strip()

    records = records.assign(co_occ=1)
    records = records.groupby([column, "word_B"], as_index=False).agg({"co_occ": "sum"})
    records = records.rename(columns={column: "word_A"})
    records = records[records.word_A != records.word_B]
    records = records.sort_values(by=["co_occ", "word_A"], ascending=[False, True])
    if top_n is not None:
        records = records.head(top_n)
    records = records.reset_index(drop=True)

    return records
