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
...     .with_source_field("author_keywords")
...     .select_top_n_terms(15)
...     .order_terms_by("OCC")
...     .having_term_occurrences_between(None, None)
...     .having_term_citations_between(None, None)
...     .having_terms_in(None)
...     #
...     .using_title_text("Most Frequent Author Keywords")
...     .using_pie_hole(0.4)
...     #
...     .where_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     #
...     .build()
... )
>>> plot.write_html("sphinx/_generated/database/metrics/performance/pie_plot.html")

.. raw:: html

    <iframe src="../../../_generated/database/metrics/performance/pie_plot.html" 
    height="600px" width="100%" frameBorder="0"></iframe>


"""
from ....internals.mixins.input_functions import InputFunctionsMixin
from ....internals.mixins.pie_plot import PiePlotMixin
from .data_frame import DataFrame


class PiePlot(
    InputFunctionsMixin,
    PiePlotMixin,
):
    """:meta private:"""

    def build(self):

        data_frame = DataFrame().update_params(**self.params.__dict__).build()

        if self.params.title_text is None:
            self.using_title_text("Pie Plot")

        fig = self.build_pie_plot(data_frame=data_frame)

        return fig
