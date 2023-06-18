# flake8: noqa
"""
Indicators by Year Plot
===============================================================================

Creates a time line plot from a dataframe of indicators by year.


Example
-------------------------------------------------------------------------------

>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/time_plot.html"
>>> import techminer2plus
>>> indicators = techminer2plus.system.indicators.indicators_by_year(root_dir)
>>> indicators_by_year_plot(
...     indicators,
...     metric="mean_global_citations",
...     title="Average Citations per Year",
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../_static/time_plot.html" height="600px" width="100%" 
    frameBorder="0"></iframe>

"""
import plotly.express as px


def indicators_by_year_plot(
    indicators_by_year,
    metric,
    title,
):
    """Makes a time line plot for indicators."""

    column_names = {
        column: column.replace("_", " ").title()
        for column in indicators_by_year.columns
        if column not in ["OCC", "cum_OCC"]
    }
    column_names["OCC"] = "OCC"
    column_names["cum_OCC"] = "cum_OCC"
    indicators_by_year = indicators_by_year.rename(columns=column_names)

    fig = px.line(
        indicators_by_year,
        x=indicators_by_year.index,
        y=column_names[metric],
        title=title,
        markers=True,
        hover_data=["OCC", "Global Citations", "Local Citations"],
    )
    fig.update_traces(
        marker=dict(size=10, line=dict(color="darkslategray", width=2)),
        marker_color="rgb(171,171,171)",
        line=dict(color="darkslategray"),
    )
    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
    )
    fig.update_yaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="lightgray",
        griddash="dot",
    )
    fig.update_xaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="lightgray",
        griddash="dot",
        tickangle=270,
    )
    return fig
