"""
Network Communities
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer2/sphinx/images/co_occurrence_network_map.png"
>>> coc_matrix = co_occurrence_matrix(
...     column='author_keywords', 
...     min_occ=7, 
...     directory=directory,
... )
>>> from techminer2.network_api.network import network
>>> network_ = network(coc_matrix)
>>> from techminer2.network_api.network_communities import network_communities
>>> network_communities(network_).head()
cluster                          CLUST_0                     CLUST_1
rn                                                                  
0                       fintech 139:1285         innovating 013:0249
1        financial technologies 028:0225               bank 012:0185
2           financial inclusion 017:0339  financial service 011:0300
3                   block-chain 017:0149         technology 007:0192
4                    regulating 011:0084           start-up 007:0141

"""


def network_communities(network):
    communities = network["communities"].copy()
    return communities
