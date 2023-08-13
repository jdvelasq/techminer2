# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _tm2.performance.overview.local_citations_per_year:

Local Citations per Year
===============================================================================


>>> from techminer2.performance.overview import local_citations_per_year
>>> chart = local_citations_per_year(
...     #
...     # CHART PARAMS:
...     title="Local Citations per Year",
...     metric_label="Local Citations per Year",
...     year_label=None,
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
>>> chart.fig_.write_html("sphinx/_static/performance/overview/local_citations_per_year.html")

.. raw:: html

    <iframe src="../../../../../_static/performance/overview/local_citations_per_year.html"  
    height="600px" width="100%" frameBorder="0"></iframe>


>>> print(chart.df_.to_markdown())
|   year |   OCC |   global_citations |   local_citations |   mean_global_citations_per_year |   mean_local_citations_per_year |
|-------:|------:|-------------------:|------------------:|---------------------------------:|--------------------------------:|
|   2016 |     1 |                 30 |                 8 |                             3.75 |                            1    |
|   2017 |     4 |                162 |                19 |                             5.79 |                            0.68 |
|   2018 |     3 |                182 |                30 |                            10.11 |                            1.67 |
|   2019 |     6 |                 47 |                20 |                             1.57 |                            0.67 |
|   2020 |    14 |                 93 |                23 |                             1.66 |                            0.41 |
|   2021 |    10 |                 27 |                 9 |                             0.9  |                            0.3  |
|   2022 |    12 |                 22 |                 3 |                             0.92 |                            0.12 |
|   2023 |     2 |                  0 |                 0 |                             0    |                            0    |





>>> print(chart.df_.T.to_markdown())
|                                |   2016 |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:-------------------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| OCC                            |   1    |   4    |   3    |   6    |  14    |   10   |  12    |      2 |
| global_citations               |  30    | 162    | 182    |  47    |  93    |   27   |  22    |      0 |
| local_citations                |   8    |  19    |  30    |  20    |  23    |    9   |   3    |      0 |
| mean_global_citations_per_year |   3.75 |   5.79 |  10.11 |   1.57 |   1.66 |    0.9 |   0.92 |      0 |
| mean_local_citations_per_year  |   1    |   0.68 |   1.67 |   0.67 |   0.41 |    0.3 |   0.12 |      0 |



>>> print(chart.prompt_)
The table below provides data on: the (a) global citations score per year \\
(global_citations); (b) local citations score (local_citations) per year; \\
(c) global citations per year divided by the age of the documents \\
(mean_global_citations_per_year); (d) local citations per year divided by \\
the age of the documents (mean_local_citations_per_year). (e) the number of \\
documents per year. Use the the information in the table to draw \\
conclusions about the impact per year. In your analysis, be sure to \\
describe in a clear and concise way, any trends or patterns you observe, \\
and identify any outliers or anomalies in the data. Limit your description \\
to one paragraph with no more than 250 words.
<BLANKLINE>
Table:
```
|   year |   OCC |   global_citations |   local_citations |   mean_global_citations_per_year |   mean_local_citations_per_year |
|-------:|------:|-------------------:|------------------:|---------------------------------:|--------------------------------:|
|   2016 |     1 |                 30 |                 8 |                             3.75 |                            1    |
|   2017 |     4 |                162 |                19 |                             5.79 |                            0.68 |
|   2018 |     3 |                182 |                30 |                            10.11 |                            1.67 |
|   2019 |     6 |                 47 |                20 |                             1.57 |                            0.67 |
|   2020 |    14 |                 93 |                23 |                             1.66 |                            0.41 |
|   2021 |    10 |                 27 |                 9 |                             0.9  |                            0.3  |
|   2022 |    12 |                 22 |                 3 |                             0.92 |                            0.12 |
|   2023 |     2 |                  0 |                 0 |                             0    |                            0    |
```
<BLANKLINE>



"""

from dataclasses import dataclass

import pandas as pd
import plotly.graph_objects as go

from ...format_prompt_for_dataframes import format_prompt_for_dataframes
from ._compute_metrics_per_year import compute_metrics_per_year
from ._plot_metrics_by_year import plot_metrics_by_year


def local_citations_per_year(
    #
    # CHART PARAMS:
    title: str = "Global Citations per Year",
    year_label=None,
    metric_label=None,
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
    """Global citations per year.

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
    data_frame = data_frame[
        [
            "OCC",
            "global_citations",
            "local_citations",
            "mean_global_citations_per_year",
            "mean_local_citations_per_year",
        ]
    ]

    prompt = __generate_prompt(data_frame)

    fig = plot_metrics_by_year(
        indicator_to_plot="local_citations",
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
        # DATABASE PARAMS:
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


def __generate_prompt(data_frame: pd.DataFrame) -> str:
    main_text = (
        "The table below provides data on: the (a) global citations score per year "
        "(global_citations); (b) local citations score (local_citations) per year; "
        "(c) global citations per year divided by the age of the documents "
        "(mean_global_citations_per_year); (d) local citations per year divided "
        "by the age of the documents (mean_local_citations_per_year). (e) the "
        "number of documents per year. "
        "Use the the information in the table to draw conclusions about the impact "
        "per year. In your analysis, be sure to describe in a clear and "
        "concise way, any trends or patterns you observe, and identify "
        "any outliers or anomalies in the data. Limit your description to "
        "one paragraph with no more than 250 words."
    )

    table_text = data_frame.to_markdown()

    return format_prompt_for_dataframes(main_text, table_text)
