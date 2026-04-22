"""
NetworkPlot
===============================================================================

* **AnalysisUnit.DOC**

.. raw:: html

    <iframe src="../_generated/px.synthes.netw.cit.network_plot_doc.html"
    height="800px" width="100%" frameBorder="0"></iframe>

Smoke tests:
    >>> from tm2p.enum import AssociationIndex, AnalysisUnit, GraphClusteringAlgorithm, Scaling
    >>> from tm2p.synthesize.netw.cit import NetworkPlot
    >>> # ---------------------------------------------------------------------
    >>> # DOC
    >>> # ---------------------------------------------------------------------
    >>> fig = (
    ...     NetworkPlot()
    ...     #
    ...     # CITATION UNIT:
    ...     .with_analysis_unit(AnalysisUnit.DOC)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering(GraphClusteringAlgorithm.LOUVAIN)
    ...     #
    ...     # NETWORK:
    ...     .using_spring_layout_intra_scale(1.0)
    ...     .using_spring_layout_cluster_scale(10.0)
    ...     .using_spring_layout_k(None)
    ...     .using_spring_layout_iterations(30)
    ...     .using_spring_layout_seed(0)
    ...     #
    ...     .using_node_colors(
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
    ...     .using_node_scaling(Scaling.SQRT)
    ...     .using_node_size_range(30, 70)
    ...     .using_textfont_opacity_range(0.35, 1.00)
    ...     .using_textfont_size_range(10, 20)
    ...     .using_max_node_labels(5)
    ...     .using_top_n_nodes(1000)
    ...     #
    ...     # https://www.w3schools.com/colors/colors_shades.asp
    ...     .using_uniform_edge_color("#e0e0e0")
    ...     .using_edge_scaling(Scaling.SQRT)
    ...     .using_global_top_edges(1000)
    ...     .using_edge_width_range(0.1, 3.0)
    ...     .using_min_node_degree(3)
    ...     .using_top_edges_per_node(5)
    ...     #
    ...     .using_xaxes_range(None, None)
    ...     .using_yaxes_range(None, None)
    ...     .using_axes_visible(False)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> fig.write_html("docsrc/_generated/px.synthes.netw.cit.network_plot_doc.html")



* **AnalysisUnit.AUTH** / **AnalysisUnit.CTRY** / **AnalysisUnit.ORG** / **AnalysisUnit.SRC**

.. raw:: html

    <iframe src="../_generated/px.synthes.netw.cit.network_plot_auth.html"
    height="800px" width="100%" frameBorder="0"></iframe>

Smoke tests:
    >>> # ---------------------------------------------------------------------
    >>> # AUTH
    >>> # ---------------------------------------------------------------------
    >>> fig = (
    ...     NetworkPlot()
    ...     #
    ...     # CITATION UNIT:
    ...     .with_analysis_unit(AnalysisUnit.AUTH)
    ...     .having_top_n_units(30)
    ...     .having_units_in(None)
    ...     .having_minimum_cited_unit_occurrences(0)
    ...     .having_occurrence_threshold(2)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering_algorithm_or_dict("louvain")
    ...     #
    ...     # NETWORK:
    ...     .using_spring_layout_k(None)
    ...     .using_spring_layout_iterations(30)
    ...     .using_spring_layout_seed(0)
    ...     #
    ...     .using_edge_colors(("#7793a5",))
    ...     .using_edge_width_range(0.8, 3.0)
    ...     .using_node_size_range(30, 70)
    ...     .using_textfont_opacity_range(0.35, 1.00)
    ...     .using_textfont_size_range(10, 20)
    ...     #
    ...     .using_xaxes_range(None, None)
    ...     .using_yaxes_range(None, None)
    ...     .using_axes_visible(False)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> fig.write_html("docsrc/_generated/px.synthes.netw.cit.network_plot_auth.html")




"""

from tm2p._intern.netw import BaseStrengthPlot

from .node_metric import NodeMetrics


class NetworkPlot(
    BaseStrengthPlot,
):
    """:meta private:"""

    def get_node_metrics(self):
        return


# from tm2p._intern import ParamsMixin
# from tm2p.enum import AnalysisUnit, UnitOrderBy
# from tm2p.portfolio.intellectual_structure.citation_network._intern.doc import (
#     DocNetworkPlot,
# )
# from tm2p.portfolio.intellectual_structure.citation_network._intern.other import (
#     OtherNetworkPlot,
# )

# from ...._intern.helpers.check_database import check_database


# class NetworkPlot(
#     ParamsMixin,
# ):
#     """:meta private:"""

#     def run(self):

#         check_database(self.params.root_directory)

#         if self.params.citation_unit == AnalysisUnit.DOC:
#             Plot = DocNetworkPlot
#         else:
#             Plot = OtherNetworkPlot

#         return (
#             Plot()
#             .update(**self.params.__dict__)
#             .update(items_order_by=UnitOrderBy.OCC)
#             .run()
#         )
