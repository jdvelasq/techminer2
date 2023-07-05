# flake8: noqa
# pylint: disable=line-too-long
"""
.. _list_items:

List Items
===============================================================================

>>> import techminer2plus as tm2p
>>> root_dir = "data/regtech/"

>>> list_items = tm2p.records(root_dir=root_dir).list_items(
...    field='author_keywords',
...    top_n=10,
... )
>>> list_items.data_frame_.head()
                       rank_occ  rank_gc  OCC  ...  h_index  g_index  m_index
author_keywords                                ...                           
REGTECH                       1        1   28  ...      9.0      4.0     1.29
FINTECH                       2        2   12  ...      5.0      3.0     0.83
REGULATORY_TECHNOLOGY         3        8    7  ...      4.0      2.0     1.00
COMPLIANCE                    4       12    7  ...      3.0      2.0     0.60
REGULATION                    5        4    5  ...      2.0      2.0     0.33
<BLANKLINE>
[5 rows x 18 columns]


>>> list_items = tm2p.list_items(
...    field='author_keywords',
...    top_n=10,
...    root_dir=root_dir,
... )
>>> list_items.data_frame_.head()
                       rank_occ  rank_gc  OCC  ...  h_index  g_index  m_index
author_keywords                                ...                           
REGTECH                       1        1   28  ...      9.0      4.0     1.29
FINTECH                       2        2   12  ...      5.0      3.0     0.83
REGULATORY_TECHNOLOGY         3        8    7  ...      4.0      2.0     1.00
COMPLIANCE                    4       12    7  ...      3.0      2.0     0.60
REGULATION                    5        4    5  ...      2.0      2.0     0.33
<BLANKLINE>
[5 rows x 18 columns]


>>> print(list_items.prompt_)
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

from ._chatbot import format_chatbot_prompt_for_df
from ._filtering_lib import generate_custom_items
from ._metrics_lib import indicators_by_field
from ._sorting_lib import sort_indicators_by_metric
from .bar_chart import bar_chart
from .cleveland_dot_chart import cleveland_dot_chart
from .column_chart import column_chart
from .line_chart import line_chart
from .pie_chart import pie_chart
from .ranking_chart import ranking_chart
from .word_cloud import word_cloud
from .world_map import world_map


# pylint: disable=too-many-instance-attributes
@dataclass
class ListItems:
    """List items."""

    #
    # PARAMS:
    field: str
    metric: str = "OCC"
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

    def __post_init__(self):
        #
        # COMPUTATIONS:
        #
        if self.filters is None:
            self.filters = {}

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
            # CHART PARAMS:
            self,
            title=title,
            metric_label=metric_label,
            field_label=field_label,
        )

    def cleveland_dot_chart(
        self, title=None, metric_label=None, field_label=None
    ):
        """Column chart interface."""

        return cleveland_dot_chart(
            #
            # CHART PARAMS:
            self,
            title=title,
            metric_label=metric_label,
            field_label=field_label,
        )

    def column_chart(self, title=None, metric_label=None, field_label=None):
        """Column chart interface."""

        return column_chart(
            #
            # CHART PARAMS:
            self,
            title=title,
            metric_label=metric_label,
            field_label=field_label,
        )

    def line_chart(self, title=None, metric_label=None, field_label=None):
        """Column chart interface."""

        return line_chart(
            #
            # CHART PARAMS:
            self,
            title=title,
            metric_label=metric_label,
            field_label=field_label,
        )

    def pie_chart(self, title=None, hole=0.4):
        """Column chart interface."""
        return pie_chart(
            #
            # CHART PARAMS:
            self,
            title=title,
            hole=hole,
        )

    def word_cloud(self, title=None, figsize=(10, 10)):
        """Word cloud interface."""
        return word_cloud(
            list_items=self,
            title=title,
            figsize=figsize,
        )

    def world_map(self, colormap="Blues", title=None):
        """World map interface."""
        return world_map(
            list_items=self,
            colormap=colormap,
            title=title,
        )

    # pylint: disable=too-many-arguments
    def ranking_chart(
        self,
        title=None,
        field_label=None,
        metric_label=None,
        textfont_size=10,
        marker_size=7,
        line_color="black",
        line_width=1.5,
        yshift=4,
    ):
        """World map interface."""
        return ranking_chart(
            list_items=self,
            title=title,
            field_label=field_label,
            metric_label=metric_label,
            textfont_size=textfont_size,
            marker_size=marker_size,
            line_color=line_color,
            line_width=line_width,
            yshift=yshift,
        )


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def list_items(
    #
    # LISTITEMS PARAMS:
    field,
    metric="OCC",
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
    """Returns a ItemList object with the extracted items of database field."""

    # pylint: disable=line-too-long
    def generate_prompt(field, metric, table):
        """Returns the prompt to be used in the chatbot."""

        main_text = (
            "Your task is to generate an analysis about the bibliometric indicators of the "
            f"'{field}' field in a scientific bibliography database. Summarize the table below, "
            f"sorted by the '{metric}' metric, and delimited by triple backticks, identify "
            "any notable patterns, trends, or outliers in the data, and discuss their "
            "implications for the research field. Be sure to provide a concise summary "
            "of your findings in no more than 150 words."
        )
        return format_chatbot_prompt_for_df(main_text, table.to_markdown())

    # check_bibliometric_metric(metric)
    # check_integer_range(gc_range)
    # check_integer_range(occ_range)
    # check_integer(top_n)

    data_frame = indicators_by_field(
        field=field,
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    data_frame = sort_indicators_by_metric(data_frame, metric)

    if custom_items is None:
        if metric == "OCCGC":
            custom_items_occ = generate_custom_items(
                indicators=sort_indicators_by_metric(data_frame, "OCC"),
                top_n=top_n,
                occ_range=occ_range,
                gc_range=gc_range,
            )

            custom_items_gc = generate_custom_items(
                indicators=sort_indicators_by_metric(
                    data_frame, "global_citations"
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
                indicators=data_frame,
                top_n=top_n,
                occ_range=occ_range,
                gc_range=gc_range,
            )

    data_frame = data_frame[data_frame.index.isin(custom_items)]

    metric = "OCC" if metric == "OCCGC" else metric

    prompt = generate_prompt(field, metric, data_frame)

    return ListItems(
        #
        # PARAMETERS:
        field=field,
        metric=metric,
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        #
        # RESULTS:
        df_=data_frame,
        prompt_=prompt,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )
