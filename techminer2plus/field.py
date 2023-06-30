# flake8: noqa
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
"""
.. _field:

Field
===============================================================================

>>> import techminer2plus as tm2p
>>> root_dir = "data/regtech/"
>>> field = tm2p.Records(root_dir=root_dir).field("author_keywords", top_n=10)
>>> field
Field(field='author_keywords', metric='OCC', top_n=10, custom_items=['REGTECH',
    'FINTECH', 'REGULATORY_TECHNOLOGY', 'COMPLIANCE', 'REGULATION',
    'ANTI_MONEY_LAUNDERING', 'FINANCIAL_SERVICES', 'FINANCIAL_REGULATION',
    'ARTIFICIAL_INTELLIGENCE', 'RISK_MANAGEMENT'])

>>> field.frame_
                         rank_occ  rank_gc  OCC  ...  h_index  g_index  m_index
author_keywords                                  ...                           
REGTECH                         1        1   28  ...      9.0      4.0     1.29
FINTECH                         2        2   12  ...      5.0      3.0     0.83
REGULATORY_TECHNOLOGY           3        8    7  ...      4.0      2.0     1.00
COMPLIANCE                      4       12    7  ...      3.0      2.0     0.60
REGULATION                      5        4    5  ...      2.0      2.0     0.33
ANTI_MONEY_LAUNDERING           6       10    5  ...      3.0      2.0     0.75
FINANCIAL_SERVICES              7        3    4  ...      3.0      2.0     0.43
FINANCIAL_REGULATION            8        9    4  ...      2.0      2.0     0.29
ARTIFICIAL_INTELLIGENCE         9       19    4  ...      3.0      2.0     0.60
RISK_MANAGEMENT                10       25    3  ...      2.0      2.0     0.33
<BLANKLINE>
[10 rows x 18 columns]


>>> print(field.prompt_)
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
from collections import defaultdict
from dataclasses import dataclass
from dataclasses import field as datafield
from typing import Dict, Optional

import pandas as pd

from .bar_chart import bar_chart
from .chatbot_prompts import format_chatbot_prompt_for_df
from .filtering_lib import generate_custom_items
from .metrics_lib import indicators_by_field
from .sorting_lib import sort_indicators_by_metric
from .terms_by_year import TermsByYear


# pylint: disable=too-many-instance-attributes
# pylint: disable=too-many-arguments
@dataclass
class Field:
    """Database field."""

    #
    # PARAMETERS:
    #
    records: pd.DataFrame
    field: str
    metric: str = "OCC"
    top_n: Optional[int] = None
    occ_range: Optional[tuple] = None
    gc_range: Optional[tuple] = None
    custom_items: Optional[list] = None

    #
    # FROM RECORDS:
    #
    root_dir: str = "./"
    database: str = "main"
    year_filter: tuple = (None, None)
    cited_by_filter: tuple = (None, None)
    filters: Dict[str, str] = datafield(
        default_factory=lambda: defaultdict(str)
    )

    #
    # RESULTS:
    #
    frame_: pd.DataFrame = pd.DataFrame()
    prompt_: str = "TODO"

    def __post_init__(self):
        #
        # COMPUTATIONS:
        #
        self.__compute_indicators_by_field()
        self.__sort_indicators_by_metric()
        self.__compute_custom_items()
        self.__filter_indicators()
        self.__repair_metric()
        self.__geneate_chatbot_prompt()

    #
    #
    # PROPERTIES
    #
    #
    def __repr__(self):
        text = (
            "Field("
            f"file='{self.field}'"
            f", metric='{self.metric}'"
            f", top_n={self.top_n}"
            f", occ_range={self.occ_range}"
            f", gc_range={self.gc_range}"
            f", custom_items={self.custom_items}"
            ")"
        )

        return textwrap.fill(text, width=80, subsequent_indent="    ")

    #
    #
    # PUBLIC METHODS FOR VISUALIZATION
    #
    #
    # def bar_chart(
    #     self,
    #     title=None,
    #     metric_label=None,
    #     field_label=None,
    # ):
    #     """Returns a bar chart."""
    #     return bar_chart(
    #         data_frame=self.frame_,
    #         x=self.metric,
    #         y=None,
    #         title=title,
    #         x_title=metric_label if metric_label is not None else self.field,
    #         y_title=field_label if field_label is not None else self.metric,
    #     )

    #
    #
    # PUBLIC METHODS FOR INTERFACING
    #
    #
    # def terms_by_year(self, cumulative=False):
    #     """Returns the terms by year."""
    #     return TermsByYear(
    #         records_instance=self.__records_instance,
    #         field_instance=self,
    #         cumulative=cumulative,
    #     )

    #
    #
    # COMPUTATIONS:
    #
    #
    def __geneate_chatbot_prompt(self):
        """Chat GPT prompt."""
        main_text = (
            "Your task is to generate an analysis about the bibliometric indicators of the "
            f"'{self.field}' field in a scientific bibliography database. Summarize the table below, "
            f"sorted by the '{self.metric}' metric, and delimited by triple backticks, identify "
            "any notable patterns, trends, or outliers in the data, and discuss their "
            "implications for the research field. Be sure to provide a concise summary "
            "of your findings in no more than 150 words."
        )
        self.prompt_ = format_chatbot_prompt_for_df(
            main_text, self.frame_.to_markdown()
        )

    def __compute_indicators_by_field(self):
        """Compute indicators by field

        :meta private:
        """
        self.frame_ = indicators_by_field(
            field=self.field,
            #
            # Database params:
            records=self.records,
            root_dir=self.root_dir,
            database=self.database,
            year_filter=self.year_filter,
            cited_by_filter=self.cited_by_filter,
            **self.filters,
        )

    def __sort_indicators_by_metric(self):
        """Sort indicators by metric.

        :meta private:
        """
        self.__frame = sort_indicators_by_metric(
            indicators=self.__frame,
            metric=self.__metric,
        )

    def __compute_custom_items(self):
        """Compute custom items.

        :meta private:
        """

        if self.__custom_items is not None:
            return

        if self.__metric == "OCCGC":
            custom_items_occ = generate_custom_items(
                indicators=sort_indicators_by_metric(self.__frame, "OCC"),
                top_n=self.__top_n,
                occ_range=self.__occ_range,
                gc_range=self.__gc_range,
            )

            custom_items_gc = generate_custom_items(
                indicators=sort_indicators_by_metric(
                    self.__frame, "global_citations"
                ),
                top_n=self.__top_n,
                occ_range=self.__occ_range,
                gc_range=self.__gc_range,
            )

            self.__custom_items = custom_items_occ[:]
            self.__custom_items += [
                item
                for item in custom_items_gc
                if item not in custom_items_occ
            ]

        else:
            self.__custom_items = generate_custom_items(
                indicators=self.__frame,
                top_n=self.__top_n,
                occ_range=self.__occ_range,
                gc_range=self.__gc_range,
            )

    def __filter_indicators(self):
        """Filter indicators.

        :meta private:
        """
        self.__frame = self.__frame[
            self.__frame.index.isin(self.__custom_items)
        ]

    def __repair_metric(self):
        """Check metric.

        :meta private:
        """
        self.__metric = "OCC" if self.__metric == "OCCGC" else self.__metric
