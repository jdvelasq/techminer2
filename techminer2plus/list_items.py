# flake8: noqa
"""
List Items
===============================================================================



>>> root_dir = "data/regtech/"


>>> import techminer2plus
>>> itemslist = techminer2plus.list_items(
...    field='author_keywords',
...    root_dir=root_dir,
... )

>>> itemslist
ItemsList(field='author_keywords', top_n='10', custom_items='['REGTECH',
    'FINTECH', 'REGULATORY_TECHNOLOGY', 'COMPLIANCE', 'REGULATION',
    'ANTI_MONEY_LAUNDERING', 'FINANCIAL_SERVICES', 'FINANCIAL_REGULATION',
    'ARTIFICIAL_INTELLIGENCE', 'RISK_MANAGEMENT']')


>>> itemslist.items_list_.head()
                       rank_occ  rank_gc  OCC  ...  h_index  g_index  m_index
author_keywords                                ...                           
REGTECH                       1        1   28  ...      9.0      4.0     1.29
FINTECH                       2        2   12  ...      5.0      3.0     0.83
REGULATORY_TECHNOLOGY         3        8    7  ...      4.0      2.0     1.00
COMPLIANCE                    4       12    7  ...      3.0      2.0     0.60
REGULATION                    5        4    5  ...      2.0      2.0     0.33
<BLANKLINE>
[5 rows x 18 columns]



>>> print(itemslist.chatbot_prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'author_keywords' field in a scientific bibliography database. \\
Summarize the table below, sorted by the 'OCC' metric, and delimited by \\
triple backticks, identify any notable patterns, trends, or outliers in the \\
data, and discuss their implications for the research field. Be sure to \\
provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| author_keywords         |   rank_occ |   rank_gc |   OCC |   Before 2022 |   Between 2022-2023 |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   average_growth_rate |   average_docs_per_year |   percentage_docs_last_year |   first_publication_year |   age |   global_citations_per_year |   h_index |   g_index |   m_index |
|:------------------------|-----------:|----------:|------:|--------------:|--------------------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------:|------------------------:|----------------------------:|-------------------------:|------:|----------------------------:|----------:|----------:|----------:|
| REGTECH                 |          1 |         1 |    28 |            20 |                   8 |                329 |                74 |                           11.75 |                           2.64 |                  -0.5 |                     4   |                   0.142857  |                     2017 |     7 |                       47    |         9 |         4 |      1.29 |
| FINTECH                 |          2 |         2 |    12 |            10 |                   2 |                249 |                49 |                           20.75 |                           4.08 |                  -0.5 |                     1   |                   0.0833333 |                     2018 |     6 |                       41.5  |         5 |         3 |      0.83 |
| REGULATORY_TECHNOLOGY   |          3 |         8 |     7 |             5 |                   2 |                 37 |                14 |                            5.29 |                           2    |                  -1.5 |                     1   |                   0.142857  |                     2020 |     4 |                        9.25 |         4 |         2 |      1    |
| COMPLIANCE              |          4 |        12 |     7 |             5 |                   2 |                 30 |                 9 |                            4.29 |                           1.29 |                   0   |                     1   |                   0.142857  |                     2019 |     5 |                        6    |         3 |         2 |      0.6  |
| REGULATION              |          5 |         4 |     5 |             4 |                   1 |                164 |                22 |                           32.8  |                           4.4  |                  -0.5 |                     0.5 |                   0.1       |                     2018 |     6 |                       27.33 |         2 |         2 |      0.33 |
| ANTI_MONEY_LAUNDERING   |          6 |        10 |     5 |             5 |                   0 |                 34 |                 8 |                            6.8  |                           1.6  |                  -1.5 |                     0   |                   0         |                     2020 |     4 |                        8.5  |         3 |         2 |      0.75 |
| FINANCIAL_SERVICES      |          7 |         3 |     4 |             3 |                   1 |                168 |                20 |                           42    |                           5    |                   0   |                     0.5 |                   0.125     |                     2017 |     7 |                       24    |         3 |         2 |      0.43 |
| FINANCIAL_REGULATION    |          8 |         9 |     4 |             2 |                   2 |                 35 |                 8 |                            8.75 |                           2    |                   0   |                     1   |                   0.25      |                     2017 |     7 |                        5    |         2 |         2 |      0.29 |
| ARTIFICIAL_INTELLIGENCE |          9 |        19 |     4 |             3 |                   1 |                 23 |                 6 |                            5.75 |                           1.5  |                   0   |                     0.5 |                   0.125     |                     2019 |     5 |                        4.6  |         3 |         2 |      0.6  |
| RISK_MANAGEMENT         |         10 |        25 |     3 |             2 |                   1 |                 14 |                 8 |                            4.67 |                           2.67 |                   0   |                     0.5 |                   0.166667  |                     2018 |     6 |                        2.33 |         2 |         2 |      0.33 |
```
<BLANKLINE>



# pylint: disable=line-too-long
"""
import textwrap
from dataclasses import dataclass

