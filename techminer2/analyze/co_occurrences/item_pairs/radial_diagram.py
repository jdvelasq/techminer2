# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Radial Diagram
===============================================================================


>>> from techminer2.analyze.co_occurrences.item_pairs import radial_diagram
>>> radial_diagram(
...     #
...     # FUNCTION PARAMS:
...     item_a="ARTIFICIAL_INTELLIGENCE",
...     item_b="REGTECH",
...     columns='author_keywords',
...     rows=None,
...     #
...     # LAYOUT:
...     nx_k=None,
...     nx_iterations=30,
...     nx_random_state=0,
...     #
...     # NODES:
...     node_size_min=30,
...     node_size_max=70,
...     textfont_size_min=10,
...     textfont_size_max=20,
...     textfont_opacity_min=0.35,
...     textfont_opacity_max=1.00,
...     #
...     # EDGES:
...     edge_color="#7793a5",
...     edge_width_min=0.8,
...     edge_width_max=3.0,
...     #
...     # AXES:
...     xaxes_range=None,
...     yaxes_range=None,
...     show_axes=False,
...     #
...     # COLUMN PARAMS:
...     col_top_n=20,
...     col_occ_range=(None, None),
...     col_gc_range=(None, None),
...     col_custom_items=None,
...     #
...     # ROW PARAMS:
...     row_top_n=None,
...     row_occ_range=(None, None),
...     row_gc_range=(None, None),
...     row_custom_items=None,
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... ).write_html("sphinx/_static/analyze/co_occurrences/item_pairs/radial_diagram.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/co_occurrences/item_pairs/radial_diagram.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

"""
import networkx as nx

from ....nx_compute_edge_width_from_edge_weight import nx_compute_edge_width_from_edge_weight
from ....nx_compute_node_size_from_item_occ import nx_compute_node_size_from_item_occ
from ....nx_compute_spring_layout import nx_compute_spring_layout
from ....nx_compute_textfont_opacity_from_item_occ import nx_compute_textfont_opacity_from_item_occ
from ....nx_compute_textfont_size_from_item_occ import nx_compute_textfont_size_from_item_occ
from ....nx_compute_textposition_from_graph import nx_compute_textposition_from_graph
from ....nx_set_edge_color_to_constant import nx_set_edge_color_to_constant
from ....nx_visualize_graph import nx_visualize_graph
from ..co_occurrence_matrix import co_occurrence_matrix


def radial_diagram(
    #
    # FUNCTION PARAMS:
    item_a,
    item_b,
    columns,
    rows=None,
    #
    # CHART PARAMS:
    title=None,
    #
    # LAYOUT:
    nx_k=None,
    nx_iterations=30,
    nx_random_state=0,
    #
    # NODES:
    node_size_min=30,
    node_size_max=70,
    textfont_size_min=10,
    textfont_size_max=20,
    textfont_opacity_min=0.35,
    textfont_opacity_max=1.00,
    #
    # EDGES:
    edge_color="#7793a5",
    edge_width_min=0.8,
    edge_width_max=3.0,
    #
    # AXES:
    xaxes_range=None,
    yaxes_range=None,
    show_axes=False,
    #
    # COLUMN PARAMS:
    col_top_n=None,
    col_occ_range=(None, None),
    col_gc_range=(None, None),
    col_custom_items=None,
    #
    # ROW PARAMS:
    row_top_n=None,
    row_occ_range=(None, None),
    row_gc_range=(None, None),
    row_custom_items=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """Makes a butterfly chart."""

    def extract_item_position_and_name(candidate_items, item):
        """Obtains the positions of topics in a list."""

        org_candidate_items = candidate_items[:]
        candidate_items = [col.split(" ")[:-1] for col in candidate_items]
        candidate_items = [" ".join(col) for col in candidate_items]
        pos = candidate_items.index(item)
        name = org_candidate_items[pos]
        return pos, name

    #
    # MAIN CODE:
    #
    associations = co_occurrence_matrix(
        #
        # FUNCTION PARAMS:
        columns=columns,
        rows=rows,
        #
        # COLUMN PARAMS:
        col_top_n=col_top_n,
        col_occ_range=col_occ_range,
        col_gc_range=col_gc_range,
        col_custom_items=col_custom_items,
        #
        # ROW PARAMS:
        row_top_n=row_top_n,
        row_occ_range=row_occ_range,
        row_gc_range=row_gc_range,
        row_custom_items=row_custom_items,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    ).df_

    #
    # Extracts name and position for item_a and item_b
    pos_a, name_a = extract_item_position_and_name(associations.columns.tolist(), item_a)
    pos_b, name_b = extract_item_position_and_name(associations.columns.tolist(), item_b)
    associations = associations.iloc[:, [pos_a, pos_b]]

    #
    # Delete name_a and name_b from matrix.index if exists
    if name_a in associations.index:
        associations = associations.drop([name_a])
    if name_b in associations.index:
        associations = associations.drop([name_b])

    #
    # delete rows with all zeros
    associations = associations.loc[(associations != 0).any(axis=1)]

    #
    # Create the networkx graph
    nx_graph = nx.Graph()
    nx_graph = __add_nodes_from(nx_graph, associations)
    nx_graph = __add_weighted_edges_from(nx_graph, associations)

    #
    # Sets the layout
    nx_graph = nx_compute_spring_layout(nx_graph, nx_k, nx_iterations, nx_random_state)

    #
    # Sets the node attributes
    # nx_graph = nx_set_node_color_from_group_attr(nx_graph)
    nx_graph = nx_compute_node_size_from_item_occ(nx_graph, node_size_min, node_size_max)
    nx_graph = nx_compute_textfont_size_from_item_occ(
        nx_graph, textfont_size_min, textfont_size_max
    )
    nx_graph = nx_compute_textfont_opacity_from_item_occ(
        nx_graph, textfont_opacity_min, textfont_opacity_max
    )

    #
    # Sets the edge attributes
    nx_graph = nx_compute_edge_width_from_edge_weight(nx_graph, edge_width_min, edge_width_max)
    nx_graph = nx_compute_textposition_from_graph(nx_graph)
    nx_graph = nx_set_edge_color_to_constant(nx_graph, edge_color)

    return nx_visualize_graph(
        #
        # FUNCTION PARAMS:
        nx_graph=nx_graph,
        #
        # NETWORK PARAMS:
        xaxes_range=xaxes_range,
        yaxes_range=yaxes_range,
        show_axes=show_axes,
    )


def __add_nodes_from(
    nx_graph,
    associations,
):
    associations = associations.copy()

    #
    # Adds the rows with  group=0
    nodes = associations.index.tolist()
    nx_graph.add_nodes_from(nodes, group=0, node_color="#7793a5")

    #
    # Adds the column with  group=1
    nodes = associations.columns.to_list()
    nx_graph.add_nodes_from(nodes, group=1, node_color="#465c6b")

    #
    # sets the labels of nodes
    for node in nx_graph.nodes():
        nx_graph.nodes[node]["text"] = node

    return nx_graph


def __add_weighted_edges_from(
    nx_graph,
    associations,
):
    associations = associations.copy()

    for item in associations.columns.tolist():
        for row in associations.index.tolist():
            weight = associations.loc[row, item]
            nx_graph.add_weighted_edges_from(
                ebunch_to_add=[(row, item, weight)],
                dash="solid",
            )

    return nx_graph
