"""Extracts articles per cluster from graph."""


def extract_articles_per_cluster(graph):
    """Extracts records per cluster of graph."""

    articles_per_cluster = {}

    for node in graph.nodes():
        group = graph.nodes[node]["group"]
        cluster = f"CL_{group:02d}"
        if cluster not in articles_per_cluster:
            articles_per_cluster[cluster] = []
        node = " ".join(node.split(" ")[:-1])
        articles_per_cluster[cluster].append(node)

    return articles_per_cluster
