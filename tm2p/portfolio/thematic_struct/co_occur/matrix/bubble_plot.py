"""
BubbleChart
===============================================================================

.. raw:: html

    <iframe src="../_generated/px.portfolio.thematic_struct.co_occur.matrix.bubble_plot.html"
    height="600px" width="100%" frameBorder="0"></iframe>

Smoke tests:
    >>> from tm2p.enum import Field, UnitOrderBy
    >>> from tm2p.portfolio.thematic_struct.co_occur.matrix import BubblePlot
    >>> fig = (
    ...     BubblePlot()
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
    ...     # PLOT:
    ...     .using_title_text(None)
    ...     .using_colormap("Blues")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> assert type(fig).__name__ == 'Figure'    >>> fig.write_html("docsrc/_generated/px.portfolio.thematic_struct.co_occur.matrix.bubble_plot.html")


"""

from tm2p._intern import ParamsMixin
from tm2p._intern.plots.basic.bubble_plot import bubble_plot

from .matrix_list import MatrixList


class BubblePlot(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        data_frame = MatrixList().update(**self.params.__dict__).run()

        fig = bubble_plot(
            self.params,
            x_name="ROWS",
            y_name="COLUMNS",
            size_col="OCC",
            dataframe=data_frame,
        )

        return fig
