# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements


def nx_collect_degrees(nx_graph):
    """Collects the degrees of a graph as a sorted list."""

    degrees = []
    for node in nx_graph.nodes():
        degrees.append((node, nx_graph.nodes[node]["degree"]))
    degrees = sorted(degrees, key=lambda x: x[1], reverse=True)

    return degrees
