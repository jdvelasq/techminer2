# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements


def internal__clusters_to_terms_mapping(
    nx_graph,
    retain_counters,
):
    """Gets communities from a networkx graph as a dictionary."""

    mapping = {}

    for node, data in nx_graph.nodes(data=True):
        cluster = data["group"]
        if cluster not in mapping:
            mapping[cluster] = []
        if retain_counters is False:
            node = " ".join(node.split(" ")[:-1])
        mapping[cluster].append(node)

    return mapping
