"""
Heat Map
===============================================================================


>>> directory = "data/regtech/"

>>> from techminer2.vantagepoint__co_occ_matrix import vantagepoint__co_occ_matrix
>>> matrix = vantagepoint__co_occ_matrix(
...    criterion='author_keywords',
...    topic_min_occ=3,
...    directory=directory,
... )
>>> file_name = "sphinx/_static/vantagepoint__heat_map-1.html"


>>> from techminer2.vantagepoint__heat_map import vantagepoint__heat_map
>>> vantagepoint__heat_map(
...     matrix,
... ).write_html(file_name)


.. raw:: html

    <iframe src="../../_static/vantagepoint__heat_map-1.html" height="800px" width="100%" frameBorder="0"></iframe>





"""
import numpy as np
import plotly.express as px


def vantagepoint__heat_map(matrix, colormap="Blues"):

    """Make a heat map."""

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

    return fig
