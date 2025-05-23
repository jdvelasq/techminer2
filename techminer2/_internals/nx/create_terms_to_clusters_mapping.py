# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements


def internal__create_terms_to_clusters_mapping(
    params,
    nx_graph,
):
    """Creates a dictionary with terms as keys and clusters as values."""

    mapping = {}
    for node, data in nx_graph.nodes(data=True):
        cluster = data["group"]
        if params.term_counters is False:
            node = " ".join(node.split(" ")[:-1])
        mapping[node] = cluster

    return mapping
