# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""Pie Plot Mixin."""

from dataclasses import dataclass
from typing import Optional

import plotly.express as px  # type: ignore


@dataclass
class RankingPlotParams:
    """:meta private:"""

    title_text: Optional[str] = None
    xaxes_label: Optional[str] = None
    yaxes_label: Optional[str] = None
