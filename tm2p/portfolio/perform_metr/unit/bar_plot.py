"""
BarPlot
===============================================================================

.. raw:: html

    <iframe src="../_generated/px.portfolio.performance_metrics.item_metrics.bar_plot.html"
    height="450" width="100%" frameBorder="0"></iframe>

Smoke tests:
    >>> from tm2p.enum import Field, UnitOrderBy
    >>> from tm2p.portfolio.perform_metr.item_metrics import BarPlot
    >>> plot = (
    ...     BarPlot()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.SRC_ISO4)
    ...     #
    ...     # TERMS:
    ...     .having_top_n_units(10)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
    ...     #
    ...     # PLOT:
    ...     .using_title_text("Bar Plot")
    ...     .using_xaxes_title_text("Occurrences")
    ...     .using_yaxes_title_text("OCC")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     #
    ...     .run()
    ... )
    >>> type(plot).__name__
    'Figure'
    >>> plot.write_html("docsrc/_generated/px.portfolio.performance_metrics.item_metrics.bar_plot.html")

"""

from tm2p._intern import ParamsMixin
from tm2p._intern.plots.basic.bar_plot import bar_plot

from .metr import Metrics


class BarPlot(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        df = Metrics().update(**self.params.__dict__).run()
        fig = bar_plot(params=self.params, df=df)

        return fig
