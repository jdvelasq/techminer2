# flake8: noqa
"""
Network Communities
===============================================================================

Extracts the community (cluster) members from a networkx graph as a dataframe.



>>> root_dir = "data/regtech/"

>>> import techminer2plus
>>> cooc_matrix = techminer2plus.analyze.matrix.co_occurrence_matrix(
...    columns='author_keywords',
...    col_occ_range=(2, None),
...    root_dir=root_dir,
... )
>>> graph = techminer2plus.analyze.network.cluster_network(
...    cooc_matrix,
...    algorithm_or_estimator='louvain',
... )
>>> techminer2plus.analyze.network.network_communities(graph)
                            CL_00  ...                           CL_03
0                  REGTECH 28:329  ...    ANTI_MONEY_LAUNDERING 05:034
1               COMPLIANCE 07:030  ...  ARTIFICIAL_INTELLIGENCE 04:023
2               BLOCKCHAIN 03:005  ...              CHARITYTECH 02:017
3          SMART_CONTRACTS 02:022  ...              ENGLISH_LAW 02:017
4           ACCOUNTABILITY 02:014  ...                                
5  DATA_PROTECTION_OFFICER 02:014  ...                                
6                     GDPR 02:014  ...                                
7               TECHNOLOGY 02:010  ...                                
<BLANKLINE>
[8 rows x 4 columns]




"""

import pandas as pd

from ...network import nx_extract_communities


def network_communities(graph):
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
    communities = nx_extract_communities(graph, conserve_counters=True)
    communities = sort_community_members(communities)
    communities = pd.DataFrame.from_dict(communities, orient="index").T
    communities = communities.fillna("")
    communities = communities.sort_index(axis=1)

    return communities
