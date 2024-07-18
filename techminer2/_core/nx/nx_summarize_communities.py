# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements


import pandas as pd

from .nx_clusters_to_terms_mapping import nx_clusters_to_terms_mapping


def nx_summarize_communities(
    nx_graph,
    conserve_counters,
):
    """Gets communities from a networkx graph as a data frame."""

    communities_dict = nx_clusters_to_terms_mapping(nx_graph, retain_counters=conserve_counters)
    communities_len = {}
    communities_perc = {}

    total = float(sum(len(communities_dict[key]) for key in communities_dict))

    for key, values in communities_dict.items():
        communities_len[key] = len(values)
        communities_perc[key] = round(communities_len[key] / total * 100, 1)
        communities_dict[key] = "; ".join(values)

    summary = pd.DataFrame(
        {
            "Cluster": list(communities_dict.keys()),
            "Num Terms": communities_len.values(),
            "Percentage": communities_perc.values(),
            "Terms": communities_dict.values(),
        }
    )

    summary = summary.sort_values("Cluster", ascending=True)
    summary = summary.reset_index(drop=True)

    return summary
