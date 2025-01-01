# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Network Map
===============================================================================


## >>> from techminer2.co_occurrence_matrix import CoOccurrenceNetworkMap
## >>> plot = (
## ...     CoOccurrenceNetworkMap()
## ...     .set_columns_params(
## ...         field="author_keywords",
## ...         top_n=10,
## ...         occ_range=(None, None),
## ...         gc_range=(None, None),
## ...         custom_terms=None,
## ...     #
## ...     ).set_rows_params(
## ...         field="authors",
## ...         top_n=10,
## ...         occ_range=(None, None),
## ...         gc_range=(None, None),
## ...         custom_terms=None,
## ...     #
## ...     ).set_format_params(
## ...         retain_counters=True,
## ...     #
## ...     ).set_nx_params(
## ...         nx_k=None,
## ...         nx_iterations=30,
## ...         nx_random_state=0,
## ...     #
## ...     ).set_plot_params(
## ...          node_colors=(
## ...              "#7793a5", 
## ...              "#465c6b",
## ...          ),
## ...          edge_colors=(
## ...              "#7793a5", 
## ...              "#7793a5", 
## ...              "#7793a5", 
## ...              "#7793a5",
## ...          ),
## ...          node_size_range=(30, 70),
## ...          textfont_size_range=(10, 20),
## ...          textfont_opacity_range=(0.35, 1.00),
## ...     #
## ...     ).set_axes_params(
## ...         xaxes_range=None,
## ...         yaxes_range=None,
## ...         show_axes=False,
## ...     #
## ...     ).set_database_params(
## ...         root_dir="example/", 
## ...         database="main",
## ...         year_filter=(None, None),
## ...         cited_by_filter=(None, None),
## ...     #
## ...     ).build()
## ... )
## >>> plot.write_html("sphinx/_generated/analyze/co_occurrence_matrix/network_map_0.html")

.. raw:: html

    <iframe src="../../_generated/analyze/co_occurrence_matrix/network_map_0.html"
    height="600px" width="100%" frameBorder="0"></iframe>

    
## >>> from techminer2.co_occurrence_matrix import CoOccurrenceNetworkMap   
## >>> plot = (
## ...     CoOccurrenceNetworkMap()
## ...     .set_column_params(
## ...         field="author_keywords",
## ...         top_n=10,
## ...         occ_range=(None, None),
## ...         gc_range=(None, None),
## ...         custom_terms=None,
## ...     ).set_rows_params(
## ...         field=None,
## ...         top_n=None,
## ...         occ_range=(None, None),
## ...         gc_range=(None, None),
## ...         custom_terms=None,
## ...     ).set_format_params(
## ...         retain_counters=True,
## ...     ).set_nx_params(
## ...         nx_k=None,
## ...         nx_iterations=30,
## ...         nx_random_state=0,
## ...     ).set_plot_params(
## ...          node_colors=(
## ...              "#7793a5", 
## ...              "#465c6b",
## ...          ),
## ...          edge_colors=(
## ...              "#7793a5", 
## ...              "#7793a5", 
## ...              "#7793a5", 
## ...              "#7793a5",
## ...          ),
## ...          node_size_range=(30, 70),
## ...          textfont_size_range=(10, 20),
## ...          textfont_opacity_range=(0.35, 1.00),
## ...     ).set_axes_params(
## ...         xaxes_range=None,
## ...         yaxes_range=None,
## ...         show_axes=False,
## ...     ).set_database_params(
## ...         root_dir="example/", 
## ...         database="main",
## ...         year_filter=(None, None),
## ...         cited_by_filter=(None, None),
## ...     ).build()
## ... )
## >>> plot.write_html("sphinx/_generated/analyze/co_occurrence_matrix/network_map_1.html")

.. raw:: html

    <iframe src="../../_generated/analyze/co_occurrence_matrix/network_map_1.html"
    height="600px" width="100%" frameBorder="0"></iframe>



    
