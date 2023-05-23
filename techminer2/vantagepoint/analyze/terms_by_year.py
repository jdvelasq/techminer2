"""
Terms by Year (GPT)
===============================================================================


>>> directory = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> r = vantagepoint.analyze.terms_by_year(
...    criterion='author_keywords',
...    topics_length=10,
...    directory=directory,
... )
>>> r.table_
year                            2017  2018  2019  2020  2021  2022  2023
author_keywords                                                         
regtech 28:329                     2     3     4     8     3     6     2
fintech 12:249                     0     2     4     3     1     2     0
regulatory technology 07:037       0     0     0     2     3     2     0
compliance 07:030                  0     0     1     3     1     1     1
regulation 05:164                  0     2     0     1     1     1     0
financial services 04:168          1     1     0     1     0     1     0
financial regulation 04:035        1     0     0     1     0     2     0
artificial intelligence 04:023     0     0     1     2     0     1     0
anti-money laundering 03:021       0     0     0     1     2     0     0
risk management 03:014             0     1     0     1     0     1     0


>>> print(r.prompt_)
Analyze the table below which contains the  occurrences by year for the author_keywords. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| author_keywords                |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:-------------------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| regtech 28:329                 |      2 |      3 |      4 |      8 |      3 |      6 |      2 |
| fintech 12:249                 |      0 |      2 |      4 |      3 |      1 |      2 |      0 |
| regulatory technology 07:037   |      0 |      0 |      0 |      2 |      3 |      2 |      0 |
| compliance 07:030              |      0 |      0 |      1 |      3 |      1 |      1 |      1 |
| regulation 05:164              |      0 |      2 |      0 |      1 |      1 |      1 |      0 |
| financial services 04:168      |      1 |      1 |      0 |      1 |      0 |      1 |      0 |
| financial regulation 04:035    |      1 |      0 |      0 |      1 |      0 |      2 |      0 |
| artificial intelligence 04:023 |      0 |      0 |      1 |      2 |      0 |      1 |      0 |
| anti-money laundering 03:021   |      0 |      0 |      0 |      1 |      2 |      0 |      0 |
| risk management 03:014         |      0 |      1 |      0 |      1 |      0 |      1 |      0 |
<BLANKLINE>
<BLANKLINE>


>>> r = vantagepoint.analyze.terms_by_year(
...    criterion='author_keywords',
...    topics_length=10,
...    directory=directory,
...    cumulative=True,
... )
>>> r.table_
year                            2017  2018  2019  2020  2021  2022  2023
author_keywords                                                         
regtech 28:329                     2     5     9    17    20    26    28
fintech 12:249                     0     2     6     9    10    12    12
regulatory technology 07:037       0     0     0     2     5     7     7
compliance 07:030                  0     0     1     4     5     6     7
regulation 05:164                  0     2     2     3     4     5     5
financial services 04:168          1     2     2     3     3     4     4
financial regulation 04:035        1     1     1     2     2     4     4
artificial intelligence 04:023     0     0     1     3     3     4     4
anti-money laundering 03:021       0     0     0     1     3     3     3
risk management 03:014             0     1     1     2     2     3     3


>>> print(r.prompt_)
Analyze the table below which contains the cumulative occurrences by year for the author_keywords. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| author_keywords                |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:-------------------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| regtech 28:329                 |      2 |      5 |      9 |     17 |     20 |     26 |     28 |
| fintech 12:249                 |      0 |      2 |      6 |      9 |     10 |     12 |     12 |
| regulatory technology 07:037   |      0 |      0 |      0 |      2 |      5 |      7 |      7 |
| compliance 07:030              |      0 |      0 |      1 |      4 |      5 |      6 |      7 |
| regulation 05:164              |      0 |      2 |      2 |      3 |      4 |      5 |      5 |
| financial services 04:168      |      1 |      2 |      2 |      3 |      3 |      4 |      4 |
| financial regulation 04:035    |      1 |      1 |      1 |      2 |      2 |      4 |      4 |
| artificial intelligence 04:023 |      0 |      0 |      1 |      3 |      3 |      4 |      4 |
| anti-money laundering 03:021   |      0 |      0 |      0 |      1 |      3 |      3 |      3 |
| risk management 03:014         |      0 |      1 |      1 |      2 |      2 |      3 |      3 |
<BLANKLINE>
<BLANKLINE>


"""
from dataclasses import dataclass

from ... import chatgpt
from ...add_counters_to_items_in_table_column import (
    add_counters_to_items_in_table_column,
)
from ...techminer.indicators.indicators_by_topic import indicators_by_topic
from ...techminer.indicators.indicators_by_topic_per_year import (
    indicators_by_topic_per_year,
)


@dataclass(init=False)
class _TableResult:
    table_: None
    prompt_: None
    metric_: None
    cumulative_: None
    criterion_for_columns_: None
    criterion_for_rows_: None


def terms_by_year(
    criterion,
    topics_length=50,
    topic_min_occ=None,
    topic_max_occ=None,
    topic_min_citations=None,
    topic_max_citations=None,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    cumulative=False,
    **filters,
):
    """Computes the number of terms by year."""

    results = _TableResult()
    results.metric_ = "OCC"
    results.criterion_for_columns_ = "years"
    results.criterion_for_rows_ = criterion
    results.cumulative_ = cumulative

    indicators_by_year = indicators_by_topic_per_year(
        criterion=criterion,
        directory=directory,
        database="documents",
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    indicators_by_year = indicators_by_year[["OCC"]]
    indicators_by_year = indicators_by_year.reset_index()

    indicators = indicators_by_topic(
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
    if topic_max_occ is not None:
        custom_topics = custom_topics[custom_topics["OCC"] <= topic_max_occ]
    if topic_min_citations is not None:
        custom_topics = custom_topics[
            custom_topics["global_citations"] >= topic_min_citations
        ]
    if topic_max_citations is not None:
        custom_topics = custom_topics[
            custom_topics["global_citations"] <= topic_max_citations
        ]
    custom_topics = custom_topics.index.copy()
    custom_topics = custom_topics[:topics_length]

    indicators = indicators.loc[custom_topics, :]

    indicators_by_year = indicators_by_year[
        indicators_by_year[criterion].isin(indicators.index)
    ]

    max_year = indicators_by_year["year"].max()
    min_year = indicators_by_year["year"].min()

    indicators_by_year = indicators_by_year.pivot(
        index=criterion, columns="year", values="OCC"
    )
    indicators_by_year = indicators_by_year.fillna(0)
    indicators_by_year = indicators_by_year.astype(int)

    indicators_by_year = indicators_by_year.loc[custom_topics, :]

    indicators_by_year = indicators_by_year.reset_index()
    indicators_by_year = add_counters_to_items_in_table_column(
        column=criterion,
        name=criterion,
        directory=directory,
        database=database,
        table=indicators_by_year,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )
    indicators_by_year = indicators_by_year.set_index(criterion)

    for year in range(min_year, max_year + 1):
        if year not in indicators_by_year.columns:
            indicators_by_year[year] = 0

    indicators_by_year = indicators_by_year.sort_index(ascending=True, axis=1)

    if cumulative:
        indicators_by_year = indicators_by_year.cumsum(axis=1)

    results.table_ = indicators_by_year

    results.prompt_ = chatgpt.generate_prompt_for_terms_by_year_matrix(results)

    return results
