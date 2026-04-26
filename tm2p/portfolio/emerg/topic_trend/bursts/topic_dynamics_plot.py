"""
TopicDynamicsPlot
===============================================================================

.. raw:: html

    <iframe src="../_generated/px.portfolio.emergence.topic_trends.burst.topic_dynamics_plot.html"
    height="600px" width="100%" frameBorder="0"></iframe>

Smoke tests:
    >>> from tm2p.enum import Field, UnitOrderBy
    >>> from tm2p.portfolio.emergence.topic_trends.bursts import TopicDynamicsPlot
    >>> fig = (
    ...     TopicDynamicsPlot()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.CONCEPT_NORM)
    ...     .having_top_n_units(50)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # KLEINBERG BURST:
    ...     .using_kleinberg_burst_rate(2.0)
    ...     .using_kleinberg_burst_gamma(1.0)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> fig.write_html("docsrc/_generated/px.portfolio.emergence.topic_trends.burst.topic_dynamics_plot.html")



"""

import plotly.graph_objects as go  # type: ignore

from tm2p._intern import ParamsMixin
from tm2p.portfolio.emerg.topic_trend.bursts.topic_dynamics import TopicDynamics


class TopicDynamicsPlot(
    ParamsMixin,
):
    """:meta private:"""

    # ---------------------------------------------------------------------------
    def run(self):

        df = TopicDynamics().update(**self.params.__dict__).run()
        min_occ = df.OCC.min()
        max_occ = df.OCC.max()
        df["height"] = 0.15 + 0.82 * (df.OCC - min_occ) / (max_occ - min_occ)

        df["width"] = df.DURATION

        fig = go.Figure(
            go.Bar(
                x=df.width,
                y=df.index,
                base=df.START,
                width=df.height,
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
