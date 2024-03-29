# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements


import pandas as pd

from .nx_extract_communities_as_dict import nx_extract_communities_as_dict


def nx_extract_communities_as_data_frame(nx_graph, conserve_counters):
    """Gets communities from a networkx graph as a data frame."""

    communities = nx_extract_communities_as_dict(nx_graph, conserve_counters)
    communities = pd.DataFrame.from_dict(communities, orient="index").T
    communities = communities.fillna("")
    communities = communities.sort_index(axis=1)

    return communities
