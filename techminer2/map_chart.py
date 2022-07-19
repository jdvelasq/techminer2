"""
Map Chart
===============================================================================

>>> import pandas as pd
>>> from sklearn.decomposition import TruncatedSVD
>>> from techminer2 import *
>>> directory = "data/regtech/"

>>> file_name = "sphinx/_static/map_chart.html"

>>> coc_matrix = co_occ_matrix(
...     column='author_keywords',
...     top_n=20,
...     directory=directory,
... )

>>> from techminer2.association_index import association_index
>>> coc_matrix = association_index(coc_matrix, "salton")

>>> decomposed_matrix = TruncatedSVD(
...     n_components=2,
...     random_state=0,
... ).fit_transform(coc_matrix)

>>> decomposed_matrix = pd.DataFrame(
...     decomposed_matrix,
...     columns=['dim0', 'dim1'],
...     index=coc_matrix.index,
... )

>>> map_chart(
...     decomposed_matrix, 
...     dim_x=0,
...     dim_y=1,
...     delta=0.4,
... ).write_html(file_name)


.. raw:: html

    <iframe src="_static/map_chart.html" height="800px" width="100%" frameBorder="0"></iframe>


"""
import plotly.graph_objects as go


def map_chart(
    dataframe,
    dim_x=0,
    dim_y=1,
    delta=1.0,
):
    """Makes a map chart."""

    dataframe = dataframe.copy()

    node_x = dataframe[f"dim{dim_x}"]
    node_y = dataframe[f"dim{dim_y}"]

    x_mean = node_x.mean()
    y_mean = node_y.mean()
    textposition = []
    for x_pos, y_pos in zip(node_x, node_y):
        if x_pos >= x_mean and y_pos >= y_mean:
            textposition.append("top right")
        if x_pos <= x_mean and y_pos >= y_mean:
            textposition.append("top left")
        if x_pos <= x_mean and y_pos <= y_mean:
            textposition.append("bottom left")
        if x_pos >= x_mean and y_pos <= y_mean:
            textposition.append("bottom right")

    fig = go.Figure(
        layout=go.Layout(
            xaxis={"mirror": "allticks"},
            yaxis={"mirror": "allticks"},
        )
    )
    fig.add_trace(
        go.Scatter(
            x=node_x,
            y=node_y,
            mode="markers+text",
            textposition=textposition,
            text=dataframe.index.tolist(),
        )
    )
    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        margin=dict(l=1, r=1, t=1, b=1),
    )
    fig.update_traces(
        marker=dict(
            line=dict(color="darkslategray", width=2),
        ),
        marker_color="lightgrey",
    )

    x_max = node_x.max()
    x_min = node_x.min()

    fig.update_xaxes(
        linecolor="white",
        linewidth=1,
        gridcolor="lightgray",
        griddash="dot",
        ticks="outside",
        tickwidth=2,
        ticklen=10,
        minor=dict(ticklen=5),
        range=[x_min - delta, x_max + delta],
    )
    fig.update_yaxes(
        linecolor="white",
        linewidth=1,
        gridcolor="lightgray",
        griddash="dot",
        ticks="outside",
        tickwidth=2,
        ticklen=10,
        minor=dict(ticklen=5),
    )
    return fig
