"""
NetworkPlot
===============================================================================

.. raw:: html

    <iframe src="../_generated/px.synthes.netw.co_occur.network_plot.html"
    height="800px" width="100%" frameBorder="0"></iframe>

Smoke tests:
    >>> from tm2p.enum import AssociationIndex  # type: ignore
    >>> from tm2p.enum import AnalysisUnit  # type: ignore
    >>> from tm2p.enum import GraphClusteringAlgorithm  # type: ignore
    >>> from tm2p.enum import NodeSizeMetric  # type: ignore
    >>> from tm2p.enum import Scaling  # type: ignore
    >>> from tm2p.enum import UnitOrderBy  # type: ignore
    >>> from tm2p.portfolio.thematic_struct.co_occur.dir_simil_netw import NetworkPlot  # type: ignore
    >>> fig = (
    ...     NetworkPlot()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.KW)
    ...     #
    ...     .having_top_n_units(50)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
    ...     #
    ...     .using_minimum_pair_co_occurrence(2)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(False)
    ...     #
    ...     # NORMALIZATION:
    ...     .using_association_index(AssociationIndex.ASSOCIATION_STRENGTH)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering(GraphClusteringAlgorithm.LOUVAIN)
    ...     #
    ...     # NETWORK:
    ...     .using_spring_layout_k(0.27)
    ...     .using_spring_layout_iterations(100)
    ...     .using_spring_layout_seed(0)
    ...     #
    ...     .using_discrete_node_colors(
    ...         (
    ...             "#1f77b4",
    ...             "#ff7f0e",
    ...             "#2ca02c",
    ...             "#d62728",
    ...             "#9467bd",
    ...             "#8c564b",
    ...             "#e377c2",
    ...             "#7f7f7f",
    ...             "#bcbd22",
    ...             "#17becf",
    ...         )
    ...     )
    ...     .using_min_node_degree(2)
    ...     .using_node_scaling(Scaling.SQRT)
    ...     .using_node_size_metric(NodeSizeMetric.TLS)
    ...     .using_node_size_range(12, 80)
    ...     .using_top_n_nodes(50)
    ...     .using_uniform_node_opacity(0.75)
    ...     #
    ...     .using_max_node_labels(15)
    ...     .using_node_label_max_length(20)
    ...     #
    ...     .using_textfont_opacity_range(0.55, 1.00)
    ...     .using_textfont_size_range(10, 24)
    ...     #
    ...     # https://www.w3schools.com/colors/colors_shades.asp
    ...     .using_edge_opacity_range(0.25, 0.65)
    ...     .using_edge_scaling(Scaling.SQRT)
    ...     .using_edge_width_range(1.5, 5.0)
    ...     .using_global_top_edges(200)
    ...     .using_top_edges_per_node(5)
    ...     .using_uniform_edge_color("#d8d8d8")
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
    >>> fig.write_html("docsrc/_generated/px.synthes.netw.co_occur.network_plot.html")


"""

from tm2p._intern import ParamsMixin
from tm2p._intern.plots.adv.co_occ_netw_plot import build_co_occ_network_plot

from .dir_matrix import DirectMatrix
from .item_to_clust import ItemToCluster
from .matrix import Matrix as CoOccurrenceMatrix


class NetworkPlot(
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

        i2c = ItemToCluster().update(**self.params.__dict__).using_counters(True).run()

        fig = build_co_occ_network_plot(
            params=self.params,
            similarity_matrix=similarity_matrix,
            co_occurrence_matrix=co_occ_matrix,
            i2c=i2c,
        )

        return fig
