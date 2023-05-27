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


"""
from ...add_counters import add_counters
from ...classes import TermsByYear
from ...custom_topics import generate_custom_topics
from ...sort_indicators import sort_indicators_by_metric
from ...techminer.indicators.indicators_by_topic import indicators_by_topic
from ...techminer.indicators.indicators_by_topic_per_year import (
    indicators_by_topic_per_year,
)


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
    """Computes a table with the number of occurrences of each term by year.

    Parameters
    ----------
    criterion : str
        Criterion to be used to extract the terms.

    topics_length : int, optional
        Number of terms to be included in the analysis. The default is 50.

    topic_min_occ : int, optional
        Minimum number of occurrences of the terms to be included in the analysis. The default is None.

    topic_max_occ : int, optional
        Maximum number of occurrences of the terms to be included in the analysis. The default is None.

    topic_min_citations : int, optional
        Minimum number of citations of the terms to be included in the analysis. The default is None.

    topic_max_citations : int, optional
        Maximum number of citations of the terms to be included in the analysis. The default is None.

    custom_topics : list of str, optional
        List of custom topics. The default is None.

    root_dir : str, optional
        Root directory. The default is './'.

    database : str, optional
        Database to be used. The default is 'documents'.

    start_year : int, optional
        Start year. The default is None.

    end_year : int, optional
        End year. The default is None.

    cumulative : bool, optional
        If True, the cumulative number of occurrences is computed. The default is False.

    Returns
    -------
    TermsByYear








    """

    def obtain_custom_topics(
        criterion,
        topics_length,
        topic_min_occ,
        topic_max_occ,
        topic_min_citations,
        topic_max_citations,
        root_dir,
        database,
        start_year,
        end_year,
        **filters,
    ):
        indicators = indicators_by_topic(
            criterion=criterion,
            root_dir=root_dir,
            database=database,
            start_year=start_year,
            end_year=end_year,
            **filters,
        )

        indicators = sort_indicators_by_metric(indicators, "OCC")

        custom_topics = generate_custom_topics(
            indicators=indicators,
            topics_length=topics_length,
            topic_min_occ=topic_min_occ,
            topic_max_occ=topic_max_occ,
            topic_min_citations=topic_min_citations,
            topic_max_citations=topic_max_citations,
        )

        indicators = indicators[indicators.index.isin(custom_topics)]
        custom_topics = indicators.index.tolist()

        return custom_topics

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

    def pivot_table(indicators_by_year):
        indicators_by_year = indicators_by_year.copy()

        max_year = indicators_by_year["year"].max()
        min_year = indicators_by_year["year"].min()

        indicators_by_year = indicators_by_year.pivot(
            index=criterion, columns="year", values="OCC"
        )
        indicators_by_year = indicators_by_year.fillna(0)
        indicators_by_year = indicators_by_year.astype(int)

        for year in range(min_year, max_year + 1):
            if year not in indicators_by_year.columns:
                indicators_by_year[year] = 0

        return indicators_by_year

    #
    # Main:
    #

    indicators_by_year = indicators_by_topic_per_year(
        criterion=criterion,
        root_dir=root_dir,
        database="documents",
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    indicators_by_year = indicators_by_year[["OCC"]]
    indicators_by_year = indicators_by_year.reset_index()

    if custom_topics is None:
        custom_topics = obtain_custom_topics(
            criterion=criterion,
            topics_length=topics_length,
            topic_min_occ=topic_min_occ,
            topic_max_occ=topic_max_occ,
            topic_min_citations=topic_min_citations,
            topic_max_citations=topic_max_citations,
            root_dir=root_dir,
            database=database,
            start_year=start_year,
            end_year=end_year,
            **filters,
        )

    indicators_by_year = indicators_by_year[
        indicators_by_year[criterion].isin(custom_topics)
    ]

    indicators_by_year = pivot_table(indicators_by_year)
    indicators_by_year = indicators_by_year.loc[custom_topics, :]

    indicators_by_year = indicators_by_year.reset_index()

    indicators_by_year = add_counters(
        column=criterion,
        name=criterion,
        directory=root_dir,
        database=database,
        table=indicators_by_year,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )
    indicators_by_year = indicators_by_year.set_index(criterion)

    indicators_by_year = indicators_by_year.sort_index(ascending=True, axis=1)

    if cumulative:
        indicators_by_year = indicators_by_year.cumsum(axis=1)

    termsByYear = TermsByYear()
    termsByYear.metric_ = "OCC"
    termsByYear.criterion_for_columns_ = "years"
    termsByYear.criterion_for_rows_ = criterion
    termsByYear.cumulative_ = cumulative
    termsByYear.table_ = indicators_by_year

    termsByYear.prompt_ = generate_prompt(termsByYear)

    return termsByYear
