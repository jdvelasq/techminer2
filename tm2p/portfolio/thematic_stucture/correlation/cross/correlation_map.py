"""
Cross-correlation Map
===============================================================================

.. raw:: html

    <iframe src="../_generated/px.portfolio.thematic_stucture.correlation.cross.correlation_map.html"
    height="800px" width="100%" frameBorder="0"></iframe>

Smoke tests:
    >>> # grey colors: https://www.w3schools.com/colors/colors_shades.asp
    >>> from tm2p.enum import UnitOrderBy, Field, Correlation, Scaling
    >>> from tm2p.portfolio.thematic_stucture.correlation.cross import CorrelationMap
    >>> plot = (
    ...     CorrelationMap()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.AUTHKW_NORM)
    ...     .having_top_n_units(20)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
    ...     #
    ...     # CORRELATION:
    ...     .with_cross_field(Field.CTRY_ISO3)
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
    ...     .using_max_node_labels(10)
    ...     #
    ...     .using_edge_colors(("#7793a5", "#7793a5", "#7793a5", "#7793a5"))
    ...     .using_edge_scaling(Scaling.SQRT)
    ...     .using_edge_similarity_threshold(0.60)
    ...     .using_global_top_edges(1000)
    ...     .using_edge_widths((1.0, 1.0, 2.0, 3.5))
    ...     .using_min_node_degree(2)
    ...     .using_top_edges_per_node(5)
    ...     #
    ...     .using_xaxes_range(None, None)
    ...     .using_yaxes_range(None, None)
    ...     .using_axes_visible(False)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> plot.write_html("docsrc/_generated/px.portfolio.thematic_stucture.correlation.cross.correlation_map.html")


"""

from tm2p._intern import ParamsMixin
from tm2p._intern.plots.advanced import build_correlation_map
from tm2p.portfolio.thematic_stucture.correlation.cross.matrix import Matrix


class CorrelationMap(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        matrix = Matrix().update(**self.params.__dict__).run()

        return build_correlation_map(self.params, matrix)
