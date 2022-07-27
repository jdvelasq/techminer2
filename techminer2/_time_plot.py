"""
Time Plot
===============================================================================

See :doc:`annual indicators <annual_indicators>` to obtain a `pandas.Dataframe` 
with the data.


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/time_plot.html"

>>> from ._indicators.indicators_by_year import indicators_by_year
>>> from techminer2._time_plot import time_plot

>>> indicators = indicators_by_year(directory=directory)
>>> time_plot(
...     indicators,
...     metric="OCC",
...     title="Annual Scientific Production",
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/time_plot.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
import plotly.express as px


def time_plot(
    indicators,
    metric,
    title,
):
    """Makes a time line plot for indicators."""

    column_names = {
        column: column.replace("_", " ").title()
        for column in indicators.columns
        if column not in ["OCC", "cum_OCC"]
    }
    column_names["OCC"] = "OCC"
    column_names["cum_OCC"] = "cum_OCC"
    indicators = indicators.rename(columns=column_names)

    fig = px.line(
        indicators,
        x=indicators.index,
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
