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


>>> from techminer2.tools import word_trends
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
...     custom_terms=None,
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> chart.fig_.write_html("sphinx/_static/tools/word_trends.html")

.. raw:: html

    <iframe src="../_static/tools/word_trends.html" 
    height="600px" width="100%" frameBorder="0"></iframe>


>>> chart.df_.head()
                      rank_occ  OCC  ...  average_growth_rate  average_docs_per_year
author_keywords                      ...                                            
FINTECH                      1   31  ...                 -1.0                    9.0
INNOVATION                   2    7  ...                 -1.5                    0.5
FINANCIAL_SERVICES           3    4  ...                  0.0                    1.5
FINANCIAL_INCLUSION          4    3  ...                 -1.0                    0.0
FINANCIAL_TECHNOLOGY         5    3  ...                  0.0                    1.0
<BLANKLINE>
[5 rows x 7 columns]


>>> print(chart.prompt_) # doctest: +ELLIPSIS
Your task is ...



"""
from dataclasses import dataclass

import plotly.express as px

from ..helpers.helper_format_prompt_for_dataframes import helper_format_prompt_for_dataframes
from ..metrics.growth_metrics import growth_metrics


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
    custom_terms=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """:meta private:"""

    #
    # Extracs only the performance metrics data frame
    data_frame = growth_metrics(
        #
        # ITEMS PARAMS:
        field=field,
        time_window=time_window,
        #
        # ITEM FILTERS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_terms=custom_terms,
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

    # extracts the name of column starting with 'between'
    between = [_ for _ in data_frame.columns if _.startswith("between")][0]
    before = [_ for _ in data_frame.columns if _.startswith("before")][0]

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
    prompt = helper_format_prompt_for_dataframes(main_text, data_frame.to_markdown())

    @dataclass
    class Results:
        df_ = data_frame
        prompt_ = prompt
        fig_ = fig

    return Results()
