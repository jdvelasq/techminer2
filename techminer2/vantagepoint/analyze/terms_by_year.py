"""
Terms by Year
===============================================================================


>>> directory = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> vantagepoint.analyze.terms_by_year(
...    criterion='author_keywords',
...    topics_length=10,
...    directory=directory,
... ).head(20)
                   author_keywords  year  OCC  cum_OCC
0     anti-money laundering 03:021  2020    1        1
1     anti-money laundering 03:021  2021    2        3
2   artificial intelligence 04:023  2019    1        1
3   artificial intelligence 04:023  2020    2        3
4   artificial intelligence 04:023  2022    1        4
5                compliance 07:030  2019    1        1
6                compliance 07:030  2020    3        4
7                compliance 07:030  2021    1        5
8                compliance 07:030  2022    1        6
9                compliance 07:030  2023    1        7
10     financial regulation 04:035  2017    1        1
11     financial regulation 04:035  2020    1        2
12     financial regulation 04:035  2022    2        4
13       financial services 04:168  2017    1        1
14       financial services 04:168  2018    1        2
15       financial services 04:168  2020    1        3
16       financial services 04:168  2022    1        4
17                  fintech 12:249  2018    2        2
18                  fintech 12:249  2019    4        6
19                  fintech 12:249  2020    3        9

"""
from ...tm2__indicators_by_topic import tm2__indicators_by_topic
from ...tm2__indicators_by_topic_per_year import tm2__indicators_by_topic_per_year
from ...vantagepoint__co_occ_matrix_list import _add_counters_to_items


def terms_by_year(
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
