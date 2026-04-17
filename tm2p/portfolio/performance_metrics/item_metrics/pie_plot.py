"""
PiePlot
===============================================================================

.. raw:: html

    <iframe src="../_generated/px.portfolio.performance_metrics.item_metrics.pie_plot.html"
    height="600px" width="100%" frameBorder="0"></iframe>


Smoke tests:
    >>> from tm2p.enum import Field, UnitOrderBy
    >>> from tm2p.portfolio.performance_metrics.item_metrics import PiePlot
    >>> plot = (
    ...     PiePlot()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.AUTHKW_NORM)
    ...     #
    ...     # TERMS:
    ...     .having_top_n_units(15)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
    ...     #
    ...     # PLOT:
    ...     .using_title_text("Most Frequent Author Keywords")
    ...     .using_pie_hole(0.4)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     #
    ...     .run()
    ... )
    >>> type(plot).__name__
    'Figure'
    >>> plot.write_html("docsrc/_generated/px.portfolio.performance_metrics.item_metrics.pie_plot.html")



"""

from tm2p._intern import ParamsMixin
from tm2p._intern.plots.basic.pie_plot import pie_plot

from .metrics import Metrics


class PiePlot(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        df = Metrics().update(**self.params.__dict__).run()
        fig = pie_plot(params=self.params, dataframe=df)

        return fig


#
