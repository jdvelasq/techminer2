# flake8: noqa
# pylint: disable=line-too-long
"""
.. _terms_by_year:

Terms by Year 
===============================================================================

* Preparation

>>> import techminer2plus as tm2p
>>> root_dir = "data/regtech/"

* Object oriented interface

>>> terms_by_year = (
...     tm2p.records(root_dir=root_dir)
...     .terms_by_year("author_keywords", top_n=10)
... )
>>> terms_by_year
TermsByYear(field='author_keywords', top_n=10, occ_range=(None, None),
    gc_range=(None, None), custom_items=['REGTECH', 'FINTECH',
    'REGULATORY_TECHNOLOGY', 'COMPLIANCE', 'REGULATION',
    'ANTI_MONEY_LAUNDERING', 'FINANCIAL_SERVICES', 'FINANCIAL_REGULATION',
    'ARTIFICIAL_INTELLIGENCE', 'RISK_MANAGEMENT'])

    
* Functional interface

>>> terms_by_year = tm2p.terms_by_year(
...     root_dir=root_dir,
...     field="author_keywords",
...     top_n=10,
... )
>>> terms_by_year
TermsByYear(field='author_keywords', top_n=10, occ_range=(None, None),
    gc_range=(None, None), custom_items=['REGTECH', 'FINTECH',
    'REGULATORY_TECHNOLOGY', 'COMPLIANCE', 'REGULATION',
    'ANTI_MONEY_LAUNDERING', 'FINANCIAL_SERVICES', 'FINANCIAL_REGULATION',
    'ARTIFICIAL_INTELLIGENCE', 'RISK_MANAGEMENT'])

* Results

>>> terms_by_year.df_
year                            2017  2018  2019  2020  2021  2022  2023
author_keywords                                                         
REGTECH 28:329                     2     3     4     8     3     6     2
FINTECH 12:249                     0     2     4     3     1     2     0
REGULATORY_TECHNOLOGY 07:037       0     0     0     2     3     2     0
COMPLIANCE 07:030                  0     0     1     3     1     1     1
REGULATION 05:164                  0     2     0     1     1     1     0
ANTI_MONEY_LAUNDERING 05:034       0     0     0     2     3     0     0
FINANCIAL_SERVICES 04:168          1     1     0     1     0     1     0
FINANCIAL_REGULATION 04:035        1     0     0     1     0     2     0
ARTIFICIAL_INTELLIGENCE 04:023     0     0     1     2     0     1     0
RISK_MANAGEMENT 03:014             0     1     0     1     0     1     0



>>> print(terms_by_year.prompt_)
Your task is to generate an analysis about the  occurrences by year of the \\
'author_keywords' in a scientific bibliography database. Summarize the \\
table below, delimited by triple backticks, identify any notable patterns, \\
trends, or outliers in the data, and disc  uss their implications for the \\
research field. Be sure to provide a concise summary of your findings in no \\
more than 150 words.
<BLANKLINE>
Table:
```
| author_keywords                |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:-------------------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| REGTECH 28:329                 |      2 |      3 |      4 |      8 |      3 |      6 |      2 |
| FINTECH 12:249                 |      0 |      2 |      4 |      3 |      1 |      2 |      0 |
| REGULATORY_TECHNOLOGY 07:037   |      0 |      0 |      0 |      2 |      3 |      2 |      0 |
| COMPLIANCE 07:030              |      0 |      0 |      1 |      3 |      1 |      1 |      1 |
| REGULATION 05:164              |      0 |      2 |      0 |      1 |      1 |      1 |      0 |
| ANTI_MONEY_LAUNDERING 05:034   |      0 |      0 |      0 |      2 |      3 |      0 |      0 |
| FINANCIAL_SERVICES 04:168      |      1 |      1 |      0 |      1 |      0 |      1 |      0 |
| FINANCIAL_REGULATION 04:035    |      1 |      0 |      0 |      1 |      0 |      2 |      0 |
| ARTIFICIAL_INTELLIGENCE 04:023 |      0 |      0 |      1 |      2 |      0 |      1 |      0 |
| RISK_MANAGEMENT 03:014         |      0 |      1 |      0 |      1 |      0 |      1 |      0 |
```
<BLANKLINE>




>>> terms_by_year = (
...     tm2p.records(root_dir=root_dir)
...     .terms_by_year("author_keywords", top_n=10, cumulative=True)
... )
>>> terms_by_year.df_
year                            2017  2018  2019  2020  2021  2022  2023
author_keywords                                                         
REGTECH 28:329                     2     5     9    17    20    26    28
FINTECH 12:249                     0     2     6     9    10    12    12
REGULATORY_TECHNOLOGY 07:037       0     0     0     2     5     7     7
COMPLIANCE 07:030                  0     0     1     4     5     6     7
REGULATION 05:164                  0     2     2     3     4     5     5
ANTI_MONEY_LAUNDERING 05:034       0     0     0     2     5     5     5
FINANCIAL_SERVICES 04:168          1     2     2     3     3     4     4
FINANCIAL_REGULATION 04:035        1     1     1     2     2     4     4
ARTIFICIAL_INTELLIGENCE 04:023     0     0     1     3     3     4     4
RISK_MANAGEMENT 03:014             0     1     1     2     2     3     3

>>> print(terms_by_year.prompt_)
Your task is to generate an analysis about the cumulative occurrences by \\
year of the 'author_keywords' in a scientific bibliography database. \\
Summarize the table below, delimited by triple backticks, identify any \\
notable patterns, trends, or outliers in the data, and disc  uss their \\
implications for the research field. Be sure to provide a concise summary \\
of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| author_keywords                |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:-------------------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| REGTECH 28:329                 |      2 |      5 |      9 |     17 |     20 |     26 |     28 |
| FINTECH 12:249                 |      0 |      2 |      6 |      9 |     10 |     12 |     12 |
| REGULATORY_TECHNOLOGY 07:037   |      0 |      0 |      0 |      2 |      5 |      7 |      7 |
| COMPLIANCE 07:030              |      0 |      0 |      1 |      4 |      5 |      6 |      7 |
| REGULATION 05:164              |      0 |      2 |      2 |      3 |      4 |      5 |      5 |
| ANTI_MONEY_LAUNDERING 05:034   |      0 |      0 |      0 |      2 |      5 |      5 |      5 |
| FINANCIAL_SERVICES 04:168      |      1 |      2 |      2 |      3 |      3 |      4 |      4 |
| FINANCIAL_REGULATION 04:035    |      1 |      1 |      1 |      2 |      2 |      4 |      4 |
| ARTIFICIAL_INTELLIGENCE 04:023 |      0 |      0 |      1 |      3 |      3 |      4 |      4 |
| RISK_MANAGEMENT 03:014         |      0 |      1 |      1 |      2 |      2 |      3 |      3 |
```
<BLANKLINE>



"""

