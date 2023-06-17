# flake8: noqa
"""
List Items
===============================================================================



>>> root_dir = "data/regtech/"


>>> import techminer2plus
>>> view = techminer2plus.system.analyze.list_items(
...    field='author_keywords',
...    root_dir=root_dir,
... )
>>> view.table_.head()
                       OCC  Before 2022  ...  g_index  m_index
author_keywords                          ...                  
REGTECH                 28           20  ...      4.0     1.29
FINTECH                 12           10  ...      3.0     0.83
REGULATORY_TECHNOLOGY    7            5  ...      2.0     1.00
COMPLIANCE               7            5  ...      2.0     0.60
REGULATION               5            4  ...      2.0     0.33
<BLANKLINE>
[5 rows x 16 columns]


>>> print(view.table_.head().to_markdown())
| author_keywords       |   OCC |   Before 2022 |   Between 2022-2023 |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   average_growth_rate |   average_docs_per_year |   percentage_docs_last_year |   first_publication_year |   age |   global_citations_per_year |   h_index |   g_index |   m_index |
|:----------------------|------:|--------------:|--------------------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------:|------------------------:|----------------------------:|-------------------------:|------:|----------------------------:|----------:|----------:|----------:|
| REGTECH               |    28 |            20 |                   8 |                329 |                74 |                           11.75 |                           2.64 |                  -0.5 |                     4   |                   0.142857  |                     2017 |     7 |                       47    |         9 |         4 |      1.29 |
| FINTECH               |    12 |            10 |                   2 |                249 |                49 |                           20.75 |                           4.08 |                  -0.5 |                     1   |                   0.0833333 |                     2018 |     6 |                       41.5  |         5 |         3 |      0.83 |
| REGULATORY_TECHNOLOGY |     7 |             5 |                   2 |                 37 |                14 |                            5.29 |                           2    |                  -1.5 |                     1   |                   0.142857  |                     2020 |     4 |                        9.25 |         4 |         2 |      1    |
| COMPLIANCE            |     7 |             5 |                   2 |                 30 |                 9 |                            4.29 |                           1.29 |                   0   |                     1   |                   0.142857  |                     2019 |     5 |                        6    |         3 |         2 |      0.6  |
| REGULATION            |     5 |             4 |                   1 |                164 |                22 |                           32.8  |                           4.4  |                  -0.5 |                     0.5 |                   0.1       |                     2018 |     6 |                       27.33 |         2 |         2 |      0.33 |



>>> print(view.prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'author_keywords' field in a scientific bibliography database. \\
Summarize the table below, sorted by the 'OCC' metric, and delimited by \\
triple backticks, identify any notable patterns, trends, or outliers in the \\
data, and discuss their implications for the research field. Be sure to \\
provide a concise summary of your findings in no more than 150 word.
<BLANKLINE>
Table:
```
| author_keywords         |   OCC |   Before 2022 |   Between 2022-2023 |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   average_growth_rate |   average_docs_per_year |   percentage_docs_last_year |   first_publication_year |   age |   global_citations_per_year |   h_index |   g_index |   m_index |
|:------------------------|------:|--------------:|--------------------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------:|------------------------:|----------------------------:|-------------------------:|------:|----------------------------:|----------:|----------:|----------:|
| REGTECH                 |    28 |            20 |                   8 |                329 |                74 |                           11.75 |                           2.64 |                  -0.5 |                     4   |                   0.142857  |                     2017 |     7 |                       47    |         9 |         4 |      1.29 |
| FINTECH                 |    12 |            10 |                   2 |                249 |                49 |                           20.75 |                           4.08 |                  -0.5 |                     1   |                   0.0833333 |                     2018 |     6 |                       41.5  |         5 |         3 |      0.83 |
| REGULATORY_TECHNOLOGY   |     7 |             5 |                   2 |                 37 |                14 |                            5.29 |                           2    |                  -1.5 |                     1   |                   0.142857  |                     2020 |     4 |                        9.25 |         4 |         2 |      1    |
| COMPLIANCE              |     7 |             5 |                   2 |                 30 |                 9 |                            4.29 |                           1.29 |                   0   |                     1   |                   0.142857  |                     2019 |     5 |                        6    |         3 |         2 |      0.6  |
| REGULATION              |     5 |             4 |                   1 |                164 |                22 |                           32.8  |                           4.4  |                  -0.5 |                     0.5 |                   0.1       |                     2018 |     6 |                       27.33 |         2 |         2 |      0.33 |
| ANTI_MONEY_LAUNDERING   |     5 |             5 |                   0 |                 34 |                 8 |                            6.8  |                           1.6  |                  -1.5 |                     0   |                   0         |                     2020 |     4 |                        8.5  |         3 |         2 |      0.75 |
| FINANCIAL_SERVICES      |     4 |             3 |                   1 |                168 |                20 |                           42    |                           5    |                   0   |                     0.5 |                   0.125     |                     2017 |     7 |                       24    |         3 |         2 |      0.43 |
| FINANCIAL_REGULATION    |     4 |             2 |                   2 |                 35 |                 8 |                            8.75 |                           2    |                   0   |                     1   |                   0.25      |                     2017 |     7 |                        5    |         2 |         2 |      0.29 |
| ARTIFICIAL_INTELLIGENCE |     4 |             3 |                   1 |                 23 |                 6 |                            5.75 |                           1.5  |                   0   |                     0.5 |                   0.125     |                     2019 |     5 |                        4.6  |         3 |         2 |      0.6  |
| RISK_MANAGEMENT         |     3 |             2 |                   1 |                 14 |                 8 |                            4.67 |                           2.67 |                   0   |                     0.5 |                   0.166667  |                     2018 |     6 |                        2.33 |         2 |         2 |      0.33 |
```
<BLANKLINE>

# pylint: disable=line-too-long
"""
import textwrap

