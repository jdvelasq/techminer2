# flake8: noqa
"""
(NEW) Network Communities
===============================================================================

Extracts the community (cluster) members from a networkx graph as a dataframe.


Example:
-------------------------------------------------------------------------------

>>> root_dir = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> co_occ_matrix = vantagepoint.analyze.co_occurrence_matrix(
...    columns='author_keywords',
...    col_occ_range=(2, None),
...    root_dir=root_dir,
... )
>>> graph = vantagepoint.analyze.network_clustering(
...    co_occ_matrix,
...    community_clustering='louvain',
... )
>>> vantagepoint.analyze.cluster_members(graph)
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

from ...network_utils import extract_communities_from_graph


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
    communities = extract_communities_from_graph(graph, conserve_counters=True)
    communities = sort_community_members(communities)
    communities = pd.DataFrame.from_dict(communities, orient="index").T
    communities = communities.fillna("")
    communities = communities.sort_index(axis=1)

    return communities