# flake8: noqa
"""
.. _gantt_chart:

Gantt Chart
===============================================================================


>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/gantt_chart.html"

>>> import techminer2plus
>>> data = techminer2plus.terms_by_year(
...    field='author_keywords',
...    top_n=20,
...    root_dir=root_dir,
... )
>>> chart = techminer2plus.gantt_chart(data)
>>> chart.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/gantt_chart.html" height="800px" width="100%" frameBorder="0"></iframe>

    
>>> chart.table_.head(10)
year                            2017  2018  2019  2020  2021  2022  2023
author_keywords                                                         
REGTECH 28:329                     2     3     4     8     3     6     2
FINTECH 12:249                     0     2     4     3     1     2     0
REGULATORY_TECHNOLOGY 07:037       0     0     0     2     3     2     0
COMPLIANCE 07:030                  0     0     1     3     1     1     1
REGULATION 05:164                  0     2     0     1     1     1     0
ANTI_MONEY_LAUNDERING 05:034       0     0     0     2     3     0     0
FINANCIAL_SERVICES 04:168          1     1     0     1     0     1     0
FINANCIAL_REGULATION 04:035        1     0     0     1     0     2     0
ARTIFICIAL_INTELLIGENCE 04:023     0     0     1     2     0     1     0
RISK_MANAGEMENT 03:014             0     1     0     1     0     1     0





# pylint: disable=line-too-long    
"""
from dataclasses import dataclass

import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

# from ..analyze import terms_by_year
# from ..classes import BasicChart


@dataclass
class GanttChart:
    """Gantt Chart.

    :meta private:
    """

    plot_: go.Figure
    table_: pd.DataFrame


COLOR = "#556f81"
TEXTLEN = 40


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def gantt_chart(
    terms_by_year=None,
    title=None,
):
    """Creates a Gantt Chart from a terms by year table."""

    def compute_table(obj):
        """Melt the data"""

        table = obj.table_.copy()
        table["RANKING"] = range(1, len(table) + 1)
        table = table.melt(
            value_name="OCC",
            var_name="column",
            ignore_index=False,
            id_vars=["RANKING"],
        )

        table = table[table.OCC > 0]
        table = table.sort_values(by=["RANKING"], ascending=True)
        table = table.drop(columns=["RANKING"])

        table = table.rename(columns={"column": "Year"})
        table = table.reset_index()

        return table

    def create_fig(table, criterion, metric, title):
        """Create the figure"""

        fig = px.scatter(
            table,
            x="Year",
            y=criterion,
            size=metric,
            hover_data=table.columns.to_list(),
            title=title,
            color=criterion,
        )
        fig.update_layout(
            paper_bgcolor="white",
            plot_bgcolor="white",
            showlegend=False,
            xaxis_title=None,
            yaxis_title=criterion.replace("_", " ").upper(),
        )
        fig.update_traces(
            marker={
                # "line": {"color": COLOR, "width": 1},
                "line": {"color": "white", "width": 0.5},
                "opacity": 1.0,
            },
            marker_color=COLOR,
            mode="lines+markers",
            line={"width": 2, "color": COLOR},
        )
        fig.update_xaxes(
            linecolor="white",
            linewidth=1,
            gridcolor="gray",
            griddash="dot",
            tickangle=270,
            dtick=1.0,
        )
        fig.update_yaxes(
            linecolor="white",
            linewidth=1,
            gridcolor="gray",
            griddash="dot",
        )

        return fig

    #
    # Main code:
    #

    title = "Gantt Chart" if title is None else title

    table = compute_table(terms_by_year)
    fig = create_fig(table, terms_by_year.field_, terms_by_year.metric_, title)

    return GanttChart(
        plot_=fig,
        table_=terms_by_year.table_,
    )
