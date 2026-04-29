"""
Sankey Plot
===============================================================================

.. raw:: html

    <iframe src="../_generated/px.portfolio.thematic_struct.sankey.sankey_plot.html"
    height="800px" width="100%" frameBorder="0"></iframe>


Smoke tests:
    >>> from tm2p.enum import AnalysisUnit
    >>> from tm2p.portfolio.thematic_struct.sankey import SankeyPlot
    >>> fig = (
    ...     SankeyPlot()
    ...     #
    ...     # ANALYSIS UNITS:
    ...     .with_analysis_units(
    ...         [
    ...             AnalysisUnit.CTRY,
    ...             AnalysisUnit.AUTH,
    ...             AnalysisUnit.CONCEPT,
    ...         ]
    ...     )
    ...     .having_sankey_top_n_units((20, 20, 10))
    ...     #
    ...     # PLOT:
    ...     .using_color("#7793a5")
    ...     .using_uniform_textfont_size(8)
    ...     .using_title_text("Sankey Plot")
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> assert type(fig).__name__ == 'Figure'
    >>> fig.write_html("docsrc/_generated/px.portfolio.thematic_struct.sankey.sankey_plot.html")


"""

import plotly.graph_objects as go  # type: ignore

from tm2p._intern import ParamsMixin
from tm2p.enum import UnitOrderBy
from tm2p.portfolio.thematic_struct.cross_occur.matrix import Matrix


class SankeyPlot(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def _step_01_build_matrices(self):

        matrices = []
        units = self.params.analysis_units
        top_n = self.params.top_n_sankey_units

        for (
            idx,
            col_unit,
            idx_top_n,
            col_top_n,
        ) in zip(
            units[:-1],
            units[1:],
            top_n[:-1],
            top_n[1:],
        ):

            matrix = (
                Matrix()
                .update(**self.params.__dict__)
                #
                # COLUMNS:
                .with_column_analysis_unit(col_unit)
                .having_column_units_ordered_by(UnitOrderBy.OCC)
                .having_column_units_in_top(col_top_n)
                .having_column_unit_occurrence_between(None, None)
                .having_column_unit_citation_between(None, None)
                .having_column_units_in(None)
                #
                # ROWS:
                .with_index_analysis_unit(idx)
                .having_index_units_ordered_by(UnitOrderBy.OCC)
                .having_index_units_in_top(idx_top_n)
                .having_index_unit_occurrence_between(None, None)
                .having_index_unit_citation_between(None, None)
                .having_index_units_in(None)
                #
                .using_minimum_pair_co_occurrence(1)
                #
                .run()
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
        return {key: pos for pos, key in enumerate(node_names)}

    # -------------------------------------------------------------------------
    def _step_04_build_links(self, matrices, node_indexes):

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
            font_size=self.params.textfont_size_uniform,
        )
        return fig

    # -------------------------------------------------------------------------
    def run(self):

        matrices = self._step_01_build_matrices()
        node_names = self._step_02_build_node_names(matrices)
        node_indexes = self._step_03_build_node_indexes(node_names)
        links = self._step_04_build_links(matrices, node_indexes)
        fig = self._step_05_build_diagram(node_names, links)

        return fig
