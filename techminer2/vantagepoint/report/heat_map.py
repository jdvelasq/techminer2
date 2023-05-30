# flake8: noqa
"""
Heat Map
===============================================================================


>>> root_dir = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> matrix = vantagepoint.analyze.co_occ_matrix(
...    criterion='author_keywords',
...    topic_occ_min=3,
...    root_dir=root_dir,
... )
>>> file_name = "sphinx/_static/vantagepoint__heat_map-1.html"

>>> chart = vantagepoint.report.heat_map(
...     matrix,
... )
>>> chart.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/vantagepoint__heat_map-1.html" height="800px" width="100%" frameBorder="0"></iframe>


>>> chart.table_
column                          regtech 28:329  ...  suptech 03:004
row                                             ...                
regtech 28:329                              28  ...               3
fintech 12:249                              12  ...               2
compliance 07:030                            7  ...               1
regulatory technology 07:037                 2  ...               1
regulation 05:164                            4  ...               1
artificial intelligence 04:023               2  ...               0
financial regulation 04:035                  2  ...               0
financial services 04:168                    3  ...               0
anti-money laundering 03:021                 1  ...               0
blockchain 03:005                            2  ...               0
innovation 03:012                            1  ...               0
risk management 03:014                       2  ...               1
suptech 03:004                               3  ...               3
<BLANKLINE>
[13 rows x 13 columns]

>>> print(chart.prompt_)
Analyze the table below which contains values for the metric OCC. The columns of the table correspond to author_keywords, and the rows correspond to author_keywords. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| row                            |   regtech 28:329 |   fintech 12:249 |   compliance 07:030 |   regulatory technology 07:037 |   regulation 05:164 |   artificial intelligence 04:023 |   financial regulation 04:035 |   financial services 04:168 |   anti-money laundering 03:021 |   blockchain 03:005 |   innovation 03:012 |   risk management 03:014 |   suptech 03:004 |
|:-------------------------------|-----------------:|-----------------:|--------------------:|-------------------------------:|--------------------:|---------------------------------:|------------------------------:|----------------------------:|-------------------------------:|--------------------:|--------------------:|-------------------------:|-----------------:|
| regtech 28:329                 |               28 |               12 |                   7 |                              2 |                   4 |                                2 |                             2 |                           3 |                              1 |                   2 |                   1 |                        2 |                3 |
| fintech 12:249                 |               12 |               12 |                   2 |                              1 |                   4 |                                1 |                             1 |                           2 |                              0 |                   1 |                   1 |                        2 |                2 |
| compliance 07:030              |                7 |                2 |                   7 |                              1 |                   1 |                                1 |                             0 |                           0 |                              0 |                   1 |                   0 |                        1 |                1 |
| regulatory technology 07:037   |                2 |                1 |                   1 |                              7 |                   1 |                                1 |                             0 |                           0 |                              1 |                   0 |                   1 |                        2 |                1 |
| regulation 05:164              |                4 |                4 |                   1 |                              1 |                   5 |                                0 |                             0 |                           1 |                              0 |                   1 |                   1 |                        2 |                1 |
| artificial intelligence 04:023 |                2 |                1 |                   1 |                              1 |                   0 |                                4 |                             0 |                           0 |                              1 |                   1 |                   0 |                        1 |                0 |
| financial regulation 04:035    |                2 |                1 |                   0 |                              0 |                   0 |                                0 |                             4 |                           2 |                              0 |                   0 |                   1 |                        0 |                0 |
| financial services 04:168      |                3 |                2 |                   0 |                              0 |                   1 |                                0 |                             2 |                           4 |                              0 |                   0 |                   0 |                        0 |                0 |
| anti-money laundering 03:021   |                1 |                0 |                   0 |                              1 |                   0 |                                1 |                             0 |                           0 |                              3 |                   0 |                   0 |                        0 |                0 |
| blockchain 03:005              |                2 |                1 |                   1 |                              0 |                   1 |                                1 |                             0 |                           0 |                              0 |                   3 |                   0 |                        0 |                0 |
| innovation 03:012              |                1 |                1 |                   0 |                              1 |                   1 |                                0 |                             1 |                           0 |                              0 |                   0 |                   3 |                        0 |                0 |
| risk management 03:014         |                2 |                2 |                   1 |                              2 |                   2 |                                1 |                             0 |                           0 |                              0 |                   0 |                   0 |                        3 |                1 |
| suptech 03:004                 |                3 |                2 |                   1 |                              1 |                   1 |                                0 |                             0 |                           0 |                              0 |                   0 |                   0 |                        1 |                3 |
<BLANKLINE>
<BLANKLINE>



"""
from dataclasses import dataclass

import numpy as np
import plotly.express as px


@dataclass(init=False)
class _Chart:
    plot_: None
    table_: None
    prompt_: None


def heat_map(obj, colormap="Blues"):
    """Make a heat map."""

    matrix = obj.matrix_.copy()

    fig = px.imshow(
        matrix,
        color_continuous_scale=colormap,
    )
    fig.update_xaxes(
        side="top",
        tickangle=270,
    )
    fig.update_layout(
        yaxis_title=None,
        xaxis_title=None,
        coloraxis_showscale=False,
        margin=dict(l=1, r=1, t=1, b=1),
    )

    full_fig = fig.full_figure_for_development()
    x_min, x_max = full_fig.layout.xaxis.range
    y_max, y_min = full_fig.layout.yaxis.range

    for value in np.linspace(x_min, x_max, matrix.shape[1] + 1):
        fig.add_vline(x=value, line_width=2, line_color="lightgray")

    for value in np.linspace(y_min, y_max, matrix.shape[0] + 1):
        fig.add_hline(y=value, line_width=2, line_color="lightgray")

    result = _Chart()
    result.plot_ = fig
    result.table_ = matrix
    result.prompt_ = obj.prompt_

    return result
