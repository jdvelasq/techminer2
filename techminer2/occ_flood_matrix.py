"""
OCC Flood Matrix
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"

>>> occ_flood_matrix(
...    column='author_keywords', 
...    by='authors',
...    min_occ=3,
...    directory=directory,
... )
                   author_keywords            authors  OCC
0                   regtech 70:462     Arner DW 7:220    6
1                   fintech 42:406     Arner DW 7:220    5
2                   regtech 70:462   Buckley RP 6:217    5
3      financial regulation 08:091     Arner DW 7:220    4
4                   fintech 42:406   Buckley RP 6:217    4
5                   fintech 42:406  Zetzsche DA 4:092    4
6                   regtech 70:462  Zetzsche DA 4:092    4
7                   account 04:022    Brennan R 3:008    3
8                   account 04:022       Ryan P 3:008    3
9   data protection officer 03:008    Brennan R 3:008    3
10  data protection officer 03:008       Ryan P 3:008    3
11     financial regulation 08:091   Buckley RP 6:217    3
12                  regtech 70:462  Barberis JN 4:146    3
13                  regtech 70:462    Brennan R 3:008    3
14                  regtech 70:462       Ryan P 3:008    3


"""

from ._read_records import read_records
from .items2counters import items2counters
from .load_stopwords import load_stopwords


def occ_flood_matrix(
    column,
    by,
    min_occ=None,
    max_occ=None,
    directory="./",
    database="documents",
):
    """Craates a flooding occurrence matrix."""

    records = read_records(directory, database=database, use_filter=True)

    records = records[[column, by]]

    records[column] = records[column].str.split(";")
    records = records.explode(column)
    records[column] = records[column].str.strip()

    records[by] = records[by].str.split(";")
    records = records.explode(by)
    records[by] = records[by].str.strip()

    records["OCC"] = 1
    records = records.groupby([column, by], as_index=False).aggregate("sum")

    if min_occ is not None:
        records = records[records.OCC >= min_occ]

    if max_occ is not None:
        records = records[records.OCC <= max_occ]

    records = records.sort_values(by=["OCC", column, by], ascending=[False, True, True])
    records = records.reset_index(drop=True)

    stopwords = load_stopwords(directory)
    records = records[~records[column].isin(stopwords)]
    records = records[~records[by].isin(stopwords)]

    new_col_names = items2counters(
        column=column,
        directory=directory,
        database=database,
        use_filter=True,
    )
    records[column] = records[column].map(new_col_names)

    new_by_names = items2counters(
        column=by,
        directory=directory,
        database=database,
        use_filter=True,
    )
    records[by] = records[by].map(new_by_names)

    return records
