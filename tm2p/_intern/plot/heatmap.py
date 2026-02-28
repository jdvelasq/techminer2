import numpy as np
import pandas as pd  # type: ignore
import plotly.express as px  # type: ignore
import plotly.graph_objects as go  # type: ignore

from tm2p._intern import Params

MARKER_COLOR = "#7793a5"
MARKER_LINE_COLOR = "#465c6b"


def heatmap(
    params: Params,
    dataframe: pd.DataFrame,
) -> go.Figure:

    fig = px.imshow(
        dataframe,
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
    x_min, x_max = full_fig["layout"]["xaxis"]["range"]
    y_max, y_min = full_fig["layout"]["yaxis"]["range"]

    for value in np.linspace(x_min, x_max, dataframe.shape[1] + 1):
        fig.add_vline(
            x=value,
            line_width=2,
            line_color="lightgray",
        )

    for value in np.linspace(y_min, y_max, dataframe.shape[0] + 1):
        fig.add_hline(
            y=value,
            line_width=2,
            line_color="lightgray",
        )

    return fig
