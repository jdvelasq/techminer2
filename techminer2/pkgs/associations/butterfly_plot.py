# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Butterfly Plot
===============================================================================


>>> from techminer2.pkgs.associations import ButterflyPlot
>>> plot = (
...     ButterflyPlot()
...     #
...     # FIELD:
...     .with_field("author_keywords")
...     .having_terms_in_top(10)
...     .having_terms_ordered_by("OCC")
...     .having_term_occurrences_between(None, None)
...     .having_term_citations_between(None, None)
...     .having_terms_in(["FINTECH", "INNOVATION", "FINANCIAL_SERVICES"])
...     #
...     # ROWS:
...     .having_other_terms_in_top(10)
...     .having_other_terms_ordered_by("OCC")
...     .having_other_term_occurrences_between(None, None)
...     .having_other_term_citations_between(None, None)
...     .having_other_terms_in(None)
...     #
...     # COUNTERS:
...     .using_term_counters(True)
...     #
...     # CHART PARAMS:
...     .using_title_text("Butterfly Plot")
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     .where_records_match(None)
...     #
...     .build()
... )
>>> # plot.write_html("sphinx/_generated/pkgs/associations/butterfly_plot.html")

.. raw:: html

    <iframe src="../../_generated/pkgs/associations/butterfly_plot.html" 
    height="800px" width="100%" frameBorder="0"></iframe>


"""
import plotly.graph_objects as go  # type: ignore

from ...internals.mixins import InputFunctionsMixin
from .data_frame import DataFrame


class ButterflyPlot(
    InputFunctionsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def _step_01_create_data_frame(self):
        return DataFrame().update_params(**self.params.__dict__).build()

    # -------------------------------------------------------------------------
    def _step_02_remove_col_terms_from_index(self, matrix):
        return matrix.drop(index=matrix.columns)

    # -------------------------------------------------------------------------
    def _step_03_build_butterfly_plot(self, matrix):

        name_a = matrix.columns[0]
        name_b = matrix.columns[1]

        x_max_value = matrix.max().max()

        title_text = self.params.title_text
        if title_text == "":
            title_text = "Butterfly Plot"

        fig = go.Figure()

        fig.add_trace(
            go.Bar(
                y=matrix.index,
                x=matrix[name_a],
                name=name_a,
                orientation="h",
                marker={"color": "#7793a5"},
            )
        )

        fig.add_trace(
            go.Bar(
                y=matrix.index,
                x=matrix[name_b].map(lambda w: -w),
                name=name_b,
                orientation="h",
                marker={"color": "#465c6b"},
            )
        )

        fig.update_layout(barmode="overlay")

        fig.update_layout(
            paper_bgcolor="white",
            plot_bgcolor="white",
            title_text=title_text,
        )
        fig.add_vline(
            x=0.0,
            line={
                "color": "lightgray",
                "width": 2,
                "dash": "dot",
            },
        )

        fig.update_xaxes(
            linecolor="gray",
            linewidth=2,
            gridcolor="lightgray",
            griddash="dot",
            title_text="OCC",
        )
        fig.update_yaxes(
            linecolor="white",
            linewidth=0,
            autorange="reversed",
            gridcolor="lightgray",
            griddash="dot",
            # title_text=field_label,
        )

        # sets xaxis range to (-x_max_value, x_max_value)
        fig.update_layout(
            xaxis_range=[-x_max_value, x_max_value],
        )

        # sets the legend position upper left
        fig.update_layout(
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1,
            )
        )

        return fig

    # -------------------------------------------------------------------------
    def build(self):
        matrix = self._step_01_create_data_frame()
        col_terms = self._step_02_remove_col_terms_from_index(matrix)
        return self._step_03_build_butterfly_plot(matrix)
