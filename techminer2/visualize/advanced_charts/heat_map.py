# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Heat Map
===============================================================================

>>> from techminer2.visualize.advanced_charts import HeatMap
>>> plot = (
...     HeatMap()
...     .set_column_params(
...         field="author_keywords",
...         top_n=10,
...         occ_range=(None, None),
...         gc_range=(None, None),
...         custom_terms=None,
...     ).set_row_params(
...         field=None,
...         top_n=None,
...         occ_range=(None, None),
...         gc_range=(None, None),
...         custom_terms=None,
...     ).set_cbart_params(
...         title_text=None,
...         colormap="Blues",
...     ).set_database_params(
...         root_dir="example/", 
...         database="main",
...         year_filter=(None, None),
...         cited_by_filter=(None, None),
...     ).build()
... )
>>> # plot.write_html("sphinx/_generated/visualize/advanced_charts/heat_map.html")

.. raw:: html

    <iframe src="../../_generated/visualize/advanced_charts/heat_map.html" 
    height="800px" width="100%" frameBorder="0"></iframe>



"""
from dataclasses import dataclass
from typing import Optional

import numpy as np
import plotly.express as px  # type: ignore

from ...analyze.co_occurrence_matrix.co_occurrence_matrix import CoOccurrenceMatrix
from ...analyze.co_occurrence_matrix.format_params import (
    FormatParams,
    FormatParamsMixin,
)
from ...internals.params.column_and_row_params import ColumnAndRowParamsMixin
from ...internals.params.database_params import DatabaseParams, DatabaseParamsMixin
from ...internals.params.item_params import ItemParams


@dataclass
class ChartParams:
    """:meta private:"""

    title_text: Optional[str] = None
    colormap: str = "Blues"


class ChartParamsMixin:
    """:meta private:"""

    def set_cbart_params(self, **kwars):
        for key, value in kwars.items():
            if hasattr(self.chart_params, key):
                setattr(self.chart_params, key, value)
            else:
                raise ValueError(f"Invalid parameter for ChartParams: {key}")
        return self


class HeatMap(
    ChartParamsMixin,
    ColumnAndRowParamsMixin,
    DatabaseParamsMixin,
    FormatParamsMixin,
):
    """:meta private:"""

    def __init__(self):
        self.chart_params = ChartParams()
        self.column_params = ItemParams()
        self.database_params = DatabaseParams()
        self.row_params = ItemParams()
        self.format_params = FormatParams()

    def build(self):

        matrix = (
            CoOccurrenceMatrix()
            .set_column_params(**self.column_params.__dict__)
            .set_row_params(**self.row_params.__dict__)
            .set_format_params(**self.format_params.__dict__)
            .set_database_params(**self.database_params.__dict__)
            .build()
        )

        fig = px.imshow(
            matrix,
            color_continuous_scale=self.chart_params.colormap,
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

        for value in np.linspace(x_min, x_max, matrix.shape[1] + 1):
            fig.add_vline(x=value, line_width=2, line_color="lightgray")

        for value in np.linspace(y_min, y_max, matrix.shape[0] + 1):
            fig.add_hline(y=value, line_width=2, line_color="lightgray")

        return fig
