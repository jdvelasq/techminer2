"""
Co-occurrence Matrix List
===============================================================================

>>> from techminer2 import *
>>> directory = "data/regtech/"

**Item selection by occurrence.**

>>> co_occ_matrix_list(
...    column='author_keywords',
...    row='authors',
...    min_occ=3,
...    directory=directory,
... )
                  row                          column  OCC
0      Arner DW 7:220                  regtech 70:462    6
1      Arner DW 7:220                  fintech 42:406    5
2    Buckley RP 6:217                  regtech 70:462    5
3      Arner DW 7:220     financial regulation 08:091    4
4    Buckley RP 6:217                  fintech 42:406    4
5   Zetzsche DA 4:092                  fintech 42:406    4
6   Zetzsche DA 4:092                  regtech 70:462    4
7   Barberis JN 4:146                  regtech 70:462    3
8     Brennan R 3:008           accountability 04:022    3
9     Brennan R 3:008  data protection officer 03:008    3
10    Brennan R 3:008                  regtech 70:462    3
11   Buckley RP 6:217     financial regulation 08:091    3
12       Ryan P 3:008           accountability 04:022    3
13       Ryan P 3:008  data protection officer 03:008    3
14       Ryan P 3:008                  regtech 70:462    3


>>> co_occ_matrix_list(
...    column='author_keywords',
...    min_occ=4,
...    directory=directory,
... )
                                         row             column  OCC
0                             regtech 70:462     regtech 70:462   70
1                             fintech 42:406     fintech 42:406   42
2                             fintech 42:406     regtech 70:462   42
3                             regtech 70:462     fintech 42:406   42
4                          blockchain 18:109  blockchain 18:109   18
..                                       ...                ...  ...
75                            regtech 70:462     suptech 04:003    4
76                         regulation 06:120     fintech 42:406    4
77  regulatory technologies (regtech) 12:047     regtech 70:462    4
78                            suptech 04:003     regtech 70:462    4
79                            suptech 04:003     suptech 04:003    4
<BLANKLINE>
[80 rows x 3 columns]


**Seleccition of top terms.**

>>> co_occ_matrix_list(
...    column='author_keywords',
...    row='authors',
...    top_n=5,
...    directory=directory,
... )
                  row                                    column  OCC
0      Arner DW 7:220                            regtech 70:462    6
1      Arner DW 7:220                            fintech 42:406    5
2    Buckley RP 6:217                            regtech 70:462    5
3    Buckley RP 6:217                            fintech 42:406    4
4   Zetzsche DA 4:092                            fintech 42:406    4
5   Zetzsche DA 4:092                            regtech 70:462    4
6   Barberis JN 4:146                            regtech 70:462    3
7     Brennan R 3:008                            regtech 70:462    3
8   Barberis JN 4:146                            fintech 42:406    2
9      Arner DW 7:220                         blockchain 18:109    1
10     Arner DW 7:220  regulatory technologies (regtech) 12:047    1
11  Barberis JN 4:146  regulatory technologies (regtech) 12:047    1
12   Buckley RP 6:217                         blockchain 18:109    1
13  Zetzsche DA 4:092                         blockchain 18:109    1


>>> co_occ_matrix_list(
...    column='author_keywords',
...    top_n=5,
...    directory=directory,
... )
                                         row  ... OCC
0                             regtech 70:462  ...  70
1                             fintech 42:406  ...  42
2                             fintech 42:406  ...  42
3                             regtech 70:462  ...  42
4                          blockchain 18:109  ...  18
5                          blockchain 18:109  ...  17
6                             regtech 70:462  ...  17
7                          blockchain 18:109  ...  14
8                             fintech 42:406  ...  14
9             artificial intelligence 13:065  ...  13
10  regulatory technologies (regtech) 12:047  ...  12
11            artificial intelligence 13:065  ...  10
12                            regtech 70:462  ...  10
13            artificial intelligence 13:065  ...   8
14                            fintech 42:406  ...   8
15                            regtech 70:462  ...   4
16  regulatory technologies (regtech) 12:047  ...   4
17                            fintech 42:406  ...   3
18  regulatory technologies (regtech) 12:047  ...   3
19            artificial intelligence 13:065  ...   2
20            artificial intelligence 13:065  ...   2
21                         blockchain 18:109  ...   2
22  regulatory technologies (regtech) 12:047  ...   2
<BLANKLINE>
[23 rows x 3 columns]


"""
import pandas as pd

