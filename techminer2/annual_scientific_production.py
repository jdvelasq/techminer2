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


# def _yaxis_format(y_value, y_position):
#     y_formated = "{:1.0f}".format(y_value)
#     return y_formated


# def _annual_scientific_production(
#     directory=None,
#     figsize=(6, 6),
#     color="k",
# ):

#     if directory is None:
#         directory = "/workspaces/techminer-api/tests/data/"

#     production = annual_indicators(directory)["num_documents"]
#     production = production.astype(int)

#     fig = plt.Figure(figsize=figsize)
#     ax = fig.subplots()

#     ax.plot(
#         production.index.astype(str),
#         production.values,
#         "o-",
#         markersize=8,
#         color=color,
#         alpha=1.0,
#     )

#     ax.set_title(
#         "Annual scientific production", fontsize=12, color="dimgray", loc="left"
#     )
#     ax.set_ylabel("Number of publications", color="dimgray")
#     ax.set_xlabel("Year", color="dimgray")
#     ax.set_xticklabels(
#         production.index.astype(str),
#         rotation=90,
#         horizontalalignment="center",
#         fontsize=7,
#         color="dimgray",
#     )
#     ax.set_yticklabels(
#         ax.get_yticks(),
#         fontsize=7,
#         color="dimgray",
#     )

#     ax.yaxis.set_major_locator(MaxNLocator(integer=True))

#     ax.yaxis.set_major_formatter(
#         tick.FuncFormatter(_yaxis_format),
#     )

#     ax.spines["left"].set_color("dimgray")
#     ax.spines["bottom"].set_color("dimgray")
#     ax.spines["top"].set_visible(False)
#     ax.spines["right"].set_visible(False)
#     ax.grid(alpha=0.5)
#     return fig
