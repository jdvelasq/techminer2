"""
Column production by year
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/_static/column_production_by_year.html"


>>> column_production_by_year(
...     'authors',
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/column_production_by_year.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
import plotly.express as px

from .column_indicators import column_indicators
from .column_indicators_by_year import column_indicators_by_year


def column_production_by_year(
    column,
    top_n=10,
    directory="./",
    title=None,
):

    indicators_by_year = column_indicators_by_year(column=column, directory=directory)
    indicators_by_year = indicators_by_year.reset_index()
    selected_terms = column_indicators(column=column, directory=directory).head(top_n)
    terms = selected_terms.index.to_list()

    indicators_by_year = indicators_by_year[
        indicators_by_year[column].map(lambda x: x in terms)
    ]

    indicators_by_year = indicators_by_year.rename(
        columns={
            col: col.replace("_", " ").title() for col in indicators_by_year.columns
        }
    )
    indicators_by_year = indicators_by_year.rename(columns={"Pub Year": "Year"})

    fig = px.scatter(
        indicators_by_year,
        x="Year",
        y=column.replace("_", " ").title(),
        size="Num Documents",
        color_discrete_sequence=["darkslategray"],
        hover_data=["Global Citations", "Local Citations"],
        title=title,
    )
    fig.update_layout(paper_bgcolor="white", plot_bgcolor="white")
    fig.update_yaxes(
        linecolor="white",
        linewidth=1,
        autorange="reversed",
        gridcolor="gray",
        griddash="dot",
    )
    fig.update_xaxes(
        linecolor="white",
        linewidth=1,
        gridcolor="gray",
        griddash="dot",
    )
    fig.update_xaxes(tickangle=270)
    fig.update_layout(xaxis_type="category")

    return fig
