"""
Annual Scientific Production (ok!)
===============================================================================

See :doc:`annual indicators <annual_indicators>` to obtain a `pandas.Dataframe` 
with the data.

>>> from techminer2.bibliometrix import *
>>> directory = "data/"
>>> file_name = "sphinx/_static/annual_scientific_production.html"

>>> annual_scientific_production(directory).write_html(file_name)

.. raw:: html

    <iframe src="_static/annual_scientific_production.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .annual_indicators_plot import annual_indicators_plot


def annual_scientific_production(directory="./"):
    return annual_indicators_plot(
        column="num_documents",
        title="Annual Scientific Production",
        directory=directory,
    )


# import plotly.express as px

# from .annual_indicators import annual_indicators

# def annual_scientific_production(directory="./"):
#     indicators = annual_indicators(directory)
#     fig = px.line(
#         x=indicators.index,
#         y=indicators.num_documents,
#         title="Annual Scientific Production",
#         markers=True,
#         text=indicators.num_documents,
#         labels={"x": "Year", "y": "Number of publications"},
#     )
#     fig.update_traces(marker=dict(size=12))
#     fig.update_traces(textposition="bottom right")
#     fig.update_traces(line=dict(color="black"))
#     fig.update_xaxes(tickangle=270)
#     fig.update_layout(paper_bgcolor="white", plot_bgcolor="white")
#     fig.update_xaxes(linecolor="gray", gridcolor="lightgray")
#     fig.update_yaxes(linecolor="gray", gridcolor="lightgray")
#     fig.update_yaxes(showticklabels=False)
#     return fig
