# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Matrix Plot
===============================================================================


>>> from techminer2.pkgs.associations import MatrixPlot
>>> plot = (
...     MatrixPlot()
...     #
...     # FIELD:
...     .with_field("author_keywords")
...     .having_terms_in_top(10)
...     .having_terms_ordered_by("OCC")
...     .having_term_occurrences_between(None, None)
...     .having_term_citations_between(None, None)
...     .having_terms_in(["FINTECH", "INNOVATION", "FINANCIAL_SERVICES"])
...     #
...     # ROWS:
...     .having_other_terms_in_top(10)
...     .having_other_terms_ordered_by("OCC")
...     .having_other_term_occurrences_between(None, None)
...     .having_other_term_citations_between(None, None)
...     .having_other_terms_in(None)
...     #
...     # COUNTERS:
...     .using_term_counters(True)
...     #
...     # NETWORK:
...     .using_spring_layout_k(None)
...     .using_spring_layout_iterations(30)
...     .using_spring_layout_seed(0)
...     #
...     .using_node_size_range(30, 70)
...     .using_node_colors(["#7793a5", "#465c6b"])
...     .using_textfont_size_range(10, 20)
...     .using_textfont_opacity_range(0.35, 1.00)
...     #
...     .using_edge_colors(["#b8c6d0"])
...     .using_edge_width_range(0.8, 4.0)
...     #
...     .using_xaxes_range(None, None)
...     .using_yaxes_range(None, None)
...     .using_axes_visible(False)
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     .where_records_match(None)
...     #
...     .build()
... )
>>> # plot.write_html("sphinx/_generated/pkgs/associations/matrix_plot.html")

.. raw:: html
    
    <iframe src="../../_generated/pkgs/associations/matrix_plot.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
"""
import networkx as nx  # type: ignore

from ...internals.mixins import ParamsMixin
from ...internals.nx import (
    internal__assign_constant_to_edge_colors,
    internal__assign_edge_widths_based_on_weight,
    internal__assign_node_sizes_based_on_occurrences,
    internal__assign_text_positions_based_on_quadrants,
    internal__assign_textfont_opacity_based_on_occurrences,
    internal__assign_textfont_sizes_based_on_occurrences,
    internal__compute_spring_layout_positions,
    internal__plot_nx_graph,
)
from .data_frame import DataFrame


class MatrixPlot(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def _step_01_create_data_frame(self):
        return DataFrame().update(**self.params.__dict__).build()

    # -------------------------------------------------------------------------
    def _step_02_create_a_empty_networkx_graph(self):
        return nx.Graph()

    # -------------------------------------------------------------------------
    def _step_03_add_nodes_from_matrix(self, nx_graph, matrix):

        #
        # Node colors
        row_node_color = self.params.node_colors[0]
        col_node_color = self.params.node_colors[1]

        #
        # Adds rows nodes
        matrix = matrix.copy()
        nodes = matrix.index.tolist()
        nx_graph.add_nodes_from(nodes, group=0, node_color=row_node_color)

        #
        # Adds texts
        for node in nx_graph.nodes():
            nx_graph.nodes[node]["text"] = node
            if node in matrix.columns.to_list():
                nx_graph.nodes[node]["node_color"] = col_node_color

        return nx_graph

    # -------------------------------------------------------------------------
    def _step_04_add_weighted_edges_from_matrix(self, nx_graph, matrix):

        matrix = matrix.copy()

        # delete rows matching column names
        matrix = matrix.drop(index=matrix.columns)

        for row in matrix.index.tolist():
            for col in matrix.columns.tolist():

                weight = matrix.loc[row, col]
                nx_graph.add_weighted_edges_from(
                    ebunch_to_add=[(row, col, weight)],
                    dash="solid",
                )

        return nx_graph

    # -------------------------------------------------------------------------
    def _step_05_compute_spring_layout_positions(self, nx_graph):
        return internal__compute_spring_layout_positions(
            self.params,
            nx_graph,
        )

    # -------------------------------------------------------------------------
    def _step_06_assign_node_sizes_based_on_occurrences(self, nx_graph):
        return internal__assign_node_sizes_based_on_occurrences(
            self.params,
            nx_graph,
        )

    # -------------------------------------------------------------------------
    def _step_07_assign_textfont_sizes_based_on_occurrences(self, nx_graph):
        return internal__assign_textfont_sizes_based_on_occurrences(
            self.params,
            nx_graph,
        )

    # -------------------------------------------------------------------------
    def _step_08_assign_text_opacity_based_on_occurrences(self, nx_graph):
        return internal__assign_textfont_opacity_based_on_occurrences(
            self.params, nx_graph
        )

    # -------------------------------------------------------------------------
    def _step_09_assign_edge_colors_based_on_weight(self, nx_graph):
        return internal__assign_constant_to_edge_colors(
            self.params,
            nx_graph,
        )

    # -------------------------------------------------------------------------
    def _step_10_assign_edge_widths_based_on_weight(self, nx_graph):
        return internal__assign_edge_widths_based_on_weight(
            self.params,
            nx_graph,
        )

    # -------------------------------------------------------------------------
    def _step_11_assign_text_positions_based_on_quadrants(self, nx_graph):
        return internal__assign_text_positions_based_on_quadrants(nx_graph)

    # -------------------------------------------------------------------------
    def build(self):

        cooc_matrix = self._step_01_create_data_frame()

        nx_graph = self._step_02_create_a_empty_networkx_graph()
        nx_graph = self._step_03_add_nodes_from_matrix(nx_graph, cooc_matrix)
        nx_graph = self._step_04_add_weighted_edges_from_matrix(nx_graph, cooc_matrix)
        nx_graph = self._step_05_compute_spring_layout_positions(nx_graph)
        nx_graph = self._step_06_assign_node_sizes_based_on_occurrences(nx_graph)
        nx_graph = self._step_07_assign_textfont_sizes_based_on_occurrences(nx_graph)
        nx_graph = self._step_08_assign_text_opacity_based_on_occurrences(nx_graph)
        nx_graph = self._step_09_assign_edge_colors_based_on_weight(nx_graph)
        nx_graph = self._step_10_assign_edge_widths_based_on_weight(nx_graph)
        nx_graph = self._step_11_assign_text_positions_based_on_quadrants(nx_graph)

        return internal__plot_nx_graph(
            params=self.params,
            nx_graph=nx_graph,
        )
