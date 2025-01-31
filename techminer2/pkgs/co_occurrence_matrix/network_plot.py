# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
NetworkPlot
===============================================================================


## >>> from techminer2.co_occurrence_matrix import NetworkPlot
## >>> plot = (
## ...     NetworkPlot()
## ...     #
## ...     # COLUMNS:
## ...     .wiht_field("author_keywords")
## ...     #
## ...     .having_terms_in_top(10)
## ...     .having_terms_ordered_by("OCC")
## ...     .having_term_occurrences_between(None, None)
## ...     .having_term_citations_between(None, None)
## ...     .having_terms_in(None)
## ...     #
## ...     # ROWWS:
## ...     .wiht_other_field("authors")
## ...     #
## ...     .having_other_terms_in_top(10)
## ...     .having_other_terms_ordered_by("OCC")
## ...     .having_other_term_occurrences_between(None, None)
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
## ...     .using_node_size_range(30, 70)
## ...     .using_textfont_size_range(10, 20)
## ...     .using_textfont_opacity_range(0.35, 1.00)
## ...         edge_color="#b8c6d0",
## ...         edge_width_range=(0.8, 4.0),
## ...     #
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
## >>> )
## >>> plot.write_html("sphinx/_generated/co_occurrence_matrix/co_occurrence_matrix_network_0.html")

.. raw:: html
    
    <iframe src="../../_generated/co_occurrence_matrix/co_occurrence_matrix_network_0.html" 
    height="600px" width="100%" frameBorder="0"></iframe>


## >>> from techminer2.analyze.co_occurrence_matrix import NetworkPlot
## >>> plot = (
## ...     NetworkPlot()
## ...     #
## ...     # COLUMNS:
## ...     .wiht_field("author_keywords")
## ...     #
## ...     .having_terms_in_top(10)
## ...     .having_terms_ordered_by("OCC")
## ...     .having_term_occurrences_between(2, None)
## ...     .having_term_citations_between(None, None)
## ...     .having_terms_in(None)
## ...     #
## ...     # ROWWS:
## ...     .wiht_other_field(None)
## ...     #
## ...     .having_other_terms_in_top(None)
## ...     .having_other_terms_ordered_by(None)
## ...     .having_other_term_occurrences_between(None, None)
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
## ...     .using_node_size_range(30, 70)
## ...     .using_textfont_size_range(10, 20)
## ...     .using_textfont_opacity_range(0.35, 1.00)
## 
## ...         edge_color="#b8c6d0",
## ...         edge_width_range=(0.8, 4.0),
## 
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
## >>> )
## >>> plot.write_html("sphinx/_generated/analyze/co_occurrence_matrix/co_occurrence_matrix_network_1.html")

.. raw:: html
    
    <iframe src="../../_generated/analyze/co_occurrence_matrix/co_occurrence_matrix_network_1.html" 
    height="600px" width="100%" frameBorder="0"></iframe>


    
