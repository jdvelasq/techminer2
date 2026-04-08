"""
StrenghtPlot
===============================================================================

.. raw:: html

    <iframe src="../_generated/px.portfolio.thematic_stucture.co_occurrence.first_order_network.strength_plot_1.html"
    height="800px" width="100%" frameBorder="0"></iframe>

    <iframe src="../_generated/px.portfolio.thematic_stucture.co_occurrence.first_order_network.strength_plot_2.html"
    height="800px" width="100%" frameBorder="0"></iframe>

Smoke tests:
    >>> from tm2p.enum import Field, AssociationIndex, ItemOrderBy
    >>> from tm2p.portfolio.thematic_stucture.co_occurrence.first_order_network import StrengthPlot
    >>> fig = (
    ...     StrengthPlot()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.AUTHKW_NORM)
    ...     .having_items_in_top(20)
    ...     .having_items_ordered_by(ItemOrderBy.OCC)
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # NETWORK:
    ...     .using_association_index(AssociationIndex.ASSOCIATION_STRENGTH)
    ...     #
    ...     # PLOT:
    ...     .using_line_color("black")
    ...     .using_line_width(1.5)
    ...     .using_marker_size(7)
    ...     .using_textfont_size(10)
    ...     .using_yshift(4)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> type(fig).__name__
    'Figure'
    >>> fig.write_html("docsrc/_generated/px.portfolio.thematic_stucture.co_occurrence.first_order_network.strength_plot_1.html")

    >>> fig = (
    ...     StrengthPlot()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.AUTHKW_NORM)
    ...     .having_items_in_top(20)
    ...     .having_items_ordered_by(ItemOrderBy.OCC)
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(False)
    ...     #
    ...     # NETWORK:
    ...     .using_association_index(AssociationIndex.ASSOCIATION_STRENGTH)
    ...     #
    ...     # PLOT:
    ...     .using_line_color("black")
    ...     .using_line_width(1.5)
    ...     .using_marker_size(7)
    ...     .using_textfont_size(10)
    ...     .using_yshift(4)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> fig.write_html("docsrc/_generated/px.portfolio.thematic_stucture.co_occurrence.first_order_network.strength_plot_2.html")


"""

from tm2p._intern import ParamsMixin
from tm2p._intern.nx import create_node_degree_plot

from .node_metrics import NodeMetrics


class StrengthPlot(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        use_counters = self.params.counters

        self.params.counters = True
        metrics = NodeMetrics().update(**self.params.__dict__).run()
        metrics = metrics.reset_index().rename(columns={"index": "NODE"})
        if use_counters is False:
            self.params.counters = False
            metrics["NODE"] = metrics["NODE"].str.split(" ").str[:-1].str.join(" ")
        plot = create_node_degree_plot(self.params, metrics)

        return plot
