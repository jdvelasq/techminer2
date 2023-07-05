# flake8: noqa
# pylint: disable=line-too-long
"""
.. _bubble_chart:

Bubble Chart
===============================================================================

* Preparation

>>> import techminer2plus as tm2p
>>> root_dir = "data/regtech/"


* Object oriented interface

>>> (
...     tm2p.records(root_dir=root_dir)
...     .co_occurrence_matrix(
...         columns='author_keywords',
...         col_top_n=10,
...     )
...     .bubble_chart()
...     .write_html("sphinx/_static/bubble_chart_0.html")
... )

.. raw:: html

    <iframe src="../_static/bubble_chart_0.html" height="800px" width="100%" frameBorder="0"></iframe>


* Functional interface

>>> cooc_matrix = tm2p.co_occurrence_matrix(
...    columns='author_keywords',
...    col_top_n=10,
...    root_dir=root_dir,
... )
>>> tm2p.bubble_chart(
...     cooc_matrix,
... ).write_html("sphinx/_static/bubble_chart_1.html")

.. raw:: html

    <iframe src="../_static/bubble_chart_1.html" height="800px" width="100%" frameBorder="0"></iframe>

"""
import plotly.express as px


def bubble_chart(
    cooc_matrix,
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

    return fig
