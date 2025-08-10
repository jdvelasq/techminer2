# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements


import pandas as pd  # type: ignore

from ..params_mixin import Params
from .create_clusters_to_terms_mapping import \
    internal__create_clusters_to_terms_mapping


def internal__extract_communities_to_frame(
    params,
    nx_graph,
):
    """Gets communities from a networkx graph as a data frame."""

    def f(x):
        x = [(w.split(" ")[-1], w) for w in x]
        mapping = {}
        for w in x:
            if w[0] not in mapping:
                mapping[w[0]] = []
            mapping[w[0]].append(w[1])
        mapping = {k: sorted(v) for k, v in mapping.items()}
        x = [v for k in sorted(mapping.keys(), reverse=True) for v in mapping[k]]
        return x

    local_params = Params(**params.__dict__).update(term_counters=True)
    communities = internal__create_clusters_to_terms_mapping(local_params, nx_graph)
    communities = {key: f(value) for key, value in communities.items()}
    if params.term_counters is False:
        communities = {
            key: [" ".join(v.split(" ")[:-1]) for v in value]
            for key, value in communities.items()
        }
    communities = pd.DataFrame.from_dict(communities, orient="index").T
    communities = communities.fillna("")
    communities = communities.sort_index(axis=1)

    return communities
