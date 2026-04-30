"""
MatrixPlot
===============================================================================

.. raw:: html

    <iframe src="../_generated/px.portfolio.thematic_struct.co_occur.matrix.matrix_plot.html"
    height="600px" width="100%" frameBorder="0"></iframe>

Smoke tests:
    >>> from tm2p.enum import Field, UnitOrderBy, Scaling
    >>> from tm2p.portfolio.thematic_struct.co_occur.matrix import MatrixPlot
    >>> fig = (
    ...     MatrixPlot()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.AUTHKW_NORM)
    ...     #
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
    ...     .using_node_colors(("#7793a5", "#465c6b"))
    ...     .using_node_scaling(Scaling.SQRT)
    ...     .using_node_size_range(30, 70)
    ...     .using_textfont_opacity_range(0.35, 1.00)
    ...     .using_textfont_size_range(10, 20)
    ...     .using_max_node_labels(4)
    ...     #
    ...     .using_edge_colors(("#b8c6d0",))
    ...     .using_edge_scaling(Scaling.SQRT)
    ...     .using_global_top_edges(1000)
    ...     .using_edge_width_range(0.8, 4.0)
    ...     .using_min_node_degree(2)
    ...     .using_top_edges_per_node(5)
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
    >>> assert type(fig).__name__ == 'Figure'    >>> fig.write_html("docsrc/_generated/px.portfolio.thematic_struct.co_occur.matrix.matrix_plot.html")

"""

from tm2p._intern import ParamsMixin
from tm2p._intern.plots.adv.co_occ_matrix_plot import build_co_occ_matrix_plot

from .matrix import CountMatrix


class CountMatrixPlot(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        matrix = CountMatrix().update(**self.params.__dict__).run()
        fig = build_co_occ_matrix_plot(self.params, matrix)

        return fig
