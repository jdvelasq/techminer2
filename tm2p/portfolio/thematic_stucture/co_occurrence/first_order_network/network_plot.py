"""
Network Plot
===============================================================================

.. raw:: html

    <iframe src="../_generated/px.synthes.netw.co_occur.network_plot_1.html"
    height="800px" width="100%" frameBorder="0"></iframe>

    <iframe src="../_generated/px.synthes.netw.co_occur.network_plot_2.html"
    height="800px" width="100%" frameBorder="0"></iframe>

Smoke tests:

    >>> from tm2p.enum import Field, AssociationIndex, ItemOrderBy, GraphClusteringAlgorithm
    >>> from tm2p.portfolio.thematic_stucture.co_occurrence.first_order_network import ItemsByCluster
    >>> df = (
    ...     ItemsByCluster()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.CONCEPT_NORM)
    ...     .having_items_in_top(50)
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
    ...     # CLUSTERING:
    ...     .using_clustering(GraphClusteringAlgorithm.LOUVAIN)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> print(df.to_string())  # doctest: +NORMALIZE_WHITESPACE
                                                0                                  1                                 2                              3
    0              financial technology 052:09484               innovation 033:07734                 fintech 157:34856              banking 025:04625
    1                           finance 050:10972                    china 033:06419                research 014:03510  financial inclusion 022:04623
    2                financial services 031:07105               the impact 021:04968       fintech companies 014:03279             the role 015:02528
    3                             banks 031:06740                 evidence 018:03900                 the use 013:03451         policymakers 013:01987
    4                              data 026:05921  sustainable development 018:02898        fintech services 013:02241             covid-19 012:02097
    5                   the development 026:05689      fintech development 015:03625                   users 012:02989            the world 011:02297
    6                        technology 026:04985           sustainability 014:02486  the financial industry 011:04250            countries 010:02793
    7                        blockchain 017:04405            green finance 013:03038  information technology 011:03183
    8                         consumers 017:03475   financial institutions 012:02923    the financial sector 010:03244
    9           artificial intelligence 014:02936               the effect 012:02564           practitioners 010:03018
    10                        customers 013:02933                    firms 012:01979           the emergence 010:01933
    11                         services 012:03614          economic growth 012:01976
    12                       regulators 012:02416         the relationship 011:02148
    13  the financial services industry 011:03454
    14                   the challenges 011:01924
    15                 cryptocurrencies 010:04061
    16                      investments 010:03080
    17                      innovations 010:02582
    18                    the potential 010:02255



    >>> from tm2p.enum import AssociationIndex, Field, GraphClusteringAlgorithm, NodeScaling, ItemOrderBy
    >>> from tm2p.portfolio.thematic_stucture.co_occurrence.first_order_network import NetworkPlot
    >>> fig = (
    ...     NetworkPlot()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.CONCEPT_NORM)
    ...     .having_items_in_top(50)
    ...     .having_items_ordered_by(ItemOrderBy.OCC)
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # NORMALIZATION:
    ...     .using_association_index(AssociationIndex.ASSOCIATION_STRENGTH)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering(GraphClusteringAlgorithm.LOUVAIN)
    ...     #
    ...     # PLOT:
    ...     .using_spring_layout_intra_scale(2.0)
    ...     .using_spring_layout_cluster_scale(5.0)
    ...     .using_spring_layout_k(None)
    ...     .using_spring_layout_iterations(100)
    ...     .using_spring_layout_seed(0)
    ...     #
    ...     .using_node_size_range(30, 70)
    ...     .using_node_scaling(NodeScaling.SQRT)
    ...     .using_textfont_size_range(10, 20)
    ...     .using_textfont_opacity_range(0.35, 1.00)
    ...     .using_node_n_labels(3)
    ...     #
    ...     .using_edge_top_n(1000)
    ...     .using_top_edges_per_node(5)
    ...     .using_min_edges_per_node(2)
    ...     .using_edge_colors(("#7793a5",))
    ...     .using_edge_width_range(0.1, 3.0)
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
    >>> type(fig).__name__
    'Figure'
    >>> fig.write_html("docsrc/_generated/px.synthes.netw.co_occur.network_plot_1.html")

    >>> fig = (
    ...     NetworkPlot()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.CONCEPT_NORM)
    ...     .having_items_in_top(50)
    ...     .having_items_ordered_by(ItemOrderBy.OCC)
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
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
    ...     .using_spring_layout_k(None)
    ...     .using_spring_layout_iterations(100)
    ...     .using_spring_layout_seed(0)
    ...     #
    ...     .using_node_n_labels(4)
    ...     .using_node_size_range(30, 70)
    ...     .using_node_scaling(NodeScaling.SQRT)
    ...     .using_textfont_size_range(10, 20)
    ...     .using_textfont_opacity_range(0.35, 1.00)
    ...     #
    ...     .using_edge_top_n(1000)
    ...     .using_top_edges_per_node(5)
    ...     .using_min_edges_per_node(2)
    ...     .using_edge_colors(("#7793a5",))
    ...     .using_edge_width_range(0.1, 3.0)
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
    >>> fig.write_html("docsrc/_generated/px.synthes.netw.co_occur.network_plot_2.html")


"""

from tm2p._intern import ParamsMixin, remove_counters
from tm2p._intern.nx import (
    assign_clusters_to_nodes,
    assign_edge_color_opacity,
    assign_edge_widths_based_on_weight,
    assign_node_colors_based_on_group_attribute,
    assign_node_sizes_based_on_occurrences,
    assign_text_positions_based_on_quadrants,
    assign_textfont_opacity_based_on_occurrences,
    assign_textfont_sizes_based_on_occurrences,
    compute_clustered_spring_layout_positions,
    plot_nx_graph,
    remove_nodes_and_links,
)

from ._intern.create_nx_graph import create_nx_graph
from .item_to_cluster import ItemToCluster


class NetworkPlot(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        use_counters = self.params.counters
        self.params.counters = True
        nx_graph = create_nx_graph(self.params)
        item2cluster = ItemToCluster().update(**self.params.__dict__).run()
        nx_graph = assign_clusters_to_nodes(self.params, nx_graph, item2cluster)
        nx_graph = remove_nodes_and_links(self.params, nx_graph)

        nx_graph = compute_clustered_spring_layout_positions(self.params, nx_graph)
        nx_graph = assign_node_colors_based_on_group_attribute(nx_graph)
        nx_graph = assign_node_sizes_based_on_occurrences(self.params, nx_graph)
        nx_graph = assign_textfont_sizes_based_on_occurrences(self.params, nx_graph)
        nx_graph = assign_textfont_opacity_based_on_occurrences(self.params, nx_graph)
        nx_graph = assign_edge_widths_based_on_weight(self.params, nx_graph)
        nx_graph = assign_text_positions_based_on_quadrants(nx_graph)
        nx_graph = assign_edge_color_opacity(self.params, nx_graph)

        if use_counters is False:
            self.params.counters = False
            for node, data in nx_graph.nodes(data=True):
                text = data["text"]
                nx_graph.nodes[node]["text"] = remove_counters(text)

        return plot_nx_graph(self.params, nx_graph)