import pandas as pd

from .chatbot_prompts import format_chatbot_prompt_for_tables
from .filtering_lib import generate_custom_items
from .metrics_lib import indicators_by_field
from .params_check_lib import (
    check_bibliometric_metric,
    check_integer,
    check_integer_range,
)
from .sorting_lib import sort_indicators_by_metric


# pylint: disable=too-many-instance-attributes
@dataclass
class ItemsList:
    """List view.

    :meta private:
    """

    items_list_: pd.DataFrame
    chatbot_prompt_: str
    #
    # Params:
    field_: str
    metric_: str
    #
    # Item filters:
    top_n_: int
    occ_range_: tuple
    gc_range_: tuple
    custom_items_: list
    #
    # Database params:
    root_dir_: str
    database_: str
    year_filter_: tuple
    cited_by_filter_: tuple
    filters_: dict

    def __repr__(self):
        text = "ItemsList("
        text += f"field='{self.field_}'"
        if self.top_n_ is not None:
            text += f", top_n='{self.top_n_}'"
        if self.occ_range_ is not None:
            text += f", occ_range='{str(self.occ_range_)}'"
        if self.gc_range_ is not None:
            text += f", gc_range='{str(self.gc_range_)}'"
        if self.custom_items_ is not None:
            text += f", custom_items='{str(self.custom_items_)}'"
        text += ")"
        text = textwrap.fill(text, width=75, subsequent_indent="    ")
        return text


# pylint: disable=too-many-arguments
def list_items(
    field,
    metric="OCC",
    #
    # Item filters:
    top_n=10,
    occ_range=None,
    gc_range=None,
    custom_items=None,
    #
    # Database params:
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Returns a ItemList object with the extracted items of database field."""

    check_bibliometric_metric(metric)
    check_integer_range(gc_range)
    check_integer_range(occ_range)
    check_integer(top_n)

    indicators = indicators_by_field(
        field=field,
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    indicators = sort_indicators_by_metric(indicators, metric)

    if custom_items is None:
        if metric == "OCCGC":
            custom_items_occ = generate_custom_items(
                indicators=sort_indicators_by_metric(indicators, "OCC"),
                top_n=top_n,
                occ_range=occ_range,
                gc_range=gc_range,
            )

            custom_items_gc = generate_custom_items(
                indicators=sort_indicators_by_metric(
                    indicators, "global_citations"
                ),
                top_n=top_n,
                occ_range=occ_range,
                gc_range=gc_range,
            )

            custom_items = custom_items_occ[:]
            custom_items += [
                item
                for item in custom_items_gc
                if item not in custom_items_occ
            ]

        else:
            custom_items = generate_custom_items(
                indicators=indicators,
                top_n=top_n,
                occ_range=occ_range,
                gc_range=gc_range,
            )

    indicators = indicators[indicators.index.isin(custom_items)]

    metric = "OCC" if metric == "OCCGC" else metric
    #
    # Create the itemlist object:
    #
    return ItemsList(
        #
        # Results:
        items_list_=indicators,
        chatbot_prompt_=chatbot_prompt(field, metric, indicators),
        #
        # Params:
        field_=field,
        metric_=metric,
        #
        # Item filters:
        top_n_=top_n,
        occ_range_=occ_range,
        gc_range_=gc_range,
        #
        # Database params:
        root_dir_=root_dir,
        database_=database,
        year_filter_=year_filter,
        custom_items_=indicators.index.tolist(),
        cited_by_filter_=cited_by_filter,
        filters_=filters,
    )


# pylint: disable=line-too-long
def chatbot_prompt(field, metric, table):
    """Returns the prompt to be used in the chatbot.

    :meta private:
    """

    main_text = (
        "Your task is to generate an analysis about the bibliometric indicators of the "
        f"'{field}' field in a scientific bibliography database. Summarize the table below, "
        f"sorted by the '{metric}' metric, and delimited by triple backticks, identify "
        "any notable patterns, trends, or outliers in the data, and discuss their "
        "implications for the research field. Be sure to provide a concise summary "
        "of your findings in no more than 150 words."
    )
    return format_chatbot_prompt_for_tables(main_text, table.to_markdown())
