"""
Annual Scientific Production
===============================================================================


>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/images/annual_scientific_production.png"
>>> annual_scientific_production(directory).write_image(file_name)

.. image:: images/annual_scientific_production.png
    :width: 700px
    :align: center


"""
import plotly.express as px

from .annual_indicators import annual_indicators


def annual_scientific_production(directory="./"):

    indicators = annual_indicators(directory)
    fig = px.line(
        x=indicators.index,
        y=indicators.num_documents,
        title="Annual Scientific Production",
        markers=True,
        text=indicators.num_documents,
        labels={"x": "Year", "y": "Number of publications"},
    )
    fig.update_traces(marker=dict(size=12))
    fig.update_traces(textposition="bottom right")
    fig.update_traces(line=dict(color="black"))
    fig.update_xaxes(tickangle=270)
    fig.update_layout(paper_bgcolor="white", plot_bgcolor="white")
    fig.update_xaxes(linecolor="gray", gridcolor="lightgray")
    fig.update_yaxes(linecolor="gray", gridcolor="lightgray")
    return fig
