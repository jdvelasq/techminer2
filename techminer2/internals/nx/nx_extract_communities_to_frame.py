# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements


import pandas as pd  # type: ignore

from .nx_clusters_to_terms_mapping import nx_clusters_to_terms_mapping


def nx_extract_communities_to_frame(
    nx_graph,
    conserve_counters,
):
    """Gets communities from a networkx graph as a data frame."""

    communities = nx_clusters_to_terms_mapping(nx_graph, conserve_counters)
    communities = pd.DataFrame.from_dict(communities, orient="index").T
    communities = communities.fillna("")
    communities = communities.sort_index(axis=1)

    return communities
