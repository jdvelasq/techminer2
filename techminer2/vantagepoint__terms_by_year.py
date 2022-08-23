"""
Terms by Year
===============================================================================


>>> directory = "data/regtech/"

>>> from techminer2 import vantagepoint__terms_by_year
>>> vantagepoint__terms_by_year(
...    criterion='author_keywords',
...    topics_length=10,
...    directory=directory,
... ).head(20)
                   author_keywords  year  OCC  cum_OCC
0   artificial intelligence 13:065  2018    2        2
1   artificial intelligence 13:065  2019    1        3
2   artificial intelligence 13:065  2020    5        8
3   artificial intelligence 13:065  2021    3       11
4   artificial intelligence 13:065  2022    2       13
5                blockchain 18:109  2017    2        2
6                blockchain 18:109  2018    2        4
7                blockchain 18:109  2019    5        9
8                blockchain 18:109  2020    4       13
9                blockchain 18:109  2021    4       17
10               blockchain 18:109  2022    1       18
11               compliance 12:020  2018    2        2
12               compliance 12:020  2019    3        5
13               compliance 12:020  2020    5       10
14               compliance 12:020  2021    2       12
15     financial regulation 08:091  2016    1        1
16     financial regulation 08:091  2017    1        2
17     financial regulation 08:091  2018    1        3
18     financial regulation 08:091  2019    1        4
19     financial regulation 08:091  2020    3        7

"""
from .tm2__indicators_by_topic import tm2__indicators_by_topic
from .tm2__indicators_by_topic_per_year import tm2__indicators_by_topic_per_year
from .vantagepoint__co_occ_matrix_list import _add_counters_to_items


def vantagepoint__terms_by_year(
    criterion,
    topics_length=50,
    topic_min_occ=None,
    topic_min_citations=None,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Computes the number of terms by year."""

    indicators_by_year = tm2__indicators_by_topic_per_year(
        criterion=criterion,
        directory=directory,
        database="documents",
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    indicators_by_year = indicators_by_year[["OCC", "cum_OCC"]]
    indicators_by_year = indicators_by_year.reset_index()

    ###

    indicators = tm2__indicators_by_topic(
        criterion=criterion,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    indicators = indicators.sort_values(
        ["OCC", "global_citations", "local_citations"],
        ascending=[False, False, False],
    )

    custom_topics = indicators.copy()
    if topic_min_occ is not None:
        custom_topics = custom_topics[custom_topics["OCC"] >= topic_min_occ]
    if topic_min_citations is not None:
        custom_topics = custom_topics[
            custom_topics["global_citations"] >= topic_min_citations
        ]
    custom_topics = custom_topics.index.copy()
    custom_topics = custom_topics[:topics_length]

    indicators = indicators.loc[custom_topics, :]

    indicators_by_year = indicators_by_year[
        indicators_by_year[criterion].isin(indicators.index)
    ]
    ###

    indicators_by_year = _add_counters_to_items(
        matrix_list=indicators_by_year,
        column_name=criterion,
        criterion=criterion,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    indicators_by_year = indicators_by_year.sort_values(
        [criterion, "year"], ascending=[True, True]
    )
    indicators_by_year = indicators_by_year.reset_index(drop=True)
    return indicators_by_year
