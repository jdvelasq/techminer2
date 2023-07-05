# flake8: noqa
# pylint: disable=line-too-long
"""
Heat Map
===============================================================================

* Preparation

>>> import techminer2plus as tm2p
>>> root_dir = "data/regtech/"


* Object oriented interface

>>> file_name = "sphinx/_static/heat_map_0.html"
>>> (
...     tm2p.records(root_dir=root_dir)
...     .co_occurrence_matrix(
...         columns='author_keywords',
...         rows='authors',
...         col_occ_range=(2, None),
...         row_occ_range=(2, None),
...     ).heat_map(
...         colormap="Blues"
...     )
...     .write_html("sphinx/_static/heat_map_0.html")
... )

.. raw:: html

    <iframe src="../../_static/heat_map_0.html" height="800px" width="100%" frameBorder="0"></iframe>

>>> file_name = "sphinx/_static/heat_map_1.html"
>>> (
...     tm2p.records(root_dir=root_dir)
...     .auto_correlation_matrix(
...         rows_and_columns='authors',
...         occ_range=(2, None),
...     ).heat_map(
...         colormap="Blues"
...     )
...     .write_html("sphinx/_static/heat_map_1.html")
... )

.. raw:: html

    <iframe src="../../_static/heat_map_1.html" height="800px" width="100%" frameBorder="0"></iframe>

    
>>> file_name = "sphinx/_static/heat_map_2.html"
>>> (
...     tm2p.records(root_dir=root_dir)
...     .cross_correlation_matrix(
...         rows_and_columns='authors', 
...         cross_with='countries',
...         top_n=10,
...     ).heat_map(
...         colormap="Blues"
...     )
...     .write_html("sphinx/_static/heat_map_2.html")
... )

.. raw:: html

    <iframe src="../../_static/heat_map_1.html" height="800px" width="100%" frameBorder="0"></iframe>    

* Functional interface

>>> matrix = tm2p.co_occurrence_matrix(
...    columns='author_keywords',
...    col_occ_range=(4, None),
...    root_dir=root_dir,
... )
>>> file_name = "sphinx/_static/heat_map_3.html"
>>> fig = tm2p.heat_map(
...     matrix,
...     colormap="Blues",
... )
>>> fig.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/heat_map_3.html" height="800px" width="100%" frameBorder="0"></iframe>




"""
import numpy as np
import plotly.express as px


def heat_map(
    obj,
    colormap="Blues",
):
    """Make a heat map."""

    data_frame = obj.df_.copy()

    fig = px.imshow(
        data_frame,
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
        margin={"l": 1, "r": 1, "t": 1, "b": 1},
    )

    full_fig = fig.full_figure_for_development()
    x_min, x_max = full_fig.layout.xaxis.range
    y_max, y_min = full_fig.layout.yaxis.range

    for value in np.linspace(x_min, x_max, data_frame.shape[1] + 1):
        fig.add_vline(x=value, line_width=2, line_color="lightgray")

    for value in np.linspace(y_min, y_max, data_frame.shape[0] + 1):
        fig.add_hline(y=value, line_width=2, line_color="lightgray")

    return fig