"""
import networkx as nx  # type: ignore
import pandas as pd  # type: ignore
from sklearn.metrics.pairwise import cosine_similarity  # type: ignore

from ...internals.nx.nx_assign_opacity_to_text_by_frequency import (
    nx_assign_opacity_to_text_by_frequency,
)
from ...internals.nx.nx_assign_sizes_to_nodes_by_occurrences import (
    nx_assign_sizes_to_nodes_by_occurrences,
)
from ...internals.nx.nx_assign_text_positions_to_nodes_by_quadrants import (
    nx_assign_text_positions_to_nodes_by_quadrants,
)
from ...internals.nx.nx_assign_textfont_sizes_to_nodes_by_occurrences import (
    nx_assign_textfont_sizes_to_nodes_by_occurrences,
)
from ...internals.nx.nx_compute_spring_layout_positions import (
    nx_compute_spring_layout_positions,
)
from ...internals.nx.nx_network_plot import nx_network_plot
from ...internals.nx_mixin.nx_spring_layout_params import (
    NxSpringLayoutParams,
    NxSpringLayoutParamsMixin,
)
from ...internals.params.axes_params import AxesParams, AxesParamsMixin
from ...internals.params.columns_and_rows_params import ColumnsAndRowsParamsMixin
from ...internals.params.database_params import DatabaseParams, DatabaseParamsMixin
from ...internals.params.item_params import ItemParams
from .internals.output_params import OutputParams, OutputParamsMixin
from .matrix import co_occurrence_matrix


class CoOccurrenceNetworkMap(
    ColumnsAndRowsParamsMixin,
    DatabaseParamsMixin,
    OutputParamsMixin,
    NxSpringLayoutParamsMixin,
    AxesParamsMixin,
):
    """:meta private:"""

    def __init__(self):

        self.column_params = ItemParams()
        self.database_params = DatabaseParams()
        self.row_params = ItemParams()
        self.format_params = OutputParams()
        self.nx_params = NxSpringLayoutParams()
        self.axes_params = AxesParams()

    def build(self):

        return co_occurrence_map()


def co_occurrence_map(
    #
    # FUNCTION PARAMS:
    columns,
    rows=None,
    retain_counters=True,
    #
    # COLUMN PARAMS:
    col_top_n=None,
    col_occ_range=(None, None),
    col_gc_range=(None, None),
    col_custom_terms=None,
    #
    # ROW PARAMS:
    row_top_n=None,
    row_occ_range=(None, None),
    row_gc_range=(None, None),
    row_custom_terms=None,
    #
    # LAYOUT:
    nx_k=None,
    nx_iterations=30,
    nx_random_state=0,
    #
    # NODES:
    node_colors=(
        "#7793a5",
        "#465c6b",
    ),
    node_size_range=(30, 70),
    textfont_size_range=(10, 20),
    textfont_opacity_range=(0.35, 1.00),
    #
    # EDGES:
    edge_colors=(
        "#7793a5",
        "#7793a5",
        "#7793a5",
        "#7793a5",
    ),
    #
    # AXES:
    xaxes_range=None,
    yaxes_range=None,
    show_axes=False,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """:meta private:"""

    cooc_matrix = co_occurrence_matrix(
        #
        # FUNCTION PARAMS:
        columns=columns,
        rows=rows,
        retain_counters=retain_counters,
        #
        # COLUMN PARAMS:
        col_top_n=col_top_n,
        col_occ_range=col_occ_range,
        col_gc_range=col_gc_range,
        col_custom_terms=col_custom_terms,
        #
        # ROW PARAMS:
        row_top_n=row_top_n,
        row_occ_range=row_occ_range,
        row_gc_range=row_gc_range,
        row_custom_terms=row_custom_terms,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    #
    #
    similarity = pd.DataFrame(
        cosine_similarity(cooc_matrix),
        index=cooc_matrix.index,
        columns=cooc_matrix.index,
    )

    #
    # Create the networkx graph
    nx_graph = nx.Graph()
    nx_graph = _add_nodes_from_similarity_matrix(nx_graph, similarity, node_colors)
    nx_graph = _add_weighted_edges_from_similarity_matrix(nx_graph, similarity)

    #
    # Sets the layout
    nx_graph = nx_compute_spring_layout_positions(
        nx_graph, nx_k, nx_iterations, nx_random_state
    )

    #
    # Sets the node attributes
    nx_graph = nx_assign_sizes_to_nodes_by_occurrences(nx_graph, node_size_range)
    nx_graph = nx_assign_textfont_sizes_to_nodes_by_occurrences(
        nx_graph, textfont_size_range
    )

    nx_graph = nx_assign_opacity_to_text_by_frequency(nx_graph, textfont_opacity_range)
    #
    # Sets the edge attributes
    nx_graph = __set_edge_properties(nx_graph, edge_colors)
    nx_graph = nx_assign_text_positions_to_nodes_by_quadrants(nx_graph)

    return nx_network_plot(
        #
        # FUNCTION PARAMS:
        nx_graph=nx_graph,
        #
        # NETWORK PARAMS:
        xaxes_range=xaxes_range,
        yaxes_range=yaxes_range,
        show_axes=show_axes,
    )


def _add_nodes_from_similarity_matrix(
    nx_graph,
    similarity_matrix,
    node_colors,
):
    #
    # Adds rows nodes
    matrix = similarity_matrix.copy()
    nodes = matrix.index.tolist()
    nx_graph.add_nodes_from(nodes, group=0, node_color=node_colors[0])

    #
    # Adds columns nodes
    if matrix.index.tolist() != matrix.columns.tolist():
        nodes = matrix.columns.tolist()
        nx_graph.add_nodes_from(nodes, group=1, node_color=node_colors[1])

    for node in nx_graph.nodes():
        nx_graph.nodes[node]["text"] = node

    return nx_graph


def _add_weighted_edges_from_similarity_matrix(nx_graph, similarity_matrix):
    #
    # Adds links from ...
    #
    matrix = similarity_matrix.copy()

    if matrix.index.tolist() == matrix.columns.tolist():
        #
        # This is a symmetric matrix:
        #
        for i_row, row in enumerate(matrix.index.tolist()):
            for i_col, col in enumerate(matrix.columns.tolist()):
                #
                if matrix.iloc[i_row, i_col] > 0:
                    #
                    # Unicamente toma valores por encima de la diagonal principal
                    if i_col <= i_row:
                        continue

                    weight = matrix.loc[row, col]
                    nx_graph.add_weighted_edges_from(
                        ebunch_to_add=[(row, col, weight)],
                    )

        return nx_graph

    #
    # This is a non-symmetric matrix:
    #
    for i_row, row in enumerate(matrix.index.tolist()):
        for i_col, col in enumerate(matrix.columns.tolist()):
            #
            if matrix.loc[row, col] > 0:
                #
                weight = matrix.loc[row, col]
                nx_graph.add_weighted_edges_from(
                    ebunch_to_add=[(row, col, weight)],
                )

    return nx_graph


def __set_edge_properties(nx_graph, edge_colors):
    for edge in nx_graph.edges():
        weight = nx_graph.edges[edge]["weight"]

        if weight < 0.25:
            width, dash = 2, "dot"
            edge_color = edge_colors[0]

        elif weight < 0.5:
            width, dash = 2, "dash"
            edge_color = edge_colors[1]

        elif weight < 0.75:
            width, dash = 4, "solid"
            edge_color = edge_colors[2]

        else:
            width, dash = 6, "solid"
            edge_color = edge_colors[3]

        nx_graph.edges[edge]["width"] = width
        nx_graph.edges[edge]["dash"] = dash
        nx_graph.edges[edge]["color"] = edge_color

    return nx_graph
