# flake8: noqa
# pylint: disable=line-too-long
"""
.. _list_items:

List Items
===============================================================================


* **USER COMPUTATIONAL INTERFACE:**

>>> import techminer2plus as tm2p
>>> root_dir = "data/regtech/"

>>> items_list = tm2p.Records(root_dir=root_dir).list_items(
...    field='author_keywords',
...    top_n=10,
... )
>>> items_list
ListItems(field='author_keywords', metric='OCC', top_n=10, occ_range=(None,
    None), gc_range=(None, None), custom_items=[])

>>> items_list.data_frame_.head()
                       rank_occ  rank_gc  OCC  ...  h_index  g_index  m_index
author_keywords                                ...                           
REGTECH                       1        1   28  ...      9.0      4.0     1.29
FINTECH                       2        2   12  ...      5.0      3.0     0.83
REGULATORY_TECHNOLOGY         3        8    7  ...      4.0      2.0     1.00
COMPLIANCE                    4       12    7  ...      3.0      2.0     0.60
REGULATION                    5        4    5  ...      2.0      2.0     0.33
<BLANKLINE>
[5 rows x 18 columns]


>>> print(items_list.prompt_)
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




"""
import textwrap
from dataclasses import dataclass
from dataclasses import field as datafield
from typing import Optional

import pandas as pd

from ...api.chatbot_prompts import format_chatbot_prompt_for_df
from ...api.filtering_lib import generate_custom_items
from ...api.records.list_items import list_items
from ...api.records.list_items.bar_chart import bar_chart
from ...api.sorting_lib import sort_indicators_by_metric

# =============================================================================
#
#
#  USER COMPUTATIONAL INTERFACE:
#
#
# =============================================================================


# pylint: disable=too-many-instance-attributes
@dataclass
class ListItems:
    """List items."""

    #
    # PARAMETERS:
    #
    field: str
    metric: str = "OCC"
    top_n: Optional[int] = None
    occ_range: tuple = (None, None)
    gc_range: tuple = (None, None)
    custom_items: list = datafield(default_factory=list)

    #
    # DATABASE PARAMS:
    #
    root_dir: str = "./"
    database: str = "main"
    year_filter: tuple = (None, None)
    cited_by_filter: tuple = (None, None)
    filters: dict = datafield(default_factory=dict)

    #
    # RESULTS:
    #
    data_frame_: pd.DataFrame = pd.DataFrame()
    prompt_: str = ""

    def __post_init__(self):
        #
        # COMPUTATIONS:
        #
        if self.filters is None:
            self.filters = {}

        self.data_frame_, self.prompt_ = list_items(
            #
            # FUNCTION PARAMS:
            field=self.field,
            metric=self.metric,
            top_n=self.top_n,
            occ_range=self.occ_range,
            gc_range=self.gc_range,
            custom_items=None
            if len(self.custom_items) == 0
            else self.custom_items,
            #
            # DATABASE PARAMS:
            root_dir=self.root_dir,
            database=self.database,
            year_filter=self.year_filter,
            cited_by_filter=self.cited_by_filter,
            **self.filters,
        )

    def __repr__(self):
        text = (
            "ListItems("
            f"field='{self.field}'"
            f", metric='{self.metric}'"
            f", top_n={self.top_n}"
            f", occ_range={self.occ_range}"
            f", gc_range={self.gc_range}"
            f", custom_items={self.custom_items}"
            ")"
        )

        return textwrap.fill(text, width=80, subsequent_indent="    ")

    def bar_chart(self, title=None, metric_label=None, field_label=None):
        """Bar chart interface."""

        return bar_chart(
            #
            # LISTITEMS PARAMS:
            field=self.field,
            metric=self.metric,
            top_n=self.top_n,
            occ_range=self.occ_range,
            gc_range=self.gc_range,
            custom_items=self.custom_items,
            #
            # CHART PARAMS:
            title=title,
            metric_label=metric_label,
            field_label=field_label,
            #
            # DATABASE PARAMS:
            root_dir=self.root_dir,
            database=self.database,
            year_filter=self.year_filter,
            cited_by_filter=self.cited_by_filter,
            **self.filters,
        )
