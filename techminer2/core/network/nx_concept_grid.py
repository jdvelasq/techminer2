# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

import graphviz

from .nx_communities_summary import nx_communities_summary
from .nx_extract_communities_as_data_frame import (
    nx_extract_communities_as_data_frame,
)


def nx_concept_grid(
    nx_graph,
    conserve_counters,
    n_head,
    fontsize,
):
    summary = nx_communities_summary(
        #
        # FUNCTION PARAMS:
        nx_graph=nx_graph,
        conserve_counters=True,
    )

    data_frame = nx_extract_communities_as_data_frame(
        #
        # FUNCTION PARAMS:
        nx_graph=nx_graph,
        conserve_counters=True,
    )

    if n_head is not None:
        data_frame = data_frame.head(n_head)

    graph = graphviz.Digraph(
        "graph",
        node_attr={"shape": "record"},
    )

    for i_cluster, col in enumerate(data_frame.columns):
        text = data_frame[col].to_list()
        if conserve_counters is False:
            text = [" ".join(str(t).split(" ")[:-1]) for t in text]
        text = [t if t != "" else "." for t in text]
        text = "\\r".join(text) + "\\r"
        cluster_name = col + " (" + str(summary.loc[i_cluster, "Percentage"]) + " %)"
        graph.node(
            col,
            label=r"{" + cluster_name + "|" + text + r"}",
            fontsize=fontsize,
        )

    return graph
