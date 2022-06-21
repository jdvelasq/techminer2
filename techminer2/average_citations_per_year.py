"""
Average Citations per Year (!)
===============================================================================


>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/images/average_citations_per_year.png"
>>> average_citations_per_year(directory=directory).write_image(file_name)

.. image:: images/average_citations_per_year.png
    :width: 700px
    :align: center

>>> annual_indicators(directory)[
...     [
...         'num_documents',
...         'mean_global_citations',
...         'mean_global_citations',
...         'citable_years',
...     ]
... ].head()
          num_documents  ...  citable_years
pub_year                 ...               
2016                  5  ...              6
2017                 10  ...              5
2018                 34  ...              4
2019                 38  ...              3
2020                 62  ...              2
<BLANKLINE>
[5 rows x 4 columns]

"""
import plotly.express as px

from .annual_indicators import annual_indicators


def average_citations_per_year(directory="./"):

    indicators = annual_indicators(directory)
    fig = px.line(
        x=indicators.index,
        y=indicators.mean_global_citations,
        title="Average citations per year",
        markers=True,
        text=indicators.mean_global_citations.round(2),
        labels={"x": "Year", "y": "Citations"},
    )
    fig.update_traces(marker=dict(size=12))
    fig.update_traces(textposition="top right")
    fig.update_traces(line=dict(color="black"))
    fig.update_xaxes(tickangle=270)
    fig.update_layout(paper_bgcolor="white", plot_bgcolor="white")
    fig.update_xaxes(linecolor="gray", gridcolor="lightgray")
    fig.update_yaxes(linecolor="gray", gridcolor="lightgray")
    fig.update_yaxes(showticklabels=False)
    return fig
