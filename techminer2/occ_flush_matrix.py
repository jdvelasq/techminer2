"""
OCC Flush Matrix
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"

>>> occ_flush_matrix(
...    column='author_keywords', 
...    by='authors',
...    min_occ=3,
...    directory=directory,
... )
            author_keywords      authors  OCC
0                   regtech     Arner DW    6
1                   fintech     Arner DW    5
2                   regtech   Buckley RP    5
3      financial regulation     Arner DW    4
4                   fintech   Buckley RP    4
5                   fintech  Zetzsche DA    4
6                   regtech  Zetzsche DA    4
7                   account    Brennan R    3
8                   account       Ryan P    3
9   data protection officer    Brennan R    3
10  data protection officer       Ryan P    3
11     financial regulation   Buckley RP    3
12                  regtech  Barberis JN    3
13                  regtech    Brennan R    3
14                  regtech       Ryan P    3

"""

from ._read_records import read_records


def occ_flush_matrix(
    column,
    by,
    min_occ=None,
    max_occ=None,
    directory="./",
):

    records = read_records(directory)

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

    return records
