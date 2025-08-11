# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Bar Plot
===============================================================================



This module demonstrates how to create a collaboration bar plot using the BarPlot class.
The process involves configuring the field, plot settings, and database parameters.


Example:
    >>> from techminer2.database.metrics.collaboration import BarPlot

    >>> # Creates, runs, and saves the plot to disk
    >>> plotter = (
    ...     BarPlot()
    ...     #
    ...     # FIELD:
    ...     .with_field("countries")
    ...     .having_terms_in_top(10)
    ...     .having_term_occurrences_between(None, None)
    ...     .having_term_citations_between(None, None)
    ...     .having_terms_ordered_by("OCC")
    ...     .having_terms_in(None)
    ...     #
    ...     # PLOT:
    ...     .using_title_text("Collaboration Plot")
    ...     .using_xaxes_title_text("Countries")
    ...     .using_yaxes_title_text("OCC")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory_is("examples/fintech/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ...     .where_records_match(None)
    ... )
    >>> plot = plotter.run()
    >>> plot.write_html("docs_source/_generated/px.database.metrics.collaboration.bar_plot.html")

.. raw:: html

    <iframe src="../_generated/px.database.metrics.collaboration.bar_plot.html"
    height="600px" width="100%" frameBorder="0"></iframe>




"""
import plotly.express as px  # type: ignore
from techminer2._internals.params_mixin import ParamsMixin
from techminer2.database.metrics.collaboration.data_frame import DataFrame


class BarPlot(
    ParamsMixin,
):
    """:meta private:"""

    def get_collaboration_metrics(self):
        return DataFrame().update(**self.params.__dict__).run()

    def build_collaboration_bar_plot(self, metrics):

        field = self.params.field
        title_text = self.params.title_text
        xaxes_title_text = self.params.xaxes_title_text
        yaxes_title_text = self.params.yaxes_title_text

        if title_text is None:
            title_text = "Corresponding Author's " + field.title()

        if xaxes_title_text is None:
            xaxes_title_text = "Num Documents"

        if yaxes_title_text is None:
            yaxes_title_text = field.title()

        metrics = metrics.copy()
        metrics = metrics.reset_index()

        metrics = metrics.melt(
            id_vars=field,
            value_vars=[
                "single_publication",
                "multiple_publication",
            ],
        )
        metrics = metrics.rename(
            columns={
                "variable": "publication",
                "value": "Num Documents",
            }
        )
        metrics.publication = metrics.publication.map(
            lambda x: x.replace("_", " ").title()
        )
        metrics[field] = metrics[field].map(lambda x: x.title())

        fig = px.bar(
            metrics,
            x="Num Documents",
            y=field,
            color="publication",
            title=title_text,
            hover_data=["Num Documents"],
            orientation="h",
            color_discrete_map={
                "Single Publication": "#7793a5",
                "Multiple Publication": "#465c6b",
            },
        )
        fig.update_layout(
            paper_bgcolor="white",
            plot_bgcolor="white",
        )
        fig.update_yaxes(
            linecolor="gray",
            linewidth=2,
            autorange="reversed",
            title_text=yaxes_title_text,
        )
        fig.update_xaxes(
            linecolor="gray",
            linewidth=2,
            gridcolor="gray",
            griddash="dot",
            title_text=xaxes_title_text,
        )

        return fig

    def run(self):

        metrics = self.get_collaboration_metrics()
        fig = self.build_collaboration_bar_plot(metrics)
        return fig


#
#
