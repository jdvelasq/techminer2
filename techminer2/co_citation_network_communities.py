"""
Co-citation Network / Communities
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> co_citation_network_communities(directory=directory).head()
cluster                                            CL_00  ...                                              CL_02
rn                                                        ...                                                   
0        Mollick E et al, 2014, J BUS VENTURING 01606:06  ...  Davis FD et al, 1989, MIS QUART MANAGE INF SYS...
1                  Lee I et al, 2018, BUS HORIZ 00213:38  ...  Venkatesh V et al, 2003, MIS QUART MANAGE INF ...
2              Gomber P et al, 2017, J BUS ECON 00181:21  ...       Venkatesh V et al, 2000, MANAGE SCI 09760:07
3        Schueffel P et al, 2016, J INNOV MANAG 00106:13  ...  Lee M-C et al, 2009, ELECT COMMER RES APPL 008...
4         Leong C et al, 2017, INT J INF MANAGE 00101:16  ...             Lin M et al, 2013, MANAGE SCI 00553:06
<BLANKLINE>
[5 rows x 3 columns]

"""

from .co_citation_matrix import co_citation_matrix
from .network import network
from .network_communities import network_communities


def co_citation_network_communities(
    top_n=50,
    clustering_method="louvain",
    directory="./",
):

    matrix = co_citation_matrix(
        top_n=top_n,
        directory=directory,
    )

    network_ = network(
        matrix,
        clustering_method=clustering_method,
    )

    return network_communities(network_)
