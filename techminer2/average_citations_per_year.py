"""
Average Citations per Year
===============================================================================

See :doc:`annual indicators <annual_indicators>` to obtain a `pandas.Dataframe` 
with the data.

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/_static/average_citations_per_year.html"

>>> average_citations_per_year(directory=directory).write_html(file_name)

.. raw:: html

    <iframe src="_static/average_citations_per_year.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .annual_indicators_plot import annual_indicators_plot


def average_citations_per_year(directory="./"):
    return annual_indicators_plot(
        column="mean_global_citations",
        title="Average citations per year",
        directory=directory,
    )


# import plotly.express as px

# from .annual_indicators import annual_indicators


# def average_citations_per_year(directory="./"):

#     indicators = annual_indicators(directory)
#     fig = px.line(
#         x=indicators.index,
#         y=indicators.mean_global_citations,
#         title="Average citations per year",
#         markers=True,
#         text=indicators.mean_global_citations.round(2),
#         labels={"x": "Year", "y": "Citations"},
#     )
#     fig.update_traces(marker=dict(size=12))
#     fig.update_traces(textposition="top right")
#     fig.update_traces(line=dict(color="black"))
#     fig.update_xaxes(tickangle=270)
#     fig.update_layout(paper_bgcolor="white", plot_bgcolor="white")
#     fig.update_xaxes(linecolor="gray", gridcolor="lightgray")
#     fig.update_yaxes(linecolor="gray", gridcolor="lightgray")
#     fig.update_yaxes(showticklabels=False)
#     return fig
