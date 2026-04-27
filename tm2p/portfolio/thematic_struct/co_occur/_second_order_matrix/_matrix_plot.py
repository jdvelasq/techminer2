"""
MatrixPlot
===============================================================================

.. raw:: html

    <iframe src="../_generated/px.portfolio.thematic_stucture.co_occurrence.second_order_matrix.matrix_plot.html"
    height="600px" width="100%" frameBorder="0"></iframe>

Smoke tests:
    >>> from tm2p.enum import AssociationIndex, Field, UnitOrderBy
    >>> from tm2p.portfolio.thematic_stucture.co_occurrence.second_order_matrix import MatrixPlot
    >>> fig = (
    ...     MatrixPlot()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.AUTHKW_NORM)
    ...     .having_top_n_units(10)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
    ...     #
    ...     .using_minimum_pair_co_occurrence(1)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # NETWORK:
    ...     .using_spring_layout_k(None)
    ...     .using_spring_layout_iterations(30)
    ...     .using_spring_layout_seed(0)
    ...     #
    ...     .using_node_n_labels(4)
    ...     .using_node_size_range(30, 70)
    ...     .using_node_colors(("#7793a5", "#465c6b"))
    ...     .using_textfont_size_range(10, 20)
    ...     .using_textfont_opacity_range(0.35, 1.00)
    ...     #
    ...     .using_edge_colors(("#b8c6d0",))
    ...     .using_edge_width_range(0.8, 4.0)
    ...     #
    ...     .using_xaxes_range(None, None)
    ...     .using_yaxes_range(None, None)
    ...     .using_axes_visible(False)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> assert type(fig).__name__ == 'Figure'    >>> fig.write_html("docsrc/_generated/px.portfolio.thematic_stucture.co_occurrence.second_order_matrix.matrix_plot.html")

"""

from tm2p._intern import ParamsMixin

from ...cross_occur.matrix.matrix_plot import MatrixPlot as BaseMatrixPlot


class MatrixPlot(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        return (
            BaseMatrixPlot()
            .update(**self.params.__dict__)
            #
            # COLUMNS:
            .with_column_analysis_unit(self.params.source_field)
            .having_column_units_in_top(self.params.top_n_units)
            .having_column_units_ordered_by(self.params.unit_order_by)
            .having_column_unit_occurrence_between(
                self.params.unit_occurrence_range[0],
                self.params.unit_occurrence_range[1],
            )
            .having_column_unit_citation_between(
                self.params.unit_global_citation_range[0],
                self.params.unit_global_citation_range[1],
            )
            .having_column_units_in(self.params.units_in)
            #
            # ROWS:
            .with_index_analysis_unit(self.params.source_field)
            .having_index_units_in_top(self.params.top_n_units)
            .having_index_units_ordered_by(self.params.unit_order_by)
            .having_index_unit_occurrence_between(
                self.params.unit_occurrence_range[0],
                self.params.unit_occurrence_range[1],
            )
            .having_index_unit_citation_between(
                self.params.unit_global_citation_range[0],
                self.params.unit_global_citation_range[1],
            )
            .having_index_units_in(self.params.units_in)
            #
            .run()
        )
