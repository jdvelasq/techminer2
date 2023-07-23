# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _time_analysis.average_citations_per_year:

Average Citations per Year
===============================================================================


>>> from techminer2.time_analysis import average_citations_per_year
>>> chart = average_citations_per_year(
...     #
...     # CHART PARAMS:
...     title="Average Citations per Year",
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> chart.fig_.write_html("sphinx/_static/time_analysis/average_citations_per_year.html")

.. raw:: html

    <iframe src="../../../../_static/time_analysis/average_citations_per_year.html"  
    height="600px" width="100%" frameBorder="0"></iframe>


>>> print(chart.df_.head().to_markdown())
|   year |   OCC |   cum_OCC |   local_citations |   global_citations |   citable_years |   mean_global_citations |   cum_global_citations |   mean_global_citations_per_year |   mean_local_citations |   cum_local_citations |   mean_local_citations_per_year |
|-------:|------:|----------:|------------------:|-------------------:|----------------:|------------------------:|-----------------------:|---------------------------------:|-----------------------:|----------------------:|--------------------------------:|
|   2016 |     1 |         1 |                 0 |                 30 |               8 |                30       |                     30 |                             3.75 |                0       |                     0 |                            0    |
|   2017 |     4 |         5 |                 3 |                162 |               7 |                40.5     |                    192 |                             5.79 |                0.75    |                     3 |                            0.11 |
|   2018 |     3 |         8 |                30 |                182 |               6 |                60.6667  |                    374 |                            10.11 |               10       |                    33 |                            1.67 |
|   2019 |     6 |        14 |                19 |                 47 |               5 |                 7.83333 |                    421 |                             1.57 |                3.16667 |                    52 |                            0.63 |
|   2020 |    14 |        28 |                29 |                 93 |               4 |                 6.64286 |                    514 |                             1.66 |                2.07143 |                    81 |                            0.52 |


>>> print(chart.prompt_)
The table below provides data on the average citations per year of the \\
dataset. Use the the information in the table to draw conclusions about the \\
impact per year. In your analysis, be sure to describe in a clear and \\
concise way, any trends or patterns you observe, and identify any outliers \\
or anomalies in the data. Limit your description to one paragraph with no \\
more than 250 words.
<BLANKLINE>
Table:
```
|   year |   mean_global_citations |   global_citations |
|-------:|------------------------:|-------------------:|
|   2016 |                30       |                 30 |
|   2017 |                40.5     |                162 |
|   2018 |                60.6667  |                182 |
|   2019 |                 7.83333 |                 47 |
|   2020 |                 6.64286 |                 93 |
|   2021 |                 2.7     |                 27 |
|   2022 |                 1.83333 |                 22 |
|   2023 |                 0       |                  0 |
```
<BLANKLINE>

"""
from dataclasses import dataclass

import pandas as pd
import plotly.graph_objects as go

from ..format_prompt_for_dataframes import format_prompt_for_dataframes
from ._metrics_by_year_chart import metrics_by_year_chart
from .metrics_per_year import metrics_per_year


def average_citations_per_year(
    #
    # CHART PARAMS:
    title: str = "Average Citations per Year",
    #
    # DATABASE PARAMS:
    root_dir: str = "./",
    database: str = "main",
    year_filter: tuple = (None, None),
    cited_by_filter: tuple = (None, None),
    **filters,
):
    """Average citations per year.

    :meta private:
    """

    data_frame = metrics_per_year(
        #
        # DATABASE PARAMS
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    prompt = __generate_prompt(data_frame)

    fig = metrics_by_year_chart(
        indicator_to_plot="mean_global_citations",
        title=title,
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
        "The table below provides data on the average citations per year "
        "of the dataset. Use the the information in the table to draw "
        "conclusions about the impact per year. In your analysis, be "
        "sure to describe in a clear and concise way, any trends or "
        "patterns you observe, and identify any outliers or anomalies "
        "in the data. Limit your description to one paragraph with no "
        "more than 250 words."
    )

    table_text = data_frame[["mean_global_citations", "global_citations"]].to_markdown()

    return format_prompt_for_dataframes(main_text, table_text)