import textwrap
from dataclasses import dataclass
from dataclasses import field as datafield
from typing import Optional

import pandas as pd

from ._chatbot import format_chatbot_prompt_for_df
from ._counters_lib import add_counters_to_frame_axis
from ._filtering_lib import generate_custom_items

# from ._metrics_lib import indicators_by_field, items_occ_by_year
from ._sorting_lib import sort_indicators_by_metric
from .gantt_chart import gantt_chart


# pylint: disable=too-many-instance-attributes
@dataclass
class TermsByYear:
    """Terms by year.

    :meta private:
    """

    #
    # PARAMS:
    field: str
    cumulative: bool = False
    #
    # ITEM FILTERS:
    top_n: Optional[int] = None
    occ_range: tuple = (None, None)
    gc_range: tuple = (None, None)
    custom_items: list = datafield(default_factory=list)
    #
    # DATABASE PARAMS:
    root_dir: str = "./"
    database: str = "main"
    year_filter: tuple = (None, None)
    cited_by_filter: tuple = (None, None)
    filters: dict = datafield(default_factory=dict)
    #
    # RESULTS:
    df_: pd.DataFrame = pd.DataFrame()
    prompt_: str = ""

    def __repr__(self):
        text = (
            "TermsByYear("
            f"field='{self.field}'"
            f", top_n={self.top_n}"
            f", occ_range={self.occ_range}"
            f", gc_range={self.gc_range}"
            f", custom_items={self.custom_items}"
            ")"
        )

        return textwrap.fill(text, width=80, subsequent_indent="    ")

    def gantt_chart(self, title=None):
        """Returns a Gantt chart."""
        return gantt_chart(self, title=title)


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def terms_by_year(
    #
    # PARAMS:
    field,
    cumulative=False,
    #
    # ITEM FILTERS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_items=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    # pylint: disable=line-too-long
    """Computes a table with the number of occurrences of each term by year."""

    def generate_prompt(field, cumulative, data_frame):
        # pylint: disable=line-too-long
        main_text = (
            "Your task is to generate an analysis about the "
            f"{'cumulative' if cumulative else ''} occurrences by year "
            f"of the '{field}' in a scientific bibliography database. "
            "Summarize the table below, delimited by triple backticks, "
            "identify any notable patterns, trends, or outliers in the data, "
            "and disc  uss their implications for the research field. Be sure "
            "to provide a concise summary of your findings in no more than "
            "150 words."
        )
        return format_chatbot_prompt_for_df(
            main_text, data_frame.to_markdown()
        )

    descriptors_by_year = items_occ_by_year(
        field=field,
        root_dir=root_dir,
        cumulative=cumulative,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    if custom_items is None:
        indicators = indicators_by_field(
            field=field,
            root_dir=root_dir,
            database=database,
            year_filter=year_filter,
            cited_by_filter=cited_by_filter,
            **filters,
        )

        indicators = sort_indicators_by_metric(indicators, metric="OCC")

        custom_items = generate_custom_items(
            indicators=indicators,
            top_n=top_n,
            occ_range=occ_range,
            gc_range=gc_range,
        )

    descriptors_by_year = descriptors_by_year[
        descriptors_by_year.index.isin(custom_items)
    ]

    descriptors_by_year = descriptors_by_year.loc[custom_items, :]

    descriptors_by_year = add_counters_to_frame_axis(
        descriptors_by_year,
        axis=0,
        field=field,
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    prompt = generate_prompt(field, cumulative, descriptors_by_year)

    return TermsByYear(
        #
        # PARAMS:
        field=field,
        cumulative=cumulative,
        #
        # ITEM FILTERS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        filters=filters,
        #
        # RESULTS:
        df_=descriptors_by_year,
        prompt_=prompt,
    )
