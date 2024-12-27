# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""Cleveland Dot Plot Mixin."""

from dataclasses import dataclass
from typing import Optional

import plotly.express as px  # type: ignore


@dataclass
class ClevelandDotPlotParams:
    """:meta private:"""

    title_text: Optional[str] = None
    xaxes_label: Optional[str] = None
    yaxes_label: Optional[str] = None


class ClevelandDotPlotMixin:

    def set_plot_params(self, **kwars):
        for key, value in kwars.items():
            if hasattr(self.plot_params, key):
                setattr(self.plot_params, key, value)
            else:
                raise ValueError(f"Invalid parameter for ClevelandDotPlotParams: {key}")
        return self

    def build_cleveland_dot_plot(self, dataframe, y_col):
        pass
