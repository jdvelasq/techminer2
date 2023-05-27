"""
Terms by Year --- ChatGPT
===============================================================================


>>> root_dir = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> r = vantagepoint.analyze.terms_by_year(
...    criterion='author_keywords',
...    topics_length=10,
...    root_dir=root_dir,
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
Analyze the table below which contains the  occurrences by year for the \
author_keywords. Identify any notable patterns, trends, or outliers in the \
data, and discuss their implications for the research field. Be sure to \
provide a concise summary of your findings in no more than 150 words.
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
...    root_dir=root_dir,
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
Analyze the table below which contains the cumulative occurrences by year for \
the author_keywords. Identify any notable patterns, trends, or outliers in \
the data, and discuss their implications for the research field. Be sure to \
provide a concise summary of your findings in no more than 150 words.
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

# noga: E501 W291

"""

from ... import techminer
from ...add_counters import add_counters_to_axis
from ...classes import TermsByYear
from ...custom_topics import generate_custom_topics
from ...sort_indicators import sort_indicators_by_metric
from ...techminer.indicators.indicators_by_topic import indicators_by_topic


def terms_by_year(
    criterion,
    topics_length=50,
    topic_min_occ=None,
    topic_max_occ=None,
    topic_min_citations=None,
    topic_max_citations=None,
    custom_topics=None,
    root_dir="./",
    database="documents",
    start_year=None,
    end_year=None,
    cumulative=False,
    **filters,
):
    """Computes a table with the number of occurrences of each term by year."""

    def generate_prompt(obj):
        return (
            f"Analyze the table below which contains the "
            f"{'cumulative' if obj.cumulative_ else ''} occurrences by year "
            f"for the {obj.criterion_for_rows_}. Identify any notable "
            "patterns, trends, or outliers in the data, and discuss their "
            "implications for the research field. Be sure to provide a "
            "concise summary of your findings in no more than 150 words."
            f"\n\n{obj.table_.to_markdown()}\n\n"
        )

    #
    # Main:
    #

    descriptors_by_year = techminer.indicators.topics_occ_by_year(
        criterion=criterion,
        root_dir=root_dir,
        cumulative=cumulative,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    if custom_topics is None:
        indicators = indicators_by_topic(
            criterion=criterion,
            root_dir=root_dir,
            database=database,
            start_year=start_year,
            end_year=end_year,
            **filters,
        )

        indicators = sort_indicators_by_metric(indicators, metric="OCC")

        custom_topics = generate_custom_topics(
            indicators=indicators,
            topics_length=topics_length,
            topic_min_occ=topic_min_occ,
            topic_max_occ=topic_max_occ,
            topic_min_citations=topic_min_citations,
            topic_max_citations=topic_max_citations,
        )

    descriptors_by_year = descriptors_by_year[
        descriptors_by_year.index.isin(custom_topics)
    ]

    descriptors_by_year = descriptors_by_year.loc[custom_topics, :]

    descriptors_by_year = add_counters_to_axis(
        descriptors_by_year,
        axis=0,
        criterion=criterion,
        root_dir=root_dir,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    obj = TermsByYear()
    obj.metric_ = "OCC"
    obj.criterion_for_columns_ = "years"
    obj.criterion_for_rows_ = criterion
    obj.cumulative_ = cumulative
    obj.table_ = descriptors_by_year
    obj.prompt_ = generate_prompt(obj)

    return obj
