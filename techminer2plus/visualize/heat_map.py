# flake8: noqa
"""
Heat Map
===============================================================================


>>> root_dir = "data/regtech/"

>>> import techminer2plus
>>> matrix = techminer2plus.analyze.matrix.co_occurrence_matrix(
...    columns='author_keywords',
...    col_occ_range=(4, None),
...    root_dir=root_dir,
... )

>>> file_name = "sphinx/_static/visualize/heat_map.html"
>>> chart = techminer2plus.visualize.heat_map(
...     matrix,
... )
>>> chart.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/visualize/heat_map.html" height="800px" width="100%" frameBorder="0"></iframe>


>>> chart.table_
column                          REGTECH 28:329  ...  ARTIFICIAL_INTELLIGENCE 04:023
row                                             ...                                
REGTECH 28:329                              28  ...                               2
FINTECH 12:249                              12  ...                               1
REGULATORY_TECHNOLOGY 07:037                 2  ...                               1
COMPLIANCE 07:030                            7  ...                               1
REGULATION 05:164                            4  ...                               0
ANTI_MONEY_LAUNDERING 05:034                 1  ...                               1
FINANCIAL_SERVICES 04:168                    3  ...                               0
FINANCIAL_REGULATION 04:035                  2  ...                               0
ARTIFICIAL_INTELLIGENCE 04:023               2  ...                               4
<BLANKLINE>
[9 rows x 9 columns]




>>> print(chart.prompt_)
Your task is to generate a short paragraph for a research paper analyzing \\
the co-occurrence between the items of the same column in a bibliographic \\
dataset. Analyze the table below which contains values of co-occurrence \\
(OCC) for the 'author_keywords' field in a bibliographic dataset. Identify \\
any notable patterns, trends, or outliers in the data, and discuss their \\
implications for the research field. Be sure to provide a concise summary \\
of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| row                            |   REGTECH 28:329 |   FINTECH 12:249 |   REGULATORY_TECHNOLOGY 07:037 |   COMPLIANCE 07:030 |   REGULATION 05:164 |   ANTI_MONEY_LAUNDERING 05:034 |   FINANCIAL_SERVICES 04:168 |   FINANCIAL_REGULATION 04:035 |   ARTIFICIAL_INTELLIGENCE 04:023 |
|:-------------------------------|-----------------:|-----------------:|-------------------------------:|--------------------:|--------------------:|-------------------------------:|----------------------------:|------------------------------:|---------------------------------:|
| REGTECH 28:329                 |               28 |               12 |                              2 |                   7 |                   4 |                              1 |                           3 |                             2 |                                2 |
| FINTECH 12:249                 |               12 |               12 |                              1 |                   2 |                   4 |                              0 |                           2 |                             1 |                                1 |
| REGULATORY_TECHNOLOGY 07:037   |                2 |                1 |                              7 |                   1 |                   1 |                              2 |                           0 |                             0 |                                1 |
| COMPLIANCE 07:030              |                7 |                2 |                              1 |                   7 |                   1 |                              0 |                           0 |                             0 |                                1 |
| REGULATION 05:164              |                4 |                4 |                              1 |                   1 |                   5 |                              0 |                           1 |                             0 |                                0 |
| ANTI_MONEY_LAUNDERING 05:034   |                1 |                0 |                              2 |                   0 |                   0 |                              5 |                           0 |                             0 |                                1 |
| FINANCIAL_SERVICES 04:168      |                3 |                2 |                              0 |                   0 |                   1 |                              0 |                           4 |                             2 |                                0 |
| FINANCIAL_REGULATION 04:035    |                2 |                1 |                              0 |                   0 |                   0 |                              0 |                           2 |                             4 |                                0 |
| ARTIFICIAL_INTELLIGENCE 04:023 |                2 |                1 |                              1 |                   1 |                   0 |                              1 |                           0 |                             0 |                                4 |
```
<BLANKLINE>


# pylint: disable=line-too-long
"""
from dataclasses import dataclass

import numpy as np
import plotly.express as px

from ..analyze.matrix import co_occurrence_matrix


@dataclass(init=False)
class _Chart:
    plot_: None
    table_: None
    prompt_: None


def heat_map(
    obj=None,
    colormap="Blues",
    #
    # Co-occurrence matrix params:
    columns=None,
    rows=None,
    # Columns item filters:
    col_top_n=None,
    col_occ_range=None,
    col_gc_range=None,
    col_custom_items=None,
    # Rows item filters :
    row_top_n=None,
    row_occ_range=None,
    row_gc_range=None,
    row_custom_items=None,
    # Database params:
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Make a heat map."""

    if obj is None:
        obj = co_occurrence_matrix(
            columns=columns,
            rows=rows,
            #
            # Columns item filters:
            col_top_n=col_top_n,
            col_occ_range=col_occ_range,
            col_gc_range=col_gc_range,
            col_custom_items=col_custom_items,
            #
            # Rows item filters :
            row_top_n=row_top_n,
            row_occ_range=row_occ_range,
            row_gc_range=row_gc_range,
            row_custom_items=row_custom_items,
            #
            # Database params:
            root_dir=root_dir,
            database=database,
            year_filter=year_filter,
            cited_by_filter=cited_by_filter,
            **filters,
        )

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
