# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""Base Heatmap Class."""
import numpy as np
import plotly.express as px  # type: ignore

MARKER_COLOR = "#7793a5"
MARKER_LINE_COLOR = "#465c6b"


def internal__heatmap(params, data_frame):

    fig = px.imshow(
        data_frame,
        color_continuous_scale=params.colormap,
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
