# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Heat Map
===============================================================================

>>> import techminer2 as tm2
>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/heat_map.html"
>>> tm2.heat_map(
...     columns='author_keywords',
...     col_occ_range=(4, None),
...     root_dir=root_dir,
...     colormap="Blues",
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../../../../_static/heat_map.html" height="800px" width="100%" frameBorder="0"></iframe>


"""
import numpy as np
import plotly.express as px

from .co_occurrence_matrix import co_occurrence_matrix


def heat_map(
    #
    # CO-OCC PARAMS:
    columns,
    rows=None,
    #
    # FIG PARAMS:
    colormap="Blues",
    #
    # COLUMN PARAMS:
    col_top_n=None,
    col_occ_range=(None, None),
    col_gc_range=(None, None),
    col_custom_items=None,
    #
    # ROW PARAMS:
    row_top_n=None,
    row_occ_range=(None, None),
    row_gc_range=(None, None),
    row_custom_items=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """Make a heat map."""

    data_frame = co_occurrence_matrix(
        #
        # FUNCTION PARAMS:
        columns=columns,
        rows=rows,
        #
        # COLUMN PARAMS:
        col_top_n=col_top_n,
        col_occ_range=col_occ_range,
        col_gc_range=col_gc_range,
        col_custom_items=col_custom_items,
        #
        # ROW PARAMS:
        row_top_n=row_top_n,
        row_occ_range=row_occ_range,
        row_gc_range=row_gc_range,
        row_custom_items=row_custom_items,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

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