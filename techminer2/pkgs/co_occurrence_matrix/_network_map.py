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


## >>> from techminer2.co_occurrence_matrix import NetworkMap
## >>> plot = (
## ...     CoOccurrenceNetworkMap()
## ...     #
## ...     # FIELD:
## ...     .with_field("author_keywords")
## ...     .having_terms_in_top(10)
## ...     .having_terms_ordered_by("OCC")
## ...     .having_term_occurrences_between(2, None)
## ...     .having_term_citations_between(None, None)
## ...     .having_terms_in(None)
## ...     #
## ...     # OTHER FIELD:
## ...     .with_other_field("authors")
## ...     .having_other_terms_in_top(10)
## ...     .having_other_terms_ordered_by("OCC")
## ...     .having_other_term_occurrences_between(2, None)
## ...     .having_other_term_citations_between(None, None)
## ...     .having_other_terms_in(None)
## ...     #
## ...     # COUNTERS:
## ...     .using_term_counters(True)
## ...     #
## ...     # NETWORK:
## ...     .using_spring_layout_k(None)
## ...     .using_spring_layout_iterations(30)
## ...     .using_spring_layout_seed(0)
## ...     #
## ...     .using_node_colors(
## ...         (
## ...              "#7793a5", 
## ...              "#465c6b",
## ...         )
## ...     )
## ...     .using_edge_colors(
## ...          (
## ...              "#7793a5", 
## ...              "#7793a5", 
## ...              "#7793a5", 
## ...              "#7793a5",
## ...          )
## ...     )
## ...     .using_node_size_range(30, 70)
## ...     .using_textfont_size_range(10, 20)
## ...     .using_textfont_opacity_range(0.35, 1.00)
## ...     .using_xaxes_range=(None, None)
## ...     .using_yaxes_range=(None, None)
## ...     .using_axes_visible(False)
## ...     #
## ...     # DATABASE:
## ...     .where_directory_is("example/")
## ...     .where_database_is("main")
## ...     .where_record_years_between(None, None)
## ...     .where_record_citations_between(None, None)
## ...     .where_records_match(None)
## ...     #
## ...     .build()
## ... )
## >>> plot.write_html("sphinx/_generated/co_occurrence_matrix/network_map_0.html")

.. raw:: html

    <iframe src="../../_generated/co_occurrence_matrix/network_map_0.html"
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> from techminer2.co_occurrence_matrix import CoOccurrenceNetworkMap   
>>> plot = (
## ...     CoOccurrenceNetworkMap()
## ...     #
## ...     # COLUMNS:
## ...     .with_field("author_keywords")
## ...     .having_terms_in_top(10)
## ...     .having_terms_ordered_by("OCC")
## ...     .having_term_occurrences_between(None, None)
## ...     .having_term_citations_between(None, None)
## ...     .having_terms_in(None)
## ...     #
## ...     # ROWS:
## ...     .with_other_field(None)
## ...     .having_other_terms_in_top(None)
## ...     .having_other_terms_ordered_by(None)
## ...     .having_other_term_occurrences_between(None, None)
## ...     .having_other_term_citations_between(None, None)
## ...     .having_other_terms_in(None)
## ...     #
## ...     # COUNTERS:
## ...     .using_term_counters(True)
## 
## ...     #
## ...     # NETWORK:
## ...     .using_spring_layout_k(None)
## ...     .using_spring_layout_iterations(30)
## ...     .using_spring_layout_seed(0)
## 
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
## ...     .using_node_size_range(30, 70)
## ...     .using_textfont_size_range(10, 20)
## ...     .using_textfont_opacity_range(0.35, 1.00)
## ...     .using_xaxes_range=(None, None)
## ...     .using_yaxes_range=(None, None)
## ...     .using_axes_visible(False)
## ...     #
## ...     # DATABASE:
## ...     .where_directory_is("example/")
## ...     .where_database_is("main")
## ...     .where_record_years_between(None, None)
## ...     .where_record_citations_between(None, None)
## ...     .where_records_match(None)
## ...     #
## ...     .build()
... )
>>> plot.write_html("sphinx/_generated/co_occurrence_matrix/network_map_1.html")

.. raw:: html

    <iframe src="../../_generated/co_occurrence_matrix/network_map_1.html"
    height="600px" width="100%" frameBorder="0"></iframe>



    
"""
import networkx as nx  # type: ignore
import pandas as pd  # type: ignore
from sklearn.metrics.pairwise import cosine_similarity  # type: ignore

from ...internals.nx.assign_node_sizes_based_on_occurrences import (
    internal__assign_node_sizes_based_on_occurrences,
)
from ...internals.nx.assign_text_positions_based_on_quadrants import (
    internal__assign_text_positions_based_on_quadrants,
)
from ...internals.nx.assign_textfont_opacity_based_on_occurrences import (
    internal__assign_textfont_opacity_based_on_occurrences,
)
from ...internals.nx.assign_textfont_sizes_based_on_occurrences import (
    internal__assign_textfont_sizes_based_on_occurrences,
)
from ...internals.nx.compute_spring_layout_positions import (
    internal__compute_spring_layout_positions,
)
from ...internals.nx.create_network_plot import internal__create_network_plot
from ...internals.nx_mixin.nx_spring_layout_params import (
    NxSpringLayoutParams,
    NxSpringLayoutParamsMixin,
)
from ...internals.params.axes_params import AxesParams, AxesParamsMixin
from ...internals.params.columns_and_rows_params import ColumnsAndRowsParamsMixin
from ...internals.params.item_params import ItemParams
from .internals.output_params import OutputParams, OutputParamsMixin

# from .matrix import co_occurrence_matrix


class CoOccurrenceNetworkMap(
    ColumnsAndRowsParamsMixin,
    OutputParamsMixin,
    NxSpringLayoutParamsMixin,
    AxesParamsMixin,
):
    """:meta private:"""

    def __init__(self):

        self.column_params = ItemParams()
        self.database_params = DatabaseFilters()
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
    nx_graph = internal__compute_spring_layout_positions(
        nx_graph, nx_k, nx_iterations, nx_random_state
    )

    #
    # Sets the node attributes
    nx_graph = internal__assign_node_sizes_based_on_occurrences(
        nx_graph, node_size_range
    )
    nx_graph = internal__assign_textfont_sizes_based_on_occurrences(
        nx_graph, textfont_size_range
    )

    nx_graph = internal__assign_textfont_opacity_based_on_occurrences(
        nx_graph, textfont_opacity_range
    )
    #
    # Sets the edge attributes
    nx_graph = __set_edge_properties(nx_graph, edge_colors)
    nx_graph = internal__assign_text_positions_based_on_quadrants(nx_graph)

    return internal__create_network_plot(
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
