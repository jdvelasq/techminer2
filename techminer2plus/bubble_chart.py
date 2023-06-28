# flake8: noqa
"""
Bubble Chart
===============================================================================


>>> root_dir = "data/regtech/"
>>> import techminer2plus
>>> matrix = techminer2plus.co_occurrence_matrix(
...    columns='author_keywords',
...    col_top_n=10,
...    root_dir=root_dir,
... )

>>> file_name = "sphinx/_static/bubble_chart.html"
>>> chart = techminer2plus.bubble_chart(matrix)
>>> chart.fig_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/bubble_chart.html" height="800px" width="100%" frameBorder="0"></iframe>

>>> chart.df_.head()
                 row             column  VALUE
0     REGTECH 28:329     REGTECH 28:329     28
1     FINTECH 12:249     FINTECH 12:249     12
2     FINTECH 12:249     REGTECH 28:329     12
3     REGTECH 28:329     FINTECH 12:249     12
4  COMPLIANCE 07:030  COMPLIANCE 07:030      7





# pylint: disable=line-too-long
"""
from dataclasses import dataclass

import pandas as pd
import plotly.express as px
import plotly.graph_objs as go


@dataclass
class BubbleChart:
    """Bubble Chart."""

    fig_: go.Figure
    df_: pd.DataFrame


def bubble_chart(
    cooc_matrix=None,
    title=None,
):
    """Makes a bubble chart."""

    matrix = cooc_matrix.df_.copy()
    matrix = matrix.melt(
        value_name="VALUE", var_name="column", ignore_index=False
    )
    matrix = matrix.reset_index()
    matrix = matrix.rename(columns={"index": "row"})
    matrix = matrix.sort_values(
        by=["VALUE", "row", "column"], ascending=[False, True, True]
    )
    matrix = matrix.reset_index(drop=True)

    fig = px.scatter(
        matrix,
        x="row",
        y="column",
        size="VALUE",
        hover_data=matrix.columns.to_list(),
        title=title,
    )
    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        showlegend=False,
        yaxis_title=None,
        xaxis_title=None,
        margin=dict(l=1, r=1, t=1, b=1),
    )
    fig.update_traces(
        marker=dict(
            line=dict(
                color="black",
                width=2,
            ),
        ),
        marker_color="darkslategray",
        mode="markers",
    )
    fig.update_xaxes(
        side="top",
        linecolor="white",
        linewidth=1,
        gridcolor="gray",
        griddash="dot",
        tickangle=270,
        dtick=1.0,
    )
    fig.update_yaxes(
        linecolor="white",
        linewidth=1,
        gridcolor="gray",
        griddash="dot",
        autorange="reversed",
    )

    return BubbleChart(
        fig_=fig,
        df_=matrix,
    )
