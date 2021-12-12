"""
Co-citation Network / Communities
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> co_citation_communities(directory=directory).head()
cluster             CLUST_0             CLUST_1             CLUST_2
rn                                                                 
0        2014-0003 01606:06  1989-0000 25830:14  2016-0044 00172:07
1        2013-0009 00553:06  2003-0002 16860:09  2017-0046 00146:15
2        2018-0020 00220:31  2000-0000 09760:07  2018-0054 00126:14
3        2018-0022 00213:38  2009-0013 00876:09  2018-0123 00067:08
4        2017-0038 00181:21  2013-0015 00452:06  2018-0134 00062:08

"""

from .co_citation_matrix import co_citation_matrix
from .network import network
from .network_communities import network_communities


def co_citation_communities(
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
