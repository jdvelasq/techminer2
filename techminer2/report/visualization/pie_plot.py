"""
Pie Plot
===============================================================================


Smoke tests:
    >>> from techminer2.analyze.metrics.performance import PiePlot
    >>> plot = (
    ...     PiePlot()
    ...     #
    ...     # FIELD:
    ...     .with_field("author_keywords")
    ...     #
    ...     # TERMS:
    ...     .having_terms_in_top(15)
    ...     .having_terms_ordered_by("OCC")
    ...     .having_term_occurrences_between(None, None)
    ...     .having_term_citations_between(None, None)
    ...     .having_terms_in(None)
    ...     #
    ...     # PLOT:
    ...     .using_title_text("Most Frequent Author Keywords")
    ...     .using_pie_hole(0.4)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("examples/tests/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     #
    ...     .run()
    ... )
    >>> plot.write_html("docs_source/_generated/px.database.metrics.performance.pie_plot.html")

.. raw:: html

    <iframe src="../_generated/px.database.metrics.performance.pie_plot.html"
    height="600px" width="100%" frameBorder="0"></iframe>


"""

from techminer2._internals import ParamsMixin
from techminer2._internals.plots.pie_plot import pie_plot
from techminer2.report.visualization.dataframe import DataFrame


class PiePlot(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        data_frame = DataFrame().update(**self.params.__dict__).run()

        if self.params.title_text is None:
            self.using_title_text("Pie Plot")

        fig = pie_plot(params=self.params, dataframe=data_frame)

        return fig


#
