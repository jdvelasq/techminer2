import matplotlib.pyplot as plt

import networkx as nx


def betweenness_centrality(
    nodes,
    edges,
):

    # -----------------------------------------------------------
    nodes = nodes.copy()
    edges = edges.copy()

    # creates a networkx graph
    G = nx.Graph()

    # add nodes
    for _, row in nodes.iterrows():
        G.add_node(
            row["name"],
            size=row["size"],
        )

    # add edges
    for _, row in edges.iterrows():
        G.add_weighted_edges_from(
            [
                (row["source"], row["target"], row["value"]),
            ]
        )
    # -----------------------------------------------------------

    return nx.betweenness_centrality(G)


def closeness_centrality(
    nodes,
    edges,
):

    # -----------------------------------------------------------
    nodes = nodes.copy()
    edges = edges.copy()

    # creates a networkx graph
    G = nx.Graph()

    # add nodes
    for _, row in nodes.iterrows():
        G.add_node(
            row["name"],
            size=row["size"],
        )

    # add edges
    for _, row in edges.iterrows():
        G.add_weighted_edges_from(
            [
                (row["source"], row["target"], row["value"]),
            ]
        )
    # -----------------------------------------------------------

    return nx.closeness_centrality(G)


def node_degrees_plot(
    nodes,
    edges,
    figsize=(6, 6),
):
    # -----------------------------------------------------------
    nodes = nodes.copy()
    edges = edges.copy()

    # creates a networkx graph
    G = nx.Graph()

    # add nodes
    for _, row in nodes.iterrows():
        G.add_node(
            row["name"],
            size=row["size"],
        )

    # add edges
    for _, row in edges.iterrows():
        G.add_weighted_edges_from(
            [
                (row["source"], row["target"], row["value"]),
            ]
        )
    # -----------------------------------------------------------

    degree = [val for (_, val) in G.degree()]
    degree = sorted(degree, reverse=True)

    fig = plt.figure(figsize=figsize)
    ax = fig.subplots()

    ax.plot(degree, ".-k")
    ax.set_xlabel("Node")
    ax.set_ylabel("Degree")

    fig.set_tight_layout(True)

    return fig
