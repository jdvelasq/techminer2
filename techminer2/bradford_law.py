"""
Bradford's Law
===============================================================================


>>> from techminer2 import *
>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bradford_law.html"

>>> bradford_law(directory=directory).write_html(file_name)

.. raw:: html

    <iframe src="_static/bradford_law.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> bradford_law(
...     directory=directory,
...     plot=False,
... ).head(5)
                     no  OCC  cum_OCC  global_citations  zone
source_abbr                                                  
CEUR WORKSHOP PROC    1    5        5                 2     1
STUD COMPUT INTELL    2    4        9                 3     1
JUSLETTER IT          3    4       13                 0     1
EUR BUS ORG LAW REV   4    3       16                65     1
J BANK REGUL          5    3       19                29     1


"""
import plotly.express as px

from .source_clustering import source_clustering


def bradford_law(
    directory="./",
    database="documents",
    plot=True,
):

    indicators = source_clustering(
        directory=directory,
        database=database,
    )

    if plot is False:
        return indicators

    fig = px.line(
        indicators,
        x="no",
        y="OCC",
        title="Source Clustering through Bradford's Law",
        markers=True,
        hover_data=[indicators.index, "OCC"],
        log_x=True,
    )
    fig.update_traces(
        marker=dict(size=5, line=dict(color="darkslategray", width=1)),
        marker_color="rgb(171,171,171)",
        line=dict(color="darkslategray"),
    )
    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        xaxis_title=None,
        xaxis_showticklabels=False,
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

    core = len(indicators.loc[indicators.zone == 1])

    fig.add_shape(
        type="rect",
        x0=1,
        y0=0,
        x1=core,
        y1=indicators.OCC.max(),
        line=dict(
            color="lightgrey",
            width=2,
        ),
        fillcolor="lightgrey",
        opacity=0.2,
    )

    fig.data = fig.data[::-1]

    return fig
