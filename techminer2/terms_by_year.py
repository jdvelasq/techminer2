"""
Terms by year
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"

>>> terms_by_year(
...    column='author_keywords',
...    top_n=10,
...    directory=directory,
... ).head(20)
                   author_keywords  year  OCC
0   artificial intelligence 13:065  2018    2
1   artificial intelligence 13:065  2019    1
2   artificial intelligence 13:065  2020    5
3   artificial intelligence 13:065  2021    3
4   artificial intelligence 13:065  2022    2
5                blockchain 18:109  2017    2
6                blockchain 18:109  2018    2
7                blockchain 18:109  2019    5
8                blockchain 18:109  2020    4
9                blockchain 18:109  2021    4
10               blockchain 18:109  2022    1
11               compliance 12:020  2018    2
12               compliance 12:020  2019    3
13               compliance 12:020  2020    5
14               compliance 12:020  2021    2
15     financial regulation 08:091  2016    1
16     financial regulation 08:091  2017    1
17     financial regulation 08:091  2018    1
18     financial regulation 08:091  2019    1
19     financial regulation 08:091  2020    3

"""
from .co_occ_matrix_list import _add_counters_to_items, _select_top_n_items
from .column_indicators_by_year import column_indicators_by_year


def terms_by_year(
    column,
    top_n=50,
    directory="./",
    database="documents",
):
    """Computes the number of terms by year."""

    indicators_by_year = column_indicators_by_year(
        column=column, directory=directory, database="documents", use_filter=True
    )

    indicators_by_year = indicators_by_year[["num_documents"]]
    indicators_by_year = indicators_by_year.reset_index()
    indicators_by_year = _add_counters_to_items(
        column, column, directory, database, indicators_by_year
    )
    indicators_by_year = indicators_by_year.rename(columns={"num_documents": "OCC"})
    indicators_by_year = _select_top_n_items(top_n, indicators_by_year, column)

    indicators_by_year = indicators_by_year.sort_values(
        [column, "year"], ascending=[True, True]
    )
    indicators_by_year = indicators_by_year.reset_index(drop=True)
    return indicators_by_year
