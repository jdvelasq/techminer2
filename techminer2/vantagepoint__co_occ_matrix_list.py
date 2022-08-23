"""
Co-occurrence Matrix List
===============================================================================


>>> directory = "data/regtech/"

**Item selection by occurrence.**

>>> from techminer2 import vantagepoint__co_occ_matrix_list
>>> vantagepoint__co_occ_matrix_list(
...    criterion='author_keywords',
...    topic_min_occ=4,
...    directory=directory,
... )
                row                          column  OCC
0    regtech 69:461                  regtech 69:461   69
1    regtech 69:461                  fintech 42:406   42
2    regtech 69:461               blockchain 18:109   17
3    regtech 69:461  artificial intelligence 13:065   10
4    regtech 69:461    regulatory technology 12:047    4
..              ...                             ...  ...
243  banking 04:001               regulation 06:120    2
244  banking 04:001         machine learning 06:013    1
245  banking 04:001               innovation 04:029    1
246  banking 04:001                insurtech 04:005    1
247  banking 04:001                  banking 04:001    4
<BLANKLINE>
[248 rows x 3 columns]


**Seleccition of top terms.**

>>> from techminer2 import vantagepoint__co_occ_matrix_list
>>> vantagepoint__co_occ_matrix_list(
...    criterion='author_keywords',
...    topics_length=5,
...    directory=directory,
... )
                               row                          column  OCC
0                   regtech 69:461                  regtech 69:461   69
1                   regtech 69:461                  fintech 42:406   42
2                   regtech 69:461               blockchain 18:109   17
3                   regtech 69:461  artificial intelligence 13:065   10
4                   regtech 69:461    regulatory technology 12:047    4
5                   fintech 42:406                  regtech 69:461   42
6                   fintech 42:406                  fintech 42:406   42
7                   fintech 42:406               blockchain 18:109   14
8                   fintech 42:406  artificial intelligence 13:065    8
9                   fintech 42:406    regulatory technology 12:047    3
10               blockchain 18:109                  regtech 69:461   17
11               blockchain 18:109                  fintech 42:406   14
12               blockchain 18:109               blockchain 18:109   18
13               blockchain 18:109  artificial intelligence 13:065    2
14  artificial intelligence 13:065                  regtech 69:461   10
15  artificial intelligence 13:065                  fintech 42:406    8
16  artificial intelligence 13:065               blockchain 18:109    2
17  artificial intelligence 13:065  artificial intelligence 13:065   13
18  artificial intelligence 13:065    regulatory technology 12:047    2
19    regulatory technology 12:047                  regtech 69:461    4
20    regulatory technology 12:047                  fintech 42:406    3
21    regulatory technology 12:047  artificial intelligence 13:065    2
22    regulatory technology 12:047    regulatory technology 12:047   12


"""
from .tm2__indicators_by_topic import tm2__indicators_by_topic
from ._items2counters import items2counters
from ._load_stopwords import load_stopwords
from ._read_records import read_records


def vantagepoint__co_occ_matrix_list(
    criterion,
    topics_length=None,
    topic_min_occ=None,
    topic_min_citations=None,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Creates a list of the cells of a co-occurrence matrix."""

    matrix_list = _create_matrix_list(
        criterion=criterion,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    matrix_list = _remove_stopwords(
        directory,
        matrix_list,
    )

    matrix_list = _select_topics_by_occ_and_citations_and_topic_length(
        matrix_list=matrix_list,
        topic_min_occ=topic_min_occ,
        topic_min_citations=topic_min_citations,
        topics_length=topics_length,
        criterion=criterion,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    for column_name in ["row", "column"]:

        matrix_list = _add_counters_to_items(
            matrix_list=matrix_list,
            column_name=column_name,
            criterion=criterion,
            directory=directory,
            database=database,
            start_year=start_year,
            end_year=end_year,
            **filters,
        )

    matrix_list = _sort_matrix_list(matrix_list)

    return matrix_list


def _sort_matrix_list(matrix_list):

    matrix_list = matrix_list.copy()

    for col in ["row", "column"]:

        col_upper = col.upper()
        matrix_list[col_upper] = matrix_list[col]
        matrix_list[col_upper] = matrix_list[col_upper].str.split()
        matrix_list[col_upper] = matrix_list[col_upper].map(lambda x: x[-1])

    matrix_list = matrix_list.sort_values(
        ["ROW", "row", "COLUMN", "column"], ascending=[False, True, False, True]
    )

    matrix_list = matrix_list.drop(columns=["ROW", "COLUMN"])
    matrix_list = matrix_list.reset_index(drop=True)

    return matrix_list


def _add_counters_to_items(
    matrix_list,
    column_name,
    criterion,
    directory,
    database,
    start_year,
    end_year,
    **filters,
):
    new_column_names = items2counters(
        column=criterion,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )
    matrix_list[column_name] = matrix_list[column_name].map(new_column_names)
    return matrix_list


def _select_topics_by_occ_and_citations_and_topic_length(
    matrix_list,
    topic_min_occ,
    topic_min_citations,
    topics_length,
    criterion,
    directory,
    database,
    start_year,
    end_year,
    **filters,
):
    indicators = tm2__indicators_by_topic(
        criterion=criterion,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    if topic_min_occ is not None:
        indicators = indicators[indicators.OCC >= topic_min_occ]
    if topic_min_citations is not None:
        indicators = indicators[indicators.global_citations >= topic_min_citations]

    indicators = indicators.sort_values(
        ["OCC", "global_citations", "local_citations"],
        ascending=[False, False, False],
    )

    if topics_length is not None:
        indicators = indicators.head(topics_length)

    topics = indicators.index.to_list()

    matrix_list = matrix_list[matrix_list.column.isin(topics)]
    matrix_list = matrix_list[matrix_list.row.isin(topics)]

    return matrix_list


def _remove_stopwords(directory, matrix_list):
    stopwords = load_stopwords(directory)
    matrix_list = matrix_list[~matrix_list["column"].isin(stopwords)]
    matrix_list = matrix_list[~matrix_list["row"].isin(stopwords)]
    return matrix_list


def _create_matrix_list(
    criterion,
    directory,
    database,
    start_year,
    end_year,
    **filters,
):

    records = read_records(
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    matrix_list = records[[criterion]].copy()
    matrix_list = matrix_list.rename(columns={criterion: "column"})
    matrix_list = matrix_list.assign(row=records[[criterion]])

    for name in ["column", "row"]:
        matrix_list[name] = matrix_list[name].str.split(";")
        matrix_list = matrix_list.explode(name)
        matrix_list[name] = matrix_list[name].str.strip()

    matrix_list["OCC"] = 1
    matrix_list = matrix_list.groupby(["row", "column"], as_index=False).aggregate(
        "sum"
    )

    return matrix_list
