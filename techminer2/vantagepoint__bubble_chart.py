"""
Bubble Chart
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/vantagepoint__bubble_chart.html"


>>> from techminer2 import vantagepoint__co_occ_matrix
>>> matrix = vantagepoint__co_occ_matrix(
...    column='author_keywords',
...    min_occ=4,
...    directory=directory,
... )

>>> from techminer2 import vantagepoint__bubble_chart
>>> vantagepoint__bubble_chart(matrix).write_html(file_name)

.. raw:: html

    <iframe src="../../_static/vantagepoint__bubble_chart.html" height="800px" width="100%" frameBorder="0"></iframe>

"""
import plotly.express as px


def vantagepoint__bubble_chart(
    matrix,
    title=None,
):
    """Makes a bubble chart."""

    matrix = matrix.melt(value_name="VALUE", var_name="column", ignore_index=False)
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
