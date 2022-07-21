"""
Network Communities
===============================================================================


>>> from techminer2 import *
>>> directory = "data/regtech/"
>>> matrix_list = co_occ_matrix_list(
...    column='author_keywords',
...    min_occ=3,
...    directory=directory,
... )

>>> from techminer2.co_occ_network import co_occ_network
>>> graph = co_occ_network(matrix_list)
>>> from techminer2.network_community_detection import network_community_detection
>>> graph = network_community_detection(graph, method='louvain')

>>> from techminer2.network_communities import network_communities
>>> network_communities(graph).head()
                         CL_00  ...                CL_06
0               regtech 70:462  ...  semantic web 03:002
1               fintech 42:406  ...                     
2            blockchain 18:109  ...                     
3            compliance 12:020  ...                     
4  financial regulation 08:091  ...                     
<BLANKLINE>
[5 rows x 7 columns]


"""
import pandas as pd


def get_network_graph_communities(graph):
    """Network Communities"""

    members = {}
    for node, data in graph.nodes(data=True):
        text = f"CL_{data['group'] :02d}"
        if text not in members:
            members[text] = []
        members[text].append(node)

    for key, items in members.items():
        pdf = pd.DataFrame({"members": items})
        pdf = pdf.assign(OCC=pdf.members.map(lambda x: x.split()[-1].split(":")[0]))
        pdf = pdf.assign(gc=pdf.members.map(lambda x: x.split()[-1].split(":")[1]))
        pdf = pdf.sort_values(
            by=["OCC", "gc", "members"], ascending=[False, False, True]
        )
        members[key] = pdf.members.tolist()

    df = pd.DataFrame.from_dict(members, orient="index").T
    df = df.fillna("")
    df = df.sort_index(axis=1)

    return df
