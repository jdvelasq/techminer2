# flake8: noqa
# pylint: disable=line-too-long
"""
Network Communities
===============================================================================

Extracts the community (cluster) members from a networkx graph as a dataframe.



* Preparation

>>> import techminer2 as tm2
>>> root_dir = "data/regtech/"

* Object oriented interface

>>> (
...     tm2p.records(root_dir=root_dir)
...     .co_occurrence_matrix(
...         columns='author_keywords',
...         col_top_n=20,
...     )
...     .network_create(
...         algorithm_or_estimator="louvain"
...     )
...     .network_communities()
... )
                            CL_00  ...                           CL_03
0                  REGTECH 28:329  ...    ANTI_MONEY_LAUNDERING 05:034
1               COMPLIANCE 07:030  ...  ARTIFICIAL_INTELLIGENCE 04:023
2               BLOCKCHAIN 03:005  ...              CHARITYTECH 02:017
3          SMART_CONTRACTS 02:022  ...              ENGLISH_LAW 02:017
4           ACCOUNTABILITY 02:014  ...                                
5  DATA_PROTECTION_OFFICER 02:014  ...                                
<BLANKLINE>
[6 rows x 4 columns]


* Functional interface

>>> cooc_matrix = tm2p.co_occurrence_matrix(
...    columns='author_keywords',
...    col_top_n=20,
...    root_dir=root_dir,
... )
>>> network = tm2p.network_create(
...     cooc_matrix,
...     algorithm_or_estimator='louvain',
... )
>>> network_communities(network)
                            CL_00  ...                           CL_03
0                  REGTECH 28:329  ...    ANTI_MONEY_LAUNDERING 05:034
1               COMPLIANCE 07:030  ...  ARTIFICIAL_INTELLIGENCE 04:023
2               BLOCKCHAIN 03:005  ...              CHARITYTECH 02:017
3          SMART_CONTRACTS 02:022  ...              ENGLISH_LAW 02:017
4           ACCOUNTABILITY 02:014  ...                                
5  DATA_PROTECTION_OFFICER 02:014  ...                                
<BLANKLINE>
[6 rows x 4 columns]


"""

import pandas as pd

from .._network_lib import nx_extract_communities


def network_communities(network):
    """Gets communities from a networkx graph as a dataframe."""

    def sort_community_members(communities):
        """Sorts community members in a dictionary."""

        for key, items in communities.items():
            pdf = pd.DataFrame({"members": items})
            pdf = pdf.assign(
                OCC=pdf.members.map(lambda x: x.split()[-1].split(":")[0])
            )
            pdf = pdf.assign(
                gc=pdf.members.map(lambda x: x.split()[-1].split(":")[1])
            )
            pdf = pdf.sort_values(
                by=["OCC", "gc", "members"], ascending=[False, False, True]
            )
            communities[key] = pdf.members.tolist()

        return communities

    #
    # main:
    #
    nx_graph = network.nx_graph
    communities = nx_extract_communities(nx_graph, conserve_counters=True)
    communities = sort_community_members(communities)
    communities = pd.DataFrame.from_dict(communities, orient="index").T
    communities = communities.fillna("")
    communities = communities.sort_index(axis=1)

    return communities
