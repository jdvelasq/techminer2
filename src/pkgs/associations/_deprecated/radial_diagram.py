# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Radial Diagram
===============================================================================


## >>> from techminer2.tools.associations import radial_diagram
## >>> plot = (
## ...     RadialDiagram()
## ...     .set_analysis_params(
## ...         items=["FINTECH", "INNOVATION"],
## ...     #
## ...     # COLUMNS:
## ...     .with_field("author_keywords")
## ...     .having_terms_in_top(10)
## ...     .having_terms_ordered_by("OCC")
## ...     .having_term_occurrences_between(2, None)
## ...     .having_term_citations_between(None, None)
## ...     .having_terms_in(None)
## ...     #
## ...     ).set_plot_params(
## ...         edge_color="#7793a5",
## ...         edge_width_range=(0.8, 3.0),

## ...     .using_node_size_range(30, 70)
## ...     .using_textfont_opacity_range(0.35, 1.00)
## ...     .using_textfont_size_range(10, 20)
## ...     #
## ...     # NETWORK:
## ...     .using_spring_layout_k(None)
## ...     .using_spring_layout_iterations(30)
## ...     .using_spring_layout_seed(0)
## ...     #
## ...     .using_xaxes_range(None, None)
## ...     .using_yaxes_range(None, None)
## ...     .using_axes_visible(False)

## ...     #
## ...     ).set_rows_params(
## ...         field=None,
## ...         top_n=None,
## ...         occ_range=(None, None),
## ...         gc_range=(None, None),
## ...         custom_terms=None,
## ...     #
## ...     # DATABASE:
## ...     .where_root_directory_is("example/")
## ...     .where_database_is("main")
## ...     .where_record_years_range_is(None, None)
## ...     .where_record_citations_range_is(None, None)
## ...     #
## ...     .run()
## ... )
## >>> # plot.write_html("sphinx/_static/tools/associations/radial_diagram.html")

.. raw:: html

    <iframe src="../../_static/tools/associations/radial_diagram.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

"""
# import networkx as nx  # type: ignore

# from ...internals.nx.assign_constant_to_edge_colors import (
#     internal__assign_constant_to_edge_colors,
# )
# from ...internals.nx.assign_edge_widths_based_on_weight import (
#     internal__assign_edge_widths_based_on_weight,
# )
# from ...internals.nx.assign_node_sizes_based_on_occurrences import (
#     internal__assign_node_sizes_based_on_occurrences,
# )
# from ...internals.nx.assign_text_positions_based_on_quadrants import (
#     internal__assign_text_positions_based_on_quadrants,
# )
# from ...internals.nx.assign_textfont_opacity_based_on_occurrences import (
#     internal__assign_textfont_opacity_based_on_occurrences,
# )
# from ...internals.nx.assign_textfont_sizes_based_on_occurrences import (
#     internal__assign_textfont_sizes_based_on_occurrences,
# )
# from ...internals.nx.compute_spring_layout_positions import (
#     internal__compute_spring_layout_positions,
# )
# from ...internals.nx.plot_network_graph import internal__plot_network_graph

# # from ..cross_co_occurrence.matrix import co_occurrence_matrix


# def radial_diagram(
#     #
#     # FUNCTION PARAMS:
#     items,
#     columns,
#     rows=None,
#     #
#     # CHART PARAMS:
#     title=None,
#     #
#     # LAYOUT:
#     nx_k=None,
#     nx_iterations=30,
#     nx_random_state=0,
#     #
#     # NODES:
#     node_size_range=(30, 70),
#     textfont_size_range=(10, 20),
#     textfont_opacity_range=(0.35, 1.00),
#     #
#     # EDGES:
#     edge_color="#7793a5",
#     edge_width_range=(0.8, 3.0),
#     #
#     # AXES:
#     xaxes_range=None,
#     yaxes_range=None,
#     show_axes=False,
#     #
#     # COLUMN PARAMS:
#     col_top_n=None,
#     col_occ_range=(None, None),
#     col_gc_range=(None, None),
#     col_custom_terms=None,
#     #
#     # ROW PARAMS:
#     row_top_n=None,
#     row_occ_range=(None, None),
#     row_gc_range=(None, None),
#     row_custom_terms=None,
#     #
#     # DATABASE PARAMS:
#     root_dir="./",
#     database="main",
#     year_filter=(None, None),
#     cited_by_filter=(None, None),
#     **filters,
# ):
#     """Makes a butterfly chart.

