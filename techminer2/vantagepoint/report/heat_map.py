# flake8: noqa
"""
Heat Map
===============================================================================


>>> root_dir = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> matrix = vantagepoint.analyze.co_occ_matrix(
...    columns='author_keywords',
...    col_occ_range=(4, None),
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
column                                  REGTECH 28:329  ...  ARTIFICIAL_INTELLIGENCE 04:023
row                                                     ...                                
REGTECH 28:329                                      28  ...                               2
FINTECH 12:249                                      12  ...                               1
COMPLIANCE 07:030                                    7  ...                               1
REGULATION 05:164                                    4  ...                               0
FINANCIAL_SERVICES 04:168                            3  ...                               0
FINANCIAL_REGULATION 04:035                          2  ...                               0
REGULATORY_TECHNOLOGY (REGTECH) 04:030               0  ...                               0
ARTIFICIAL_INTELLIGENCE 04:023                       2  ...                               4
<BLANKLINE>
[8 rows x 8 columns]




>>> print(chart.prompt_)
Your task is to generate a short paragraph for a research paper analyzing the co-occurrence between the items of the same column in a bibliographic dataset.
<BLANKLINE>
Analyze the table below which contains values of co-occurrence (OCC) for the 'author_keywords' field in a bibliographic dataset. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| row                                    |   REGTECH 28:329 |   FINTECH 12:249 |   COMPLIANCE 07:030 |   REGULATION 05:164 |   FINANCIAL_SERVICES 04:168 |   FINANCIAL_REGULATION 04:035 |   REGULATORY_TECHNOLOGY (REGTECH) 04:030 |   ARTIFICIAL_INTELLIGENCE 04:023 |
|:---------------------------------------|-----------------:|-----------------:|--------------------:|--------------------:|----------------------------:|------------------------------:|-----------------------------------------:|---------------------------------:|
| REGTECH 28:329                         |               28 |               12 |                   7 |                   4 |                           3 |                             2 |                                        0 |                                2 |
| FINTECH 12:249                         |               12 |               12 |                   2 |                   4 |                           2 |                             1 |                                        0 |                                1 |
| COMPLIANCE 07:030                      |                7 |                2 |                   7 |                   1 |                           0 |                             0 |                                        0 |                                1 |
| REGULATION 05:164                      |                4 |                4 |                   1 |                   5 |                           1 |                             0 |                                        0 |                                0 |
| FINANCIAL_SERVICES 04:168              |                3 |                2 |                   0 |                   1 |                           4 |                             2 |                                        0 |                                0 |
| FINANCIAL_REGULATION 04:035            |                2 |                1 |                   0 |                   0 |                           2 |                             4 |                                        0 |                                0 |
| REGULATORY_TECHNOLOGY (REGTECH) 04:030 |                0 |                0 |                   0 |                   0 |                           0 |                             0 |                                        4 |                                0 |
| ARTIFICIAL_INTELLIGENCE 04:023         |                2 |                1 |                   1 |                   0 |                           0 |                             0 |                                        0 |                                4 |
<BLANKLINE>
<BLANKLINE>




# pylint: disable=line-too-long
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
