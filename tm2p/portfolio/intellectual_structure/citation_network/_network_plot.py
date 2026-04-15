"""
NetworkPlot
===============================================================================

* **CitationUnit.DOC**

.. raw:: html

    <iframe src="../_generated/px.synthes.netw.cit.network_plot_doc.html"
    height="800px" width="100%" frameBorder="0"></iframe>

Smoke tests:
    >>> from tm2p.enum import AssociationIndex, CitationUnit, GraphClusteringAlgorithm, Scaling
    >>> from tm2p.synthesize.netw.cit import NetworkPlot
    >>> # ---------------------------------------------------------------------
    >>> # DOC
    >>> # ---------------------------------------------------------------------
    >>> fig = (
    ...     NetworkPlot()
    ...     #
    ...     # CITATION UNIT:
    ...     .with_citation_unit(CitationUnit.DOC)
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
    ...     .using_top_n_node_labels(5)
    ...     .using_top_n_nodes(1000)
    ...     #
    ...     # https://www.w3schools.com/colors/colors_shades.asp
    ...     .using_edge_color("#e0e0e0")
    ...     .using_edge_scaling(Scaling.SQRT)
    ...     .using_edge_top_n(1000)
    ...     .using_edge_width_range(0.1, 3.0)
    ...     .using_min_edges_per_node(3)
    ...     .using_top_edges_per_node(5)
    ...     #
    ...     .using_xaxes_range(None, None)
    ...     .using_yaxes_range(None, None)
    ...     .using_axes_visible(False)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> fig.write_html("docsrc/_generated/px.synthes.netw.cit.network_plot_doc.html")



* **CitationUnit.AUTH**

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
    ...     .with_citation_unit(CitationUnit.AUTH)
    ...     .having_items_in_top(30)
    ...     .having_items_in(None)
    ...     .having_minimum_citation_count(0)
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
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> fig.write_html("docsrc/_generated/px.synthes.netw.cit.network_plot_auth.html")



* **CitationUnit.CTRY**

.. raw:: html

    <iframe src="../_generated/px.synthes.netw.cit.network_plot_ctry.html"
    height="800px" width="100%" frameBorder="0"></iframe>

Smoke tests:
    >>> # ---------------------------------------------------------------------
    >>> # CTRY
    >>> # ---------------------------------------------------------------------
    >>> fig = (
    ...     NetworkPlot()
    ...     #
    ...     # CITATION UNIT:
    ...     .with_citation_unit(CitationUnit.CTRY)
    ...     .having_items_in_top(30)
    ...     .having_items_in(None)
    ...     .having_minimum_citation_count(0)
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
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> fig.write_html("docsrc/_generated/px.synthes.netw.cit.network_plot_ctry.html")


* **CitationUnit.ORG**

.. raw:: html

    <iframe src="../_generated/px.synthes.netw.cit.network_plot_org.html"
    height="800px" width="100%" frameBorder="0"></iframe>

Smoke tests:
    >>> # ---------------------------------------------------------------------
    >>> # ORG
    >>> # ---------------------------------------------------------------------
    >>> fig = (
    ...     NetworkPlot()
    ...     #
    ...     # CITATION UNIT:
    ...     .with_citation_unit(CitationUnit.ORG)
    ...     .having_items_in_top(30)
    ...     .having_items_in(None)
    ...     .having_minimum_citation_count(0)
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
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> fig.write_html("docsrc/_generated/px.synthes.netw.cit.network_plot_org.html")



* **CitationUnit.SRC**

.. raw:: html

    <iframe src="../_generated/px.synthes.netw.cit.network_plot_src.html"
    height="800px" width="100%" frameBorder="0"></iframe>

Smoke tests:
    >>> # ---------------------------------------------------------------------
    >>> # SRC
    >>> # ---------------------------------------------------------------------
    >>> fig = (
    ...     NetworkPlot()
    ...     #
    ...     # CITATION UNIT:
    ...     .with_citation_unit(CitationUnit.SRC)
    ...     .having_items_in_top(30)
    ...     .having_items_in(None)
    ...     .having_minimum_citation_count(0)
    ...     .having_occurrence_threshold(2)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(False)
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
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> fig.write_html("docsrc/_generated/px.synthes.netw.cit.network_plot_src.html")



"""

from tm2p._intern.networks import BaseStrengthPlot

from .node_metrics import NodeMetrics


class NetworkPlot(
    BaseStrengthPlot,
):
    """:meta private:"""

    def get_node_metrics(self):
        return


# from tm2p._intern import ParamsMixin
# from tm2p.enum import CitationUnit, ItemOrderBy
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

#         if self.params.citation_unit == CitationUnit.DOC:
#             Plot = DocNetworkPlot
#         else:
#             Plot = OtherNetworkPlot

#         return (
#             Plot()
#             .update(**self.params.__dict__)
#             .update(items_order_by=ItemOrderBy.OCC)
#             .run()
#         )
