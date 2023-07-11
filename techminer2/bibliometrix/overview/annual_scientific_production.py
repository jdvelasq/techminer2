# flake8: noqa
# pylint: disable=line-too-long
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=missing-docstring
# pylint: disable=invalid-name
"""
.. _annual_scientific_production:

Annual Scientific Production
===============================================================================

>>> from techminer2 import bibliometrix
>>> root_dir = "data/regtech/"
>>> annual_scientific_production = bibliometrix.overview.annual_scientific_production(
...     root_dir=root_dir,
... )

>>> annual_scientific_production.df_
      OCC  cum_OCC  ...  cum_local_citations  mean_local_citations_per_year
year                ...                                                    
2016    1        1  ...                  0.0                           0.00
2017    4        5  ...                  3.0                           0.11
2018    3        8  ...                 33.0                           1.67
2019    6       14  ...                 52.0                           0.63
2020   14       28  ...                 81.0                           0.52
2021   10       38  ...                 90.0                           0.30
2022   12       50  ...                 93.0                           0.12
2023    2       52  ...                 93.0                           0.00
<BLANKLINE>
[8 rows x 11 columns]

>>> print(annual_scientific_production.prompt_)
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
|   year |   OCC |   cum_OCC |
|-------:|------:|----------:|
|   2016 |     1 |         1 |
|   2017 |     4 |         5 |
|   2018 |     3 |         8 |
|   2019 |     6 |        14 |
|   2020 |    14 |        28 |
|   2021 |    10 |        38 |
|   2022 |    12 |        50 |
|   2023 |     2 |        52 |
```
<BLANKLINE>

>>> file_name = "sphinx/_static/annual_scientific_production_chart.html"
>>> annual_scientific_production.fig_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../_static/annual_scientific_production_chart.html" height="600px" width="100%" frameBorder="0"></iframe>
         

"""
from dataclasses import dataclass

import pandas as pd
import plotly.graph_objects as go

from ...format_prompt_for_dataframes import format_prompt_for_dataframes
from ...techminer.metrics.global_metrics_by_year_chart import (
    global_metrics_by_year_chart,
)
from ...techminer.metrics.global_metrics_by_year_table import (
    global_metrics_by_year_table,
)


def annual_scientific_production(
    title: str = "Annual Scientific Production",
    #
    # DATABASE PARAMS:
    root_dir: str = "./",
    database: str = "main",
    year_filter: tuple = (None, None),
    cited_by_filter: tuple = (None, None),
    **filters,
):
    data_frame = global_metrics_by_year_table(
        #
        # DATABASE PARAMS
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    prompt = __generate_prompt(data_frame)

    fig = global_metrics_by_year_chart(
        indicator_to_plot="OCC",
        title=title,
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
    """Makes a time line plot for indicators."""

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

    table_text = data_frame[["OCC", "cum_OCC"]].to_markdown()

    return format_prompt_for_dataframes(main_text, table_text)
