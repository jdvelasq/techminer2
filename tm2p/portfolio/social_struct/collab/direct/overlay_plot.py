"""
Network Plot
===============================================================================

.. raw:: html

    <iframe src="../_generated/px.portfolio.social_struct.collab.direct.overlay_plot.html"
    height="800px" width="100%" frameBorder="0"></iframe>

Smoke tests:
    >>> from tm2p.enum import AssociationIndex, AnalysisUnit, GraphClusteringAlgorithm, UnitOrderBy, Scaling, NodeSizeMetric
    >>> from tm2p.portfolio.social_struct.collab.direct import OverlayPlot
    >>> fig = (
    ...     OverlayPlot()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.AUTH)
    ...     #
    ...     .having_top_n_units(50)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
    ...     #
    ...     .using_minimum_pair_co_occurrence(1)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(False)
    ...     #
    ...     # NORMALIZATION:
    ...     .using_association_index(AssociationIndex.ASSOCIATION_STRENGTH)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering(GraphClusteringAlgorithm.LOUVAIN)
    ...     .using_max_recursive_clustering_depth(1)
    ...     .using_min_recursive_cluster_size(8)    
    ...     #
    ...     # PLOT:
    ...     .using_spring_layout_k(0.2)
    ...     .using_spring_layout_iterations(10)
    ...     .using_spring_layout_seed(0)
    ...     #
    ...     .using_colorscale(
    ...         [
    ...             [0.00, "#2C7BB6"],
    ...             [0.35, "#00A6CA"],
    ...             [0.65, "#4EBA6F"],
    ...             [1.00, "#F28E2B"],
    ...         ]
    ...     )
    ...     .using_uniform_node_opacity(0.75)
    ...     .using_node_size_metric(NodeSizeMetric.TLS)
    ...     .using_node_scaling(Scaling.SQRT)
    ...     .using_node_size_range(12, 80)
    ...     .using_top_n_nodes(50)
    ...     .using_min_node_degree(2)
    ...     #
    ...     .using_max_node_labels(15)
    ...     .using_node_label_max_length(20)
    ...     #
    ...     .using_textfont_opacity_range(0.55, 1.00)
    ...     .using_textfont_size_range(10, 24)
    ...     #
    ...     # https://www.w3schools.com/colors/colors_shades.asp
    ...     .using_uniform_edge_color("#d8d8d8")
    ...     .using_edge_opacity_range(0.25, 0.65)
    ...     .using_edge_scaling(Scaling.SQRT)
    ...     .using_global_top_edges(200)
    ...     .using_edge_width_range(1.5, 5.0)
    ...     .using_top_edges_per_node(5)
    ...     #
    ...     .using_xaxes_range(None, None)
    ...     .using_yaxes_range(None, None)
    ...     .using_axes_visible(False)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> assert type(fig).__name__ == 'Figure'    
    >>> fig.write_html("docsrc/_generated/px.portfolio.social_struct.collab.direct.overlay_plot.html")


"""

from tm2p._intern import ParamsMixin
from tm2p._intern.plots.adv.co_occ_overlay_plot import build_co_occ_overlay_plot
from tm2p.portfolio.perform_metr.trend.trend import Trends

from .count_matrix import CountMatrix as CoOccurrenceMatrix
from .direct_matrix import DirectMatrix
from .unit_to_cluster import UnitToCluster


class OverlayPlot(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        similarity_matrix = (
            DirectMatrix().update(**self.params.__dict__).using_counters(True).run()
        )
        co_occ_matrix = (
            CoOccurrenceMatrix()
            .update(**self.params.__dict__)
            .using_counters(True)
            .run()
        )

        trends = Trends().update(**self.params.__dict__).run()
        years = trends.columns.astype(int)
        avg_year = (trends * years).sum(axis=1) / trends.sum(axis=1)
        avg_year = avg_year.round(1)

        i2y = dict(zip(trends.index, avg_year))

        i2c = UnitToCluster().update(**self.params.__dict__).using_counters(True).run()

        fig = build_co_occ_overlay_plot(
            params=self.params,
            similarity_matrix=similarity_matrix,
            co_occurrence_matrix=co_occ_matrix,
            i2c=i2c,
            i2y=i2y,
        )

        return fig