from ._read_records import read_records
from .items2counters import items2counters
from .load_stopwords import load_stopwords


def co_occ_matrix_list(
    column,
    row=None,
    top_n=None,
    min_occ=None,
    max_occ=None,
    directory="./",
    database="documents",
):
    """Creates a list of the cells of a co-occurrence matrix."""

    if row is None:
        row = column

    matrix_list = _create_matrix_list(column, row, directory, database)
    matrix_list = _remove_stopwords(directory, matrix_list)
    matrix_list = _remove_terms_by_occ(min_occ, max_occ, matrix_list)

    matrix_list = _add_counters_to_items(
        column,
        "column",
        directory,
        database,
        matrix_list,
    )
    matrix_list = _add_counters_to_items(
        row,
        "row",
        directory,
        database,
        matrix_list,
    )

    matrix_list = _select_top_n_items(top_n, matrix_list, "column")
    matrix_list = _select_top_n_items(top_n, matrix_list, "row")

    matrix_list = matrix_list.reset_index(drop=True)

    return matrix_list


def _select_top_n_items(top_n, matrix_list, column):

    table = pd.DataFrame({"term": matrix_list[column].drop_duplicates()})
    table["ranking"] = table.term.str.split()
    table["ranking"] = table["ranking"].map(lambda x: x[-1])
    table["name"] = table.term.str.split()
    table["name"] = table["name"].map(lambda x: x[:-1])
    table["name"] = table["name"].str.join(" ")
    table = table.sort_values(["ranking", "name"], ascending=[False, True])
    table = table.head(top_n)
    terms = table.term.tolist()

    matrix_list = matrix_list[matrix_list[column].isin(terms)]
    return matrix_list


def _add_counters_to_items(column, name, directory, database, matrix_list):
    new_column_names = items2counters(
        column=column,
        directory=directory,
        database=database,
        use_filter=True,
    )
    matrix_list[name] = matrix_list[name].map(new_column_names)
    return matrix_list


def _remove_terms_by_occ(min_occ, max_occ, matrix_list):
    if min_occ is not None:
        matrix_list = matrix_list[matrix_list.OCC >= min_occ]
    if max_occ is not None:
        matrix_list = matrix_list[matrix_list.OCC <= max_occ]
    matrix_list = matrix_list.sort_values(
        by=["OCC", "row", "column"], ascending=[False, True, True]
    )
    return matrix_list


def _remove_stopwords(directory, matrix_list):
    stopwords = load_stopwords(directory)
    matrix_list = matrix_list[~matrix_list["column"].isin(stopwords)]
    matrix_list = matrix_list[~matrix_list["row"].isin(stopwords)]
    return matrix_list


def _create_matrix_list(column, row, directory, database):

    records = read_records(directory, database=database, use_filter=True)

    matrix_list = records[[column]].copy()
    matrix_list = matrix_list.rename(columns={column: "column"})
    matrix_list = matrix_list.assign(row=records[[row]])

    for name in ["column", "row"]:
        matrix_list[name] = matrix_list[name].str.split(";")
        matrix_list = matrix_list.explode(name)
        matrix_list[name] = matrix_list[name].str.strip()

    matrix_list["OCC"] = 1
    matrix_list = matrix_list.groupby(["row", "column"], as_index=False).aggregate(
        "sum"
    )

    return matrix_list
