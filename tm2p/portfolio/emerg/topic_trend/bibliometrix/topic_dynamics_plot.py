"""
TopicDynamicsPlot
===============================================================================

.. raw:: html

    <iframe src="../_generated/px.portfolio.emerg.topic_trend.bibliometrix.topic_dynamics_plot.html"
    height="600px" width="100%" frameBorder="0"></iframe>


Smoke tests:
    >>> from tm2p.enum import AnalysisUnit  # type: ignore 
    >>> from tm2p.enum import UnitOrderBy  # type: ignore
    >>> from tm2p.portfolio.emerg.topic_trend.bibliometrix import TopicDynamicsPlot
    >>> fig = (
    ...     TopicDynamicsPlot()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.CONCEPT)
    ...     .having_top_n_units_per_year(5)
    ...     #
    ...     .having_top_n_units(100)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
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
    >>> fig.write_html("docsrc/_generated/px.portfolio.emerg.topic_trend.bibliometrix.topic_dynamics_plot.html")



"""

import plotly.graph_objects as go  # type: ignore

from tm2p._intern import ParamsMixin
from tm2p.portfolio.emerg.topic_trend.bibliometrix.topic_dynamics import TopicDynamics


class TopicDynamicsPlot(
    ParamsMixin,
):
    """:meta private:"""

    # ---------------------------------------------------------------------------
    def run(self):

        words_by_year = (
            TopicDynamics()
            .update(**self.params.__dict__)
            .update(terms_order_by="OCC")
            .run()
        )

        fig = go.Figure(
            go.Bar(
                x=words_by_year.WIDTH,
                y=words_by_year.index,
                base=words_by_year.YEAR_Q1,
                width=words_by_year.HEIGHT,
                orientation="h",
                marker_color="lightslategrey",
            ),
        )
        fig.update_layout(
            paper_bgcolor="white",
            plot_bgcolor="white",
        )
        fig.update_yaxes(
            linecolor="gray",
            linewidth=1,
            gridcolor="lightgray",
            griddash="dot",
        )
        fig.update_xaxes(
            linecolor="gray",
            linewidth=1,
            gridcolor="lightgray",
            griddash="dot",
            tickangle=270,
            dtick=1.0,
        )

        return fig


#
