"""
Network Degree Plot
===============================================================================


# >>> from techminer2 import *
# >>> directory = "data/regtech/"
# >>> matrix_list = co_occ_matrix_list(
# ...    column='author_keywords',
# ...    min_occ=3,
# ...    directory=directory,
# ... )

# >>> from techminer2.co_occ_network import co_occ_network
# >>> graph = co_occ_network(matrix_list)
# >>> from techminer2.network_community_detection import network_community_detection
# >>> graph = network_community_detection(graph, method='louvain')

# >>> file_name = "sphinx/_static/network_degree_plot.html"
# >>> from techminer2.network_degree_plot import network_degree_plot
# >>> network_degree_plot(graph).write_html(file_name)

# .. raw:: html

#     <iframe src="_static/network_degree_plot.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
import pandas as pd
import plotly.express as px


def network_degree_plot(graph):

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