"""
from dataclasses import dataclass
from typing import Optional, Tuple

import networkx as nx  # type: ignore

from ...internals import DatabaseFilters, SetDatabaseFiltersMixin
from ...internals.nx.internal__assign_opacity_to_text_by_frequency import (
    internal__assign_opacity_to_text_by_frequency,
)
from ...internals.nx.internal__assign_sizes_to_nodes_by_occurrences import (
    internal__assign_sizes_to_nodes_by_occurrences,
)
from ...internals.nx.internal__assign_text_positions_to_nodes_by_quadrants import (
    internal__assign_text_positions_to_nodes_by_quadrants,
)
from ...internals.nx.internal__assign_textfont_sizes_to_nodes_by_occurrences import (
    nx_assign_textfont_sizes_to_nodes_by_occurrences,
)
from ...internals.nx.internal__assign_uniform_color_to_edges import (
    internal__assign_uniform_color_to_edges,
)
from ...internals.nx.internal__assign_widths_to_edges_by_weight import (
    internal__assign_widths_to_edges_by_weight,
)
from ...internals.nx.internal__compute_spring_layout_positions import (
    internal__compute_spring_layout_positions,
)
from ...internals.nx.internal__create_network_plot import internal__create_network_plot
from ...internals.nx_mixin.nx_spring_layout_params import (
    NxSpringLayoutParams,
    NxSpringLayoutParamsMixin,
)
from ...internals.params.axes_params import AxesParams, AxesParamsMixin
from ...internals.params.columns_and_rows_params import ColumnsAndRowsParamsMixin
from ...internals.params.item_params import ItemParams
from .data_frame import CrossCoOccurrenceDataFrame
from .internals.output_params import OutputParams, OutputParamsMixin
from .matrix_data_frame import CrossCoOccurrenceMatrix


@dataclass
class PlotParams:
    """:meta private:"""

    #
    # NODES:
    node_size_range: Tuple[int, int] = (30, 70)
    textfont_size_range: Tuple[int, int] = (10, 20)
    textfont_opacity_range: Tuple[float, float] = (0.35, 1.00)
    #
    # EDGES:
    edge_color: str = "#b8c6d0"
    edge_width_range: Tuple[float, float] = (0.8, 4.0)


class PlotParamsMixin:
    """:meta private:"""

    def set_plot_params(self, **kwargs):
        """Set database parameters."""
        for key, value in kwargs.items():
            if hasattr(self.plot_params, key):
                setattr(self.plot_params, key, value)
            else:
                raise ValueError(f"Invalid parameter for PlotParams: {key}")
        return self


class CrossCoOccurrenceNetworkPlot(
    ColumnsAndRowsParamsMixin,
    SetDatabaseFiltersMixin,
    OutputParamsMixin,
    NxSpringLayoutParamsMixin,
    AxesParamsMixin,
    PlotParamsMixin,
):
    """:meta private:"""

    def __init__(self):

        self.axes_params = AxesParams()
        self.columns_params = ItemParams()
        self.database_params = DatabaseFilters()
        self.nx_sprint_layout_params = NxSpringLayoutParams()
        self.output_params = OutputParams()
        self.plot_params = PlotParams()
        self.rows_params = ItemParams()

    def build(self):

        cooc_matrix = (
            CrossCoOccurrenceMatrix()
            .set_columns_params(**self.columns_params.__dict__)
            .set_rows_params(**self.rows_params.__dict__)
            .set_output_params(**self.output_params.__dict__)
            .set_database_params(**self.database_params.__dict__)
            .build()
        )

        #
        # Create the networkx graph
        nx_graph = nx.Graph()
        nx_graph = _add_nodes_from_co_occurrence_matrix(nx_graph, cooc_matrix)
        nx_graph = _add_weighted_edges_from_co_occurrence_matrix(nx_graph, cooc_matrix)

        #
        # Sets the layout
        nx_graph = self.nx_compute_spring_layout_positions(nx_graph)

        #
        # Sets the node attributes
        nx_graph = internal__assign_sizes_to_nodes_by_occurrences(
            nx_graph, node_size_range
        )
        nx_graph = nx_assign_textfont_sizes_to_nodes_by_occurrences(
            nx_graph, textfont_size_range
        )

        nx_graph = internal__assign_opacity_to_text_by_frequency(
            nx_graph, textfont_opacity_range
        )
        #
        # Sets the edge attributes
        nx_graph = internal__assign_widths_to_edges_by_weight(
            nx_graph, edge_width_range
        )
        nx_graph = internal__assign_text_positions_to_nodes_by_quadrants(nx_graph)

        nx_graph = internal__assign_uniform_color_to_edges(nx_graph, edge_color)

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


#######
def _add_nodes_from_co_occurrence_matrix(
    nx_graph,
    cooc_matrix,
):
    #
    # Adds rows nodes
    matrix = cooc_matrix.copy()
    nodes = matrix.index.tolist()
    nx_graph.add_nodes_from(nodes, group=0, node_color="#7793a5")

    #
    # Adds columns nodes
    if matrix.index.tolist() != matrix.columns.tolist():
        nodes = matrix.columns.tolist()
        nx_graph.add_nodes_from(nodes, group=1, node_color="#465c6b")

    for node in nx_graph.nodes():
        nx_graph.nodes[node]["text"] = node

    return nx_graph


def _add_weighted_edges_from_co_occurrence_matrix(nx_graph, cooc_matrix):
    #
    # Adds links from ...
    #
    matrix = cooc_matrix.copy()

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
                        dash="solid",
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
                    dash="solid",
                )

    return nx_graph
