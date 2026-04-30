"""
NetworkPlot
===============================================================================

* **CITED_REF** / **CITED_AUTH** / **CITED_SRC**

.. raw:: html

    <iframe src="../_static/px.portfolio.intellect_struct.co_cit_netw.latent.netw_plot_cited_auth.html"
    height="600px" width="100%" frameBorder="0"></iframe>


Smoke tests:
    >>> from tm2p.enum import AssociationIndex  # type: ignore
    >>> from tm2p.enum import AnalysisUnit  # type: ignore
    >>> from tm2p.enum import GraphClusteringAlgorithm  # type: ignore
    >>> from tm2p.enum import NodeSizeMetric  # type: ignore
    >>> from tm2p.enum import Scaling  # type: ignore
    >>> from tm2p.portfolio.intellect_struct.co_cit_netw.latent import NetworkPlot  # type: ignore
    >>> plot = (
    ...     NetworkPlot()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.CITED_REF)
    ...     #
    ...     .having_top_n_cited_units(40)
    ...     .having_minimum_cited_unit_occurrences(3)
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
    ...     # NETWORK:
    ...     .using_spring_layout_k(0.30)
    ...     .using_spring_layout_iterations(50)
    ...     .using_spring_layout_seed(5)
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
    ...     .using_uniform_node_opacity(0.75)
    ...     .using_node_size_metric(NodeSizeMetric.OCC)
    ...     .using_node_scaling(Scaling.SQRT)
    ...     .using_node_size_range(12, 80)
    ...     .using_top_n_nodes(50)
    ...     .using_min_node_degree(2)
    ...     #
    ...     .using_max_node_labels(20)
    ...     .using_node_label_max_length(40)
    ...     #
    ...     .using_textfont_opacity_range(0.55, 1.00)
    ...     .using_textfont_size_range(10, 24)
    ...     #
    ...     # https://www.w3schools.com/colors/colors_shades.asp
    ...     .using_uniform_edge_color("#d8d8d8")
    ...     .using_edge_opacity_range(0.25, 0.65)
    ...     .using_edge_scaling(Scaling.SQRT)
    ...     .using_global_top_edges(100)
    ...     .using_edge_width_range(1.5, 5.0)
    ...     .using_top_edges_per_node(5)
    ...     #
    ...     .using_xaxes_range(None, None)
    ...     .using_yaxes_range(None, None)
    ...     .using_axes_visible(False)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/system-dynamics-wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> plot.write_html("docsrc/_generated/px.portfolio.intellect_struct.co_cit_netw.latent.netw_plot_cited_auth.html")

"""

from tm2p._intern import ParamsMixin
from tm2p._intern.plots.adv.co_occ_netw_plot import build_co_occ_network_plot

from ..direct.matrix import Matrix as CoOccurrenceMatrix
from .item_to_cluster import ItemToCluster
from .latent_matrix import LatentMatrix


class NetworkPlot(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        similarity_matrix = (
            LatentMatrix().update(**self.params.__dict__).using_counters(True).run()
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
