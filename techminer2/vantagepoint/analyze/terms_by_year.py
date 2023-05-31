# flake8: noqa
"""
Terms by Year 
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
years. Identify any notable patterns, trends, or outliers in the data, and \
discuss their implications for the research field. Be sure to provide a \
concise summary of your findings in no more than 150 words.
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
the years. Identify any notable patterns, trends, or outliers in the data, \
and discuss their implications for the research field. Be sure to provide a \
concise summary of your findings in no more than 150 words.
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
from ...classes import TermsByYear
from ...counters import add_counters_to_axis
from ...item_utils import generate_custom_items
from ...sort_utils import sort_indicators_by_metric
from ...techminer.indicators.indicators_by_item import indicators_by_item


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def terms_by_year(
    criterion,
    topics_length=50,
    topic_occ_min=None,
    topic_occ_max=None,
    topic_citations_min=None,
    topic_citations_max=None,
    custom_topics=None,
    root_dir="./",
    database="documents",
    start_year=None,
    end_year=None,
    cumulative=False,
    **filters,
):
    """Computes a table with the number of occurrences of each term by year.

    Args:
        criterion (str): Criterion to be used to generate the terms.
        topics_length (int, optional): Number of terms to be included in the
            table. Defaults to 50.
        topic_occ_min (int, optional): Minimum number of occurrences of the
            terms. Defaults to None.
        topic_occ_max (int, optional): Maximum number of occurrences of the
            terms. Defaults to None.
        topic_citations_min (int, optional): Minimum number of citations of
            the terms. Defaults to None.
        topic_citations_max (int, optional): Maximum number of citations of
            the terms. Defaults to None.
        custom_topics (list, optional): List of custom topics. Defaults to
            None.
        root_dir (str, optional): Root directory. Defaults to "./".
        database (str, optional): Database to be used. Defaults to "documents".
        start_year (int, optional): Start year. Defaults to None.
        end_year (int, optional): End year. Defaults to None.
        cumulative (bool, optional): If True, the table contains the cumulative
            number of occurrences. Defaults to False.

    Returns:
        TermsByYear: A TermsByYear object.

    """

    def generate_prompt(obj):
        return (
            f"Analyze the table below which contains the "
            f"{'cumulative' if obj.cumulative_ else ''} occurrences by year "
            f"for the {obj.criterion_}. Identify any notable "
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
        indicators = indicators_by_item(
            field=criterion,
            root_dir=root_dir,
            database=database,
            year_filter=start_year,
            cited_by_filter=end_year,
            **filters,
        )

        indicators = sort_indicators_by_metric(indicators, metric="OCC")

        custom_topics = generate_custom_items(
            indicators=indicators,
            top_n=topics_length,
            occ_range=topic_occ_min,
            topic_occ_max=topic_occ_max,
            gc_range=topic_citations_min,
            topic_citations_max=topic_citations_max,
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
    obj.criterion_ = "years"
    obj.other_criterion_ = criterion
    obj.cumulative_ = cumulative
    obj.table_ = descriptors_by_year
    obj.prompt_ = generate_prompt(obj)

    return obj
