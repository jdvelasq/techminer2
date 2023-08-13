# flake8: noqa
# pylint: disable=line-too-long
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=missing-docstring
# pylint: disable=invalid-name
"""
.. _tm2.performnance.overview.publications_per_year:

Publications per Year
===============================================================================

>>> from techminer2.performance.overview import publications_per_year
>>> chart = publications_per_year(
...     #
...     # CHART PARAMS:
...     title="Publications per Year",
...     year_label=None,
...     metric_label="Publications per Year",
...     textfont_size=10,
...     marker_size=7,
...     line_width=1.5,
...     yshift=4,
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )

>>> chart.df_
      OCC  cum_OCC  global_citations
year                                
2016    1        1                30
2017    4        5               162
2018    3        8               182
2019    6       14                47
2020   14       28                93
2021   10       38                27
2022   12       50                22
2023    2       52                 0

>>> print(chart.prompt_)
The table below, delimited by triple backticks, provides data on the annual \\
scientific production in a bibliographic database. Use the table to draw \\
conclusions about annual research productivity and the cumulative \\
productivity. The column 'OCC' is the number of documents published in a \\
given year. The column 'cum_OCC' is the cumulative number of documents \\
published up to a given year. The information in the table is used to \\
create a line plot of number of publications per year. In your analysis, be \\
sure to describe in a clear and concise way, any trends or patterns you \\
observe, and identify any outliers or anomalies in the data. Limit your \\
description to one paragraph with no more than 250 words.
<BLANKLINE>
Table:
```
|   year |   OCC |   cum_OCC |   global_citations |
|-------:|------:|----------:|-------------------:|
|   2016 |     1 |         1 |                 30 |
|   2017 |     4 |         5 |                162 |
|   2018 |     3 |         8 |                182 |
|   2019 |     6 |        14 |                 47 |
|   2020 |    14 |        28 |                 93 |
|   2021 |    10 |        38 |                 27 |
|   2022 |    12 |        50 |                 22 |
|   2023 |     2 |        52 |                  0 |
```
<BLANKLINE>

>>> file_name = "sphinx/_static/performance/overview/publications_per_year.html"
>>> chart.fig_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../../_static/performance/overview/publications_per_year.html" 
    height="600px" width="100%" frameBorder="0"></iframe>
         

"""
from dataclasses import dataclass

import pandas as pd
import plotly.graph_objects as go

from ...format_prompt_for_dataframes import format_prompt_for_dataframes
from ._compute_metrics_per_year import compute_metrics_per_year
from ._plot_metrics_by_year import plot_metrics_by_year


def publications_per_year(
    #
    # CHART PARAMS:
    title: str = "Publications per Year",
    year_label=None,
    metric_label="Publications per Year",
    textfont_size=10,
    marker_size=7,
    line_width=1.5,
    yshift=4,
    #
    # DATABASE PARAMS:
    root_dir: str = "./",
    database: str = "main",
    year_filter: tuple = (None, None),
    cited_by_filter: tuple = (None, None),
    **filters,
):
    """
    :meta private:
    """
    data_frame = compute_metrics_per_year(
        #
        # DATABASE PARAMS
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )
    data_frame = data_frame[["OCC", "cum_OCC", "global_citations"]]

    prompt = __generate_prompt(data_frame)

    fig = plot_metrics_by_year(
        indicator_to_plot="OCC",
        auxiliary_indicator="global_citations",
        #
        # CHART PARAMS:
        title=title,
        year_label=year_label,
        metric_label=metric_label,
        textfont_size=textfont_size,
        marker_size=marker_size,
        line_width=line_width,
        yshift=yshift,
        #
        # DATABASE PARAMS
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    @dataclass
    class Result:
        df_: pd.DataFrame = data_frame
        fig_: go.Figure = fig
        prompt_: str = prompt

    return Result(
        df_=data_frame,
        fig_=fig,
        prompt_=prompt,
    )


def __generate_prompt(data_frame):
    #
    # Chatbot prompt
    main_text = (
        "The table below, delimited by triple backticks, provides data on "
        "the annual scientific production in a bibliographic database. Use "
        "the table to draw conclusions about annual research productivity "
        "and the cumulative productivity. The column 'OCC' is the number of "
        "documents published in a given year. The column 'cum_OCC' is "
        "the cumulative number of documents published up to a given year. "
        "The information in the table is used to create a line plot of "
        "number of publications per year. In your analysis, be sure to "
        "describe in a clear and concise way, any trends or patterns you "
        "observe, and identify any outliers or anomalies in the data. Limit "
        "your description to one paragraph with no more than 250 words."
    )

    table_text = data_frame.to_markdown()

    return format_prompt_for_dataframes(main_text, table_text)
