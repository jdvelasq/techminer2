# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements


import pandas as pd  # type: ignore

from .create_clusters_to_terms_mapping import \
    internal__create_clusters_to_terms_mapping


def internal__summarize_communities(
    params,
    nx_graph,
):
    """Gets communities from a networkx graph as a data frame."""

    communities_dict = internal__create_clusters_to_terms_mapping(
        params=params, nx_graph=nx_graph
    )
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
