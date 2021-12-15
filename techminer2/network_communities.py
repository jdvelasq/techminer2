"""
Network Communities
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/co_occurrence_network_map.png"
>>> coc_matrix = co_occurrence_matrix(column='author_keywords', min_occ=7,directory=directory)
>>> network = co_occurrence_network(coc_matrix)
>>> network_communities(network)
cluster                          CLUST_0  ...                    CLUST_2
rn                                        ...                           
0                       fintech 139:1285  ...        blockchain 017:0149
1        financial technologies 028:0225  ...  cryptocurrencies 008:0036
2           financial inclusion 017:0339  ...                           
3                    regulation 011:0084  ...                           
4          peer-to-peer lending 008:0073  ...                           
5          financial innovation 008:0044  ...                           
6                  crowdfunding 008:0116  ...                           
7                      covid-19 008:0036  ...                           
8                          risk 007:0015  ...                           
9                       finance 007:0052  ...                           
<BLANKLINE>
[10 rows x 3 columns]

"""


def network_communities(network):
    communities = network["communities"].copy()
    return communities
