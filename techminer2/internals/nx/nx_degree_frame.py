# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Network Deegre Plot

"""
import pandas as pd  # type: ignore

from .nx_assign_degree_to_nodes import nx_assign_degree_to_nodes


def nx_degree_frame(
    #
    # NX GRAPH:
    nx_graph,
):
    """Compute and plots the degree of a co-occurrence matrix."""

    def collect_degrees(graph):
        """Collects the degrees of a graph as a sorted list."""

        degrees = []
        for node in graph.nodes():
            degrees.append((node, graph.nodes[node]["degree"]))
        degrees = sorted(degrees, key=lambda x: x[1], reverse=True)

        return degrees

    def to_dataframe(degrees):
        """Converts a list of degrees to a dataframe."""

        data = pd.DataFrame(degrees, columns=["Name", "Degree"])
        data["Node"] = data.index

        return data

    #
    #
    # MAIN CODE:
    #
    #

    nx_graph = nx_assign_degree_to_nodes(nx_graph)
    degrees = collect_degrees(nx_graph)
    dataframe = to_dataframe(degrees)
    dataframe = dataframe[["Node", "Name", "Degree"]]

    return dataframe
