"""
NetworkMap
===============================================================================

.. raw:: html

    <iframe src="../_generated/px.portfolio.thematic_stucture.correlation.auto.correlation_map.html"
    height="800px" width="100%" frameBorder="0"></iframe>


Smoke tests:
    >>> # grey colors: https://www.w3schools.com/colors/colors_shades.asp
    >>> from tm2p.enum import ItemOrderBy, Field, Correlation, Scaling
    >>> from tm2p.portfolio.thematic_stucture.correlation.auto import CorrelationMap
    >>> plot = (
    ...     CorrelationMap()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.KW_NORM)
    ...     .having_items_in_top(20)
    ...     .having_items_ordered_by(ItemOrderBy.OCC)
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     # CORRELATION:
    ...     .with_correlation_method(Correlation.PEARSON)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # MAP:
    ...     .using_spring_layout_k(None)
    ...     .using_spring_layout_iterations(100)
    ...     .using_spring_layout_seed(0)
    ...     #
    ...     .using_node_colors(("#7793a5",))
    ...     .using_node_scaling(Scaling.SQRT)
    ...     .using_node_size_range(18, 90)
    ...     .using_textfont_opacity_range(0.75, 1.00)
    ...     .using_textfont_size_range(11, 16)
    ...     .using_top_n_node_labels(5)
    ...     #
    ...     .using_edge_colors(("#7793a5", "#7793a5", "#7793a5", "#7793a5"))
    ...     .using_edge_scaling(Scaling.SQRT)
    ...     .using_edge_similarity_threshold(0.20)
    ...     .using_edge_top_n(1000)
    ...     .using_edge_widths((1.0, 1.0, 2.0, 3.5))
    ...     .using_min_edges_per_node(2)
    ...     .using_top_edges_per_node(5)
    ...     #
    ...     .using_xaxes_range(None, None)
    ...     .using_yaxes_range(None, None)
    ...     .using_axes_visible(False)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> plot.write_html("docsrc/_generated/px.portfolio.thematic_stucture.correlation.auto.correlation_map.html")



"""

from tm2p._intern import ParamsMixin
from tm2p._intern.plots.advanced import build_correlation_map

from .matrix import Matrix


class CorrelationMap(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        matrix = Matrix().update(**self.params.__dict__).using_counters(True).run()

        return build_correlation_map(self.params, matrix)