from ...check_params import (
    check_bibliometric_metric,
    check_integer,
    check_integer_range,
)
from ...classes import ItemsList
from ...items import generate_custom_items
from ...sorting import sort_indicators_by_metric
from ..indicators import indicators_by_field


# pylint: disable=too-many-arguments
def list_items(
    field,
    metric="OCC",
    # Item filters:
    top_n=10,
    occ_range=None,
    gc_range=None,
    custom_items=None,
    # Database params:
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Returns a ItemList object with the extracted items of database field.



    Args:
        field (str): Database field to be used to extract the items.
        metric (str): Metric to be used to sort the items.

        top_n (int): Number of top items to be returned.
        occ_range (tuple): Range of occurrence of the items.
        gc_range (tuple): Range of global citations of the items.
        custom_items (list): List of items to be returned.

        root_dir (str): Root directory.
        database (str): Database name.
        year_filter (tuple, optional): Year database filter. Defaults to None.
        cited_by_filter (tuple, optional): Cited by database filter. Defaults to None.
        **filters (dict, optional): Filters to be applied to the database. Defaults to {}.

    Returns:
        A ItemList object.

    """

    def generate_prompt(field, table, metric):
        # pylint: disable=line-too-long
        prompt = (
            "Your task is to generate an analysis about the bibliometric indicators of the "
            f"'{field}' field in a scientific bibliography database. Summarize the table below, "
            f"sorted by the '{metric}' metric, and delimited by triple backticks, identify "
            "any notable patterns, trends, or outliers in the data, and discuss their "
            "implications for the research field. Be sure to provide a concise summary "
            "of your findings in no more than 150 words."
        )
        text = textwrap.fill(prompt, width=75)
        text = text.replace("\n", " \\\n")
        text = text[:-2] + ".\n\n"
        return text + f"Table:\n```\n{table.to_markdown()}\n```\n"

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
        custom_items = generate_custom_items(
            indicators=indicators,
            top_n=top_n,
            occ_range=occ_range,
            gc_range=gc_range,
        )

    indicators = indicators[indicators.index.isin(custom_items)]

    results = ItemsList()
    results.table_ = indicators
    results.prompt_ = generate_prompt(field, indicators, metric)
    results.metric_ = metric
    results.field_ = field
    results.custom_items_ = indicators.index.tolist()

    return results
