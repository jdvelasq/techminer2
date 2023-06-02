# flake8: noqa
"""
Cluster Items --- ChatGPT
===============================================================================

Extracts the communities from a networkx graph as a dataframe.


Example:
-------------------------------------------------------------------------------

>>> root_dir = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> co_occ_matrix = vantagepoint.analyze.co_occ_matrix(
...    columns='author_keywords',
...    col_occ_range=(2, None),
...    root_dir=root_dir,
... )
>>> graph = vantagepoint.analyze.cluster_field(
...    co_occ_matrix,
...    community_clustering='louvain',
... )
>>> vantagepoint.analyze.cluster_items(graph)
                            CL_00  ...                           CL_03
0                  regtech 28:329  ...  artificial intelligence 04:023
1               compliance 07:030  ...    anti-money laundering 03:021
2               blockchain 03:005  ...              charitytech 02:017
3          smart contracts 02:022  ...              english law 02:017
4           accountability 02:014  ...                                
5  data protection officer 02:014  ...                                
6                     gdpr 02:014  ...                                
7               technology 02:010  ...                                
<BLANKLINE>
[8 rows x 4 columns]


"""

import pandas as pd


def cluster_items(graph):
    """Gets communities from a networkx graph as a dataframe."""

    def extract_communities(graph):
        """Gets communities from a networkx graph as a dictionary."""

        communities = {}

        for node, data in graph.nodes(data=True):
            text = f"CL_{data['group'] :02d}"
            if text not in communities:
                communities[text] = []
            communities[text].append(node)

        return communities

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
    communities = extract_communities(graph)
    communities = sort_community_members(communities)
    communities = pd.DataFrame.from_dict(communities, orient="index").T
    communities = communities.fillna("")
    communities = communities.sort_index(axis=1)

    return communities
