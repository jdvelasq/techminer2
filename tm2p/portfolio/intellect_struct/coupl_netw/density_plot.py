"""
DensityPlot
===============================================================================

.. raw:: html

    <iframe src="../_generated/px.portfolio.intellectual_structure.coupling_network.density_plot_doc.html"
    height="800px" width="100%" frameBorder="0"></iframe>

Smoke tests:
    >>> from tm2p.enum import AssociationIndex, AnalysisUnit, GraphClusteringAlgorithm, UnitOrderBy, Scaling, NodeSizeMetric
    >>> from tm2p.portfolio.intellect_struct.coupl_netw import DensityPlot
    >>> fig = (
    ...     DensityPlot()
    ...     #
    ...     # COUPLING UNIT:
    ...     .with_analysis_unit(AnalysisUnit.DOC)
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
    ...     # PLOT:
    ...     .using_spring_layout_k(0.27)
    ...     .using_spring_layout_iterations(100)
    ...     .using_spring_layout_seed(0)
    ...     #
    ...     .using_colorscale(
    ...         [
    ...             [0.00, "#081D58"],
    ...             [0.25, "#163A63"],
    ...             [0.50, "#1D6FA5"],
    ...             [0.72, "#2FB7B5"],
    ...             [0.88, "#A5DB36"],
    ...             [0.96, "#FDE725"],
    ...             [1.00, "#F46D43"],
    ...         ]
    ...     )
    ...     .using_node_size_metric(NodeSizeMetric.TLS)
    ...     .using_node_scaling(Scaling.SQRT)
    ...     .using_top_n_nodes(50)
    ...     .using_min_node_degree(2)
    ...     #
    ...     .using_max_node_labels(100)
    ...     .using_node_label_max_length(20)
    ...     #
    ...     .using_textfont_opacity_range(0.85, 1.00)
    ...     .using_textfont_size_range(12, 20)
    ...     #
    ...     .using_kernel_bandwidth(0.1)
    ...     .using_contour_opacity(1.0)
    ...     #
    ...     .using_edge_scaling(Scaling.SQRT)
    ...     .using_global_top_edges(200)
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
    >>> assert type(fig).__name__ == 'Figure'    >>> fig.write_html("docsrc/_generated/px.portfolio.intellectual_structure.coupling_network.density_plot_doc.html")

* **AnalysisUnit.AUTH** /  **AnalysisUnit.CTRY** /  / **AnalysisUnit.ORG** / **AnalysisUnit.SRC**

"""

from tm2p._intern import ParamsMixin
from tm2p._intern.plots.adv.co_occ_dens_plot import build_co_occ_density_plot

from .direct_matrix import DirectMatrix
from .item_to_cluster import ItemToCluster
from .matrix import Matrix as CouplingMatrix


class DensityPlot(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        similarity_matrix = (
            DirectMatrix().update(**self.params.__dict__).using_counters(True).run()
        )
        co_occ_matrix = (
            CouplingMatrix().update(**self.params.__dict__).using_counters(True).run()
        )

        i2c = ItemToCluster().update(**self.params.__dict__).using_counters(True).run()

        fig = build_co_occ_density_plot(
            params=self.params,
            similarity_matrix=similarity_matrix,
            co_occurrence_matrix=co_occ_matrix,
            i2c=i2c,
        )

        return fig
