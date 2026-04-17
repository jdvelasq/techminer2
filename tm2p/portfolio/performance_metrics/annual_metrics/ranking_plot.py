"""
RankingPlot
===============================================================================

.. raw:: html

    <iframe src="../_generated/px.portfolio.performance_metrics.annual_metrics.mean_citations_per_year.html"
    height="600px" width="100%" frameBorder="0"></iframe>

    <iframe src="../_generated/px.portfolio.performance_metrics.annual_metrics.annual_scientific_production.html"
    height="600px" width="100%" frameBorder="0"></iframe>


Smoke tests:
    >>> from tm2p.portfolio.performance_metrics.annual_metrics import Column
    >>> from tm2p.portfolio.performance_metrics.annual_metrics import RankingPlot
    >>> fig = (
    ...     RankingPlot()
    ...     #
    ...     .with_plotting_column(Column.MEAN_GCS_PER_YEAR)
    ...     #
    ...     .using_title_text("Mean Citations Per Year")
    ...     .using_xaxes_title_text("Years")
    ...     .using_yaxes_title_text("Mean Citations Per Year")
    ...     #
    ...     .using_line_width(1.5)
    ...     .using_marker_size(7)
    ...     .using_textfont_size(10)
    ...     .using_yshift(4)
    ...     #
    ...     .where_root_directory("tests/scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     #
    ...     .run()
    ... )
    >>> type(fig).__name__
    'Figure'
    >>> fig.write_html("docsrc/_generated/px.portfolio.performance_metrics.annual_metrics.mean_citations_per_year.html")

    >>> fig = (
    ...     RankingPlot()
    ...     #
    ...     .with_plotting_column(Column.OCC)
    ...     #
    ...     .using_title_text("Annual Scientific Production")
    ...     .using_xaxes_title_text("Years")
    ...     .using_yaxes_title_text("Documents")
    ...     #
    ...     .using_line_width(1.5)
    ...     .using_marker_size(7)
    ...     .using_textfont_size(10)
    ...     .using_yshift(4)
    ...     #
    ...     .where_root_directory("tests/scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     #
    ...     .run()
    ... )
    >>> type(fig).__name__
    'Figure'
    >>> fig.write_html("docsrc/_generated/px.portfolio.performance_metrics.annual_metrics.annual_scientific_production.html")



"""

import plotly.express as px  # type: ignore

from tm2p._intern import ParamsMixin
from tm2p.portfolio.performance_metrics.annual_metrics.metrics import Metrics

MARKER_COLOR = "#7793a5"
MARKER_LINE_COLOR = "#465c6b"


class RankingPlot(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        df = Metrics().update(**self.params.__dict__).run()
        df["Rank"] = range(1, len(df) + 1)

        fig = px.line(
            df,
            x="Rank",
            y=self.params.ranking_plotting_column.value,  # type: ignore
            hover_data=df.columns.to_list(),
            markers=True,
        )

        fig.update_traces(
            marker={
                "size": self.params.marker_size,
                "line": {
                    "color": MARKER_LINE_COLOR,
                    "width": 1,
                },
            },
            marker_color=MARKER_COLOR,
            line={
                "color": MARKER_LINE_COLOR,
                "width": self.params.line_width,
            },
        )
        fig.update_layout(
            paper_bgcolor="white",
            plot_bgcolor="white",
            title_text=self.params.title_text,
        )
        fig.update_yaxes(
            linecolor="gray",
            linewidth=1,
            gridcolor="lightgray",
            griddash="dot",
            title=self.params.yaxes_title_text,
        )
        fig.update_xaxes(
            linecolor="gray",
            linewidth=1,
            gridcolor="lightgray",
            griddash="dot",
            title=self.params.xaxes_title_text,
        )

        for name, row in df.iterrows():
            fig.add_annotation(
                x=row["Rank"],
                y=row[self.params.ranking_plotting_column.value],  # type: ignore
                text=name,
                showarrow=False,
                textangle=-90,
                yanchor="bottom",
                font={
                    "size": self.params.textfont_size_uniform,
                },
                yshift=self.params.yshift,
            )

        return fig
