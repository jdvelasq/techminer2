"""
Line Plot
===============================================================================


Smoke tests:
    >>> from techminer2.analyze.metrics.performance import LinePlot
    >>> plot = (
    ...     LinePlot()
    ...     #
    ...     # FIELD:
    ...     .with_field("author_keywords")
    ...     #
    ...     # TERMS:
    ...     .having_items_in_top(10)
    ...     .having_items_ordered_by("OCC")
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     # PLOT:
    ...     .using_title_text("Line Plot")
    ...     .using_xaxes_title_text("Author Keywords")
    ...     .using_yaxes_title_text("OCC")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("examples/tests/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     #
    ...     .run()
    ... )
    >>> plot.write_html("docs_source/_generated/px.database.metrics.performance.line_plot.html")

.. raw:: html

    <iframe src="../_generated/px.database.metrics.performance.line_plot.html"
    height="600px" width="100%" frameBorder="0"></iframe>


"""

from techminer2._internals import ParamsMixin
from techminer2._internals.plots.line_plot import line_plot
from techminer2.report.visualization.dataframe import DataFrame


class LinePlot(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        data_frame = DataFrame().update(**self.params.__dict__).run()

        if self.params.title_text is None:
            self.using_title_text("Column Plot")

        if self.params.xaxes_title_text is None:
            self.using_xaxes_title_text(
                self.params.field.replace("_", " ").upper() + " RANK"
            )

        if self.params.yaxes_title_text is None:
            self.using_yaxes_title_text(
                self.params.items_order_by.replace("_", " ").upper()
            )

        fig = line_plot(params=self.params, dataframe=data_frame)

        return fig


#
