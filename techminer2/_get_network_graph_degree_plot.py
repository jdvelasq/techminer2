"""Networkx Degree Plot"""

import pandas as pd
import plotly.express as px


def get_network_graph_degree_plot(graph):
    """Networkx Degree Plot"""

    degrees = []
    for _, adjacencies in enumerate(graph.adjacency()):
        degrees.append((adjacencies[0], len(adjacencies[1])))

    degree = pd.DataFrame(
        {
            "Name": [node for node, degree in degrees],
            "Degree": [degree for node, degree in degrees],
        }
    )

    degree = degree.sort_values(by="Degree", ascending=False)
    degree["Node"] = range(len(degrees))

    fig = px.line(
        degree,
        x="Node",
        y="Degree",
        markers=True,
        hover_data=["Name"],
    )
    fig.update_traces(
        marker=dict(size=8, line=dict(color="darkslategray", width=2)),
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
        # tickangle=270,
    )
    return fig
