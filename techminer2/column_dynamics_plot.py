"""
Column dynamics plot
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/images/column_dynamics_plot.png"

>>> column_dynamics_plot(
...     column='iso_source_name', 
...     top_n=10, 
...     directory=directory,
... ).write_image(file_name)

.. image:: images/column_dynamics_plot.png
    :width: 700px
    :align: center

"""
import plotly.express as px

from .column_dynamics_table import column_dynamics_table


def column_dynamics_plot(
    column,
    top_n=10,
    directory="./",
):
    dynamics = column_dynamics_table(
        column=column,
        top_n=top_n,
        directory=directory,
    )

    dynamics = dynamics.reset_index()
    dynamics = dynamics.melt(
        id_vars="index", value_vars=[t for t in dynamics.columns if t != "index"]
    )
    dynamics = dynamics.rename(
        columns={
            "index": "year",
            "value": "Cum Num Documents",
            column: column.replace("_", " ").title(),
        }
    )

    fig = px.line(
        dynamics,
        x="year",
        y="Cum Num Documents",
        color=column.replace("_", " ").title(),
    )
    fig.update_layout(paper_bgcolor="white", plot_bgcolor="white")
    fig.update_xaxes(tickangle=270)
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
    )
    return fig
