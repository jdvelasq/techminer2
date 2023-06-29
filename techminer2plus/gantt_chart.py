# flake8: noqa
# pylint: disable=line-too-long
"""
.. _gantt_chart:

Gantt Chart
===============================================================================


>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/gantt_chart.html"

>>> import techminer2plus
>>> import techminer2plus as tm2p
>>> root_dir = "data/regtech/"
>>> (
...     tm2p.Records(root_dir=root_dir)
...     .field("author_keywords", top_n=10)
...     .terms_by_year()
...     .gantt_chart()
...     .write_html(file_name)
... )

.. raw:: html

    <iframe src="../_static/gantt_chart.html" height="800px" width="100%" frameBorder="0"></iframe>

"""
import plotly.express as px

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

        table = obj.frame_.copy()
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
    fig = create_fig(table, terms_by_year.field_, "OCC", title)

    return fig
