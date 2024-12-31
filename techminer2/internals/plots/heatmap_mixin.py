# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""Base Heatmap Class."""


from dataclasses import dataclass
from typing import Optional

import numpy as np
import plotly.express as px  # type: ignore

MARKER_COLOR = "#7793a5"
MARKER_LINE_COLOR = "#465c6b"


@dataclass
class HeatmapParams:
    """:meta private:"""

    title_text: Optional[str] = None
    colormap: str = "Blues"


class HeatmapMixin:

    def set_plot_params(self, **kwars):
        for key, value in kwars.items():
            if hasattr(self.plot_params, key):
                setattr(self.plot_params, key, value)
            else:
                raise ValueError(f"Invalid parameter for HeatmapParams: {key}")
        return self

    def build_heatmap(self, dataframe):

        fig = px.imshow(
            dataframe,
            color_continuous_scale=self.plot_params.colormap,
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

        for value in np.linspace(x_min, x_max, dataframe.shape[1] + 1):
            fig.add_vline(x=value, line_width=2, line_color="lightgray")

        for value in np.linspace(y_min, y_max, dataframe.shape[0] + 1):
            fig.add_hline(y=value, line_width=2, line_color="lightgray")

        return fig
