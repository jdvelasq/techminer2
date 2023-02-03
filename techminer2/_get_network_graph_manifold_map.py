"""MDS/TSNE Map from a network graph."""

import pandas as pd
import plotly.express as px

from ._bubble_map import bubble_map


def get_network_graph_manifold_map(
    matrix_list,
    graph,
    manifold_method,
):
    """Bults a network map from a network graph."""

    matrix = matrix_list.pivot(index="row", columns="column", values="OCC")
    matrix = matrix.fillna(0)

    # manifold_method = MDS(n_components=2)
    transformed_matrix = manifold_method.fit_transform(matrix)

    nodes = matrix.index.to_list()
    # node_names = [" ".join(name.split()[:-1]) for name in nodes]
    node_occ = [int(name.split()[-1].split(":")[0]) for name in nodes]
    node_global_citations = [int(name.split()[-1].split(":")[-1]) for name in nodes]

    manifold_data = pd.DataFrame(
        {
            "node": nodes,
            "OCC": node_occ,
            "global_citations": node_global_citations,
        }
    )

    manifold_data["Dim-0"] = transformed_matrix[:, 0]
    manifold_data["Dim-1"] = transformed_matrix[:, 1]

    node2cluster = {node: graph.nodes[node]["group"] for node in graph.nodes()}
    manifold_data["cluster"] = manifold_data.node.map(node2cluster)
    name2degree = dict(graph.degree())
    manifold_data["degree"] = manifold_data.node.map(name2degree)

    manifold_data["color"] = manifold_data["cluster"].map(
        lambda x: px.colors.qualitative.Dark24[x]
        if x < 24
        else px.colors.qualitative.Light24[x]
    )

    fig = bubble_map(
        node_x=manifold_data["Dim-0"],
        node_y=manifold_data["Dim-1"],
        node_text=manifold_data["node"],
        node_color=manifold_data["color"],
        node_size=manifold_data["degree"],
    )

    return fig