#     :meta private:
#     """

#     def extract_item_position_and_name(candidate_items, item):
#         """Obtains the positions of topics in a list."""

#         org_candidate_items = candidate_items[:]
#         candidate_items = [col.split(" ")[:-1] for col in candidate_items]
#         candidate_items = [" ".join(col) for col in candidate_items]
#         pos = candidate_items.index(item)
#         name = org_candidate_items[pos]
#         return pos, name

#     #
#     # MAIN CODE:
#     #
#     associations = co_occurrence_matrix(
#         #
#         # FUNCTION PARAMS:
#         columns=columns,
#         rows=rows,
#         #
#         # COLUMN PARAMS:
#         col_top_n=col_top_n,
#         col_occ_range=col_occ_range,
#         col_gc_range=col_gc_range,
#         col_custom_terms=col_custom_terms,
#         #
#         # ROW PARAMS:
#         row_top_n=row_top_n,
#         row_occ_range=row_occ_range,
#         row_gc_range=row_gc_range,
#         row_custom_terms=row_custom_terms,
#         #
#         # DATABASE PARAMS:
#         root_dir=root_dir,
#         database=database,
#         year_filter=year_filter,
#         cited_by_filter=cited_by_filter,
#         **filters,
#     )

#     #
#     # Extracts name and position for item_a and item_b
#     if isinstance(items, str):
#         items = [items]

#     positions = []
#     names = []
#     for item in items:
#         position, name = extract_item_position_and_name(
#             associations.columns.tolist(), item
#         )
#         positions.append(position)
#         names.append(name)

#     associations = associations.iloc[:, positions]

#     #
#     # Delete names from matrix.index if exists
#     for name in names:
#         associations = associations.drop([name])

#     #
#     # delete rows with all zeros
#     associations = associations.loc[(associations != 0).any(axis=1)]

#     #
#     # Create the networkx graph
#     nx_graph = nx.Graph()
#     nx_graph = __add_nodes_from(nx_graph, associations)
#     nx_graph = __add_weighted_edges_from(nx_graph, associations)

#     #
#     # Sets the layout
#     nx_graph = internal__compute_spring_layout_positions(
#         nx_graph, nx_k, nx_iterations, nx_random_state
#     )

#     #
#     # Sets the node attributes
#     nx_graph = internal__assign_node_sizes_based_on_occurrences(
#         nx_graph, node_size_range
#     )
#     nx_graph = internal__assign_textfont_sizes_based_on_occurrences(
#         nx_graph, textfont_size_range
#     )
#     nx_graph = internal__assign_textfont_opacity_based_on_occurrences(
#         nx_graph, textfont_opacity_range
#     )

#     #
#     # Sets the edge attributes
#     nx_graph = internal__assign_edge_widths_based_on_weight(nx_graph, edge_width_range)
#     nx_graph = internal__assign_text_positions_based_on_quadrants(nx_graph)
#     nx_graph = internal__assign_constant_to_edge_colors(nx_graph, edge_color)

#     return internal__plot_network_graph(
#         #
#         # FUNCTION PARAMS:
#         nx_graph=nx_graph,
#         #
#         # NETWORK PARAMS:
#         xaxes_range=xaxes_range,
#         yaxes_range=yaxes_range,
#         show_axes=show_axes,
#     )


# def __add_nodes_from(
#     nx_graph,
#     associations,
# ):
#     associations = associations.copy()

#     #
#     # Adds the rows with  group=0
#     nodes = associations.index.tolist()
#     nx_graph.add_nodes_from(nodes, group=0, node_color="#7793a5")

#     #
#     # Adds the column with  group=1
#     nodes = associations.columns.to_list()
#     nx_graph.add_nodes_from(nodes, group=1, node_color="#465c6b")

#     #
#     # sets the labels of nodes
#     for node in nx_graph.nodes():
#         nx_graph.nodes[node]["text"] = node

#     return nx_graph


# def __add_weighted_edges_from(
#     nx_graph,
#     associations,
# ):
#     associations = associations.copy()

#     for item in associations.columns.tolist():
#         for row in associations.index.tolist():
#             weight = associations.loc[row, item]
#             nx_graph.add_weighted_edges_from(
#                 ebunch_to_add=[(row, item, weight)],
#                 dash="solid",
#             )

#     return nx_graph
