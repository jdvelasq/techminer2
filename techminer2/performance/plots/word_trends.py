# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=import-outside-toplevel
"""
Word Trends
===============================================================================


>>> from techminer2.performance.plots import word_trends
>>> chart = word_trends(
...     #
...     # ITEMS PARAMS:
...     field='author_keywords',
...     #
...     # TREND ANALYSIS:
...     time_window=2,
...     #
...     # CHART PARAMS:
...     title="Total Number of Documents, with Percentage of Documents Published in the Last Years",
...     metric_label=None,
...     field_label=None,
...     #
...     # ITEM FILTERS:
...     top_n=20,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_items=None,
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> chart.fig_.write_html("sphinx/_static/performance/plots/word_trends.html")

.. raw:: html

    <iframe src="../../../../../_static/performance/plots/word_trends.html" 
    height="600px" width="100%" frameBorder="0"></iframe>


>>> chart.df_.head()
                       rank_occ  OCC  ...  between_2022_2023  growth_percentage
author_keywords                       ...                                      
REGTECH                       1   28  ...                  8              28.57
FINTECH                       2   12  ...                  2              16.67
REGULATORY_TECHNOLOGY         3    7  ...                  2              28.57
COMPLIANCE                    4    7  ...                  2              28.57
REGULATION                    5    5  ...                  1              20.00
<BLANKLINE>
[5 rows x 5 columns]

>>> print(chart.prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'author_keywords' field in a scientific bibliography database. \\
Summarize the table below, containing the number of documents before_2022 \\
and between_2022_2023, and sorted by the total number of documents, and \\
delimited by triple backticks. Identify any notable patterns, trends, or \\
outliers in the data, and discuss their implications for the research \\
field. Be sure to provide a concise summary of your findings in no more \\
than 150 words.
<BLANKLINE>
Table:
```
| author_keywords         |   rank_occ |   OCC |   before_2022 |   between_2022_2023 |   growth_percentage |
|:------------------------|-----------:|------:|--------------:|--------------------:|--------------------:|
| REGTECH                 |          1 |    28 |            20 |                   8 |               28.57 |
| FINTECH                 |          2 |    12 |            10 |                   2 |               16.67 |
| REGULATORY_TECHNOLOGY   |          3 |     7 |             5 |                   2 |               28.57 |
| COMPLIANCE              |          4 |     7 |             5 |                   2 |               28.57 |
| REGULATION              |          5 |     5 |             4 |                   1 |               20    |
| ANTI_MONEY_LAUNDERING   |          6 |     5 |             5 |                   0 |                0    |
| FINANCIAL_SERVICES      |          7 |     4 |             3 |                   1 |               25    |
| FINANCIAL_REGULATION    |          8 |     4 |             2 |                   2 |               50    |
| ARTIFICIAL_INTELLIGENCE |          9 |     4 |             3 |                   1 |               25    |
| RISK_MANAGEMENT         |         10 |     3 |             2 |                   1 |               33.33 |
| INNOVATION              |         11 |     3 |             2 |                   1 |               33.33 |
| BLOCKCHAIN              |         12 |     3 |             3 |                   0 |                0    |
| SUPTECH                 |         13 |     3 |             1 |                   2 |               66.67 |
| SEMANTIC_TECHNOLOGIES   |         14 |     2 |             2 |                   0 |                0    |
| DATA_PROTECTION         |         15 |     2 |             1 |                   1 |               50    |
| SMART_CONTRACTS         |         16 |     2 |             2 |                   0 |                0    |
| CHARITYTECH             |         17 |     2 |             1 |                   1 |               50    |
| ENGLISH_LAW             |         18 |     2 |             1 |                   1 |               50    |
| ACCOUNTABILITY          |         19 |     2 |             2 |                   0 |                0    |
| DATA_PROTECTION_OFFICER |         20 |     2 |             2 |                   0 |                0    |
```
<BLANKLINE>



"""
from dataclasses import dataclass

import plotly.express as px

from ...format_prompt_for_dataframes import format_prompt_for_dataframes
from ..performance_metrics import performance_metrics


def word_trends(
    #
    # ITEM PARAMS:
    field,
    #
    # TREND ANALYSIS:
    time_window=2,
    #
    # CHART PARAMS:
    title=None,
    metric_label=None,
    field_label=None,
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
    """
    :meta private:
    """

    #
    # Extracs only the performance metrics data frame
    data_frame = performance_metrics(
        #
        # ITEMS PARAMS:
        field=field,
        metric="OCC",
        #
        # ITEM FILTERS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        #
        # TREND ANALYSIS:
        time_window=time_window,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    ).df_

    metric_label = "OCC" if metric_label is None else metric_label
    field_label = field.replace("_", " ").upper() if field_label is None else field_label

    before = data_frame.columns[2]
    between = data_frame.columns[3]

    fig_data = data_frame[["OCC", before, between]].copy()
    fig_data[field] = fig_data.index
    fig_data = fig_data.reset_index(drop=True)

    fig_data = fig_data.melt(
        id_vars=field,
        value_vars=[before, between],
    )

    fig_data = fig_data.rename(
        columns={
            field: field.replace("_", " ").title(),
            "variable": "Period",
            "value": "Num Documents",
        }
    )

    fig = px.bar(
        fig_data,
        x="Num Documents",
        y=field.replace("_", " ").title(),
        color="Period",
        title=title,
        orientation="h",
        color_discrete_map={
            before: "#7793a5",
            between: "#465c6b",
        },
    )
    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
    )
    fig.update_yaxes(
        linecolor="gray",
        linewidth=2,
        autorange="reversed",
        title=field_label,
    )
    fig.update_xaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="gray",
        griddash="dot",
    )

    main_text = (
        "Your task is to generate an analysis about the bibliometric indicators of the "
        f"'{field}' field in a scientific bibliography database. Summarize the table below, "
        f"containing the number of documents {before} and {between}, "
        "and sorted by the total number of documents, and delimited by triple backticks. Identify "
        "any notable patterns, trends, or outliers in the data, and discuss their "
        "implications for the research field. Be sure to provide a concise summary "
        "of your findings in no more than 150 words. "
    )
    prompt = format_prompt_for_dataframes(main_text, data_frame.to_markdown())

    @dataclass
    class Results:
        df_ = data_frame
        prompt_ = prompt
        fig_ = fig

    return Results()
