"""
Co-occurrence Matrix List
===============================================================================


>>> directory = "data/regtech/"

**Item selection by occurrence.**

>>> from techminer2 import vantagepoint
>>> vantagepoint.analyze.matrix.co_occ_matrix_list(
...    criterion='author_keywords',
...    topic_min_occ=4,
...    directory=directory,
... )
                               row                          column  OCC
0                   regtech 28:329                  regtech 28:329   28
1                   regtech 28:329                  fintech 12:249   12
2                   regtech 28:329    regulatory technology 07:037    2
3                   regtech 28:329               compliance 07:030    7
4                   regtech 28:329               regulation 05:164    4
5                   regtech 28:329       financial services 04:168    3
6                   regtech 28:329     financial regulation 04:035    2
7                   regtech 28:329  artificial intelligence 04:023    2
8                   fintech 12:249                  regtech 28:329   12
9                   fintech 12:249                  fintech 12:249   12
10                  fintech 12:249    regulatory technology 07:037    1
11                  fintech 12:249               compliance 07:030    2
12                  fintech 12:249               regulation 05:164    4
13                  fintech 12:249       financial services 04:168    2
14                  fintech 12:249     financial regulation 04:035    1
15                  fintech 12:249  artificial intelligence 04:023    1
16    regulatory technology 07:037                  regtech 28:329    2
17    regulatory technology 07:037                  fintech 12:249    1
18    regulatory technology 07:037    regulatory technology 07:037    7
19    regulatory technology 07:037               compliance 07:030    1
20    regulatory technology 07:037               regulation 05:164    1
21    regulatory technology 07:037  artificial intelligence 04:023    1
22               compliance 07:030                  regtech 28:329    7
23               compliance 07:030                  fintech 12:249    2
24               compliance 07:030    regulatory technology 07:037    1
25               compliance 07:030               compliance 07:030    7
26               compliance 07:030               regulation 05:164    1
27               compliance 07:030  artificial intelligence 04:023    1
28               regulation 05:164                  regtech 28:329    4
29               regulation 05:164                  fintech 12:249    4
30               regulation 05:164    regulatory technology 07:037    1
31               regulation 05:164               compliance 07:030    1
32               regulation 05:164               regulation 05:164    5
33               regulation 05:164       financial services 04:168    1
34       financial services 04:168                  regtech 28:329    3
35       financial services 04:168                  fintech 12:249    2
36       financial services 04:168               regulation 05:164    1
37       financial services 04:168       financial services 04:168    4
38       financial services 04:168     financial regulation 04:035    2
39     financial regulation 04:035                  regtech 28:329    2
40     financial regulation 04:035                  fintech 12:249    1
41     financial regulation 04:035       financial services 04:168    2
42     financial regulation 04:035     financial regulation 04:035    4
43  artificial intelligence 04:023                  regtech 28:329    2
44  artificial intelligence 04:023                  fintech 12:249    1
45  artificial intelligence 04:023    regulatory technology 07:037    1
46  artificial intelligence 04:023               compliance 07:030    1
47  artificial intelligence 04:023  artificial intelligence 04:023    4



**Seleccition of top terms.**

>>> from techminer2 import vantagepoint
>>> vantagepoint.analyze.matrix.co_occ_matrix_list(
...    criterion='author_keywords',
...    topics_length=5,
...    directory=directory,
... )
                             row                        column  OCC
0                 regtech 28:329                regtech 28:329   28
1                 regtech 28:329                fintech 12:249   12
2                 regtech 28:329  regulatory technology 07:037    2
3                 regtech 28:329             compliance 07:030    7
4                 regtech 28:329             regulation 05:164    4
5                 fintech 12:249                regtech 28:329   12
6                 fintech 12:249                fintech 12:249   12
7                 fintech 12:249  regulatory technology 07:037    1
8                 fintech 12:249             compliance 07:030    2
9                 fintech 12:249             regulation 05:164    4
10  regulatory technology 07:037                regtech 28:329    2
11  regulatory technology 07:037                fintech 12:249    1
12  regulatory technology 07:037  regulatory technology 07:037    7
13  regulatory technology 07:037             compliance 07:030    1
14  regulatory technology 07:037             regulation 05:164    1
15             compliance 07:030                regtech 28:329    7
16             compliance 07:030                fintech 12:249    2
17             compliance 07:030  regulatory technology 07:037    1
18             compliance 07:030             compliance 07:030    7
19             compliance 07:030             regulation 05:164    1
20             regulation 05:164                regtech 28:329    4
21             regulation 05:164                fintech 12:249    4
22             regulation 05:164  regulatory technology 07:037    1
23             regulation 05:164             compliance 07:030    1
24             regulation 05:164             regulation 05:164    5


"""
from ...._items2counters import items2counters
from ...._load_stopwords import load_stopwords
from ...._read_records import read_records
from ....techminer.indicators.tm2__indicators_by_topic import tm2__indicators_by_topic


def co_occ_matrix_list(
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
