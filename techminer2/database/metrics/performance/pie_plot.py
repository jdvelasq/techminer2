# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Pie Plot
===============================================================================


>>> from techminer2.database.metrics.performance import PiePlot
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
...     .where_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     #
...     .build()
... )
>>> # plot.write_html("sphinx/_generated/database/metrics/performance/pie_plot.html")

.. raw:: html

    <iframe src="../../../_generated/database/metrics/performance/pie_plot.html" 
    height="600px" width="100%" frameBorder="0"></iframe>


"""
from ...._internals.params_mixin import ParamsMixin
from ...._internals.plots.internal__pie_plot import internal__pie_plot
from .data_frame import DataFrame


class PiePlot(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):

        data_frame = DataFrame().update(**self.params.__dict__).build()

        if self.params.title_text is None:
            self.using_title_text("Pie Plot")

        fig = internal__pie_plot(params=self.params, data_frame=data_frame)

        return fig
