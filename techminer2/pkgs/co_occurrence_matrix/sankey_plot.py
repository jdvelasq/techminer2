# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Sankey Plot
===============================================================================

>>> from techminer2.pkgs.co_occurrence_matrix import SankeyPlot
>>> plot = (
...     SankeyPlot()
...     #
...     # FIELDS:
...     .with_field("authors")
...     .having_terms_in_top(10)
...     .having_term_occurrences_between(None, None)
...     .having_term_citations_between(None, None)
...     .having_terms_in(None)
...     #
...     .with_other_field(["countries", "author_keywords"])
...     #
...     # PLOT:
...     .using_color(None)
...     .using_textfont_size(8)
...     .using_title_text("Bar Plot")
...     #
...     # COUNTERS:
...     .using_term_counters(True)
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
>>> # plot.write_html("sphinx/_generated/pkgs/co_occurrence_matrix/sankey_plot.html")

.. raw:: html

    <iframe src="../../_generated/pkgs/co_occurrence_matrix/sankey_plot.html" 
    height="800px" width="100%" frameBorder="0"></iframe>

"""
import plotly.graph_objects as go  # type: ignore

from ..._internals.mixins import ParamsMixin
from .matrix_data_frame import MatrixDataFrame


class SankeyPlot(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def _step_01_build_matrices(self):

        matrices = []
        fields = [self.params.field] + self.params.other_field

        for row_field, col_field in zip(fields[:-1], fields[1:]):

            matrix = (
                MatrixDataFrame()
                .update(**self.params.__dict__)
                #
                # COLUMNS:
                .with_field(
                    col_field,
                )
                .having_terms_in_top(
                    self.params.top_n,
                )
                .having_term_occurrences_between(
                    self.params.term_occurrences_range[0],
                    self.params.term_occurrences_range[1],
                )
                .having_term_citations_between(
                    self.params.term_citations_range[0],
                    self.params.term_citations_range[1],
                )
                .having_terms_in(
                    self.params.terms_in,
                )
                #
                # ROWS:
                .with_other_field(
                    row_field,
                )
                .having_other_terms_in_top(
                    self.params.top_n,
                )
                .having_other_term_occurrences_between(
                    self.params.term_occurrences_range[0],
                    self.params.term_occurrences_range[1],
                )
                .having_other_term_citations_between(
                    self.params.term_citations_range[0],
                    self.params.term_citations_range[1],
                )
                .having_other_terms_in(
                    self.params.terms_in,
                )
                .build()
            )

            matrices.append(matrix)

        return matrices

    # -------------------------------------------------------------------------
    def _step_02_build_node_names(self, matrices):

        node_names = []
        for i_matrix, matrix in enumerate(matrices):
            if i_matrix == 0:
                node_names.extend(matrix.index.to_list())
            node_names.extend(matrix.columns.to_list())

        return node_names

    # -------------------------------------------------------------------------

    def _step_03_build_node_indexes(self, node_names):
        """Builds the node indices"""
        return {key: pos for pos, key in enumerate(node_names)}

    # -------------------------------------------------------------------------
    def _step_04_build_links(self, matrices, node_indexes):
        """Links are a node dictionary with source, target and value"""

        source = []
        target = []
        value = []

        for coc_matrix in matrices:
            matrix = coc_matrix.copy()

            for row in matrix.index:
                for col in matrix.columns:
                    source.append(node_indexes[row])
                    target.append(node_indexes[col])
                    value.append(matrix.loc[row, col])
        return {"source": source, "target": target, "value": value}

    # -------------------------------------------------------------------------
    def _step_05_build_diagram(self, node_names, links):
        fig = go.Figure(
            data=[
                go.Sankey(
                    node={
                        "label": node_names,
                        "color": self.params.color,
                    },
                    link=links,
                )
            ]
        )
        fig.update_layout(
            title_text=self.params.title_text,
            font_size=self.params.textfont_size,
        )
        return fig

    # -------------------------------------------------------------------------
    def build(self):

        matrices = self._step_01_build_matrices()
        node_names = self._step_02_build_node_names(matrices)
        node_indexes = self._step_03_build_node_indexes(node_names)
        links = self._step_04_build_links(matrices, node_indexes)
        fig = self._step_05_build_diagram(node_names, links)

        return fig
