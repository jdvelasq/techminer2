"""
Collaboration network (social structure)
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> coc_matrix = co_occurrence_matrix(
...     column='authors', 
...     association="equivalence",
...     min_occ=2,
...     directory=directory,
... )
>>> coc_matrix.head()
authors            Wojcik D Rabbani MR Hornuf L  ... Giudici P Iman N Zavolokina L
#d                        5          3        3  ...         2      2            2
#c                      19         39       110  ...       18     19           54 
authors     #d #c                                ...                              
Wojcik D    5  19       1.0        0.0      0.0  ...       0.0    0.0          0.0
Rabbani MR  3  39       0.0        1.0      0.0  ...       0.0    0.0          0.0
Hornuf L    3  110      0.0        0.0      1.0  ...       0.0    0.0          0.0
Xiang D     2  7        0.0        0.0      0.0  ...       0.0    0.0          0.0
Kauffman RJ 2  228      0.0        0.0      0.0  ...       0.0    0.0          0.0
<BLANKLINE>
[5 rows x 38 columns]


>>> network = co_occurrence_network(
...     coc_matrix, 
...     clustering_method="louvain",
... )
>>> network_communities(network)
cluster            CLUST_0  ...           CLUST_9
rn                          ...                  
0           Weber BW 2:228  ...  Bernards N 2:035
1           Parker C 2:228  ...                  
2        Kauffman RJ 2:228  ...                  
3           Gomber P 2:228  ...                  
<BLANKLINE>
[4 rows x 20 columns]

>>> file_name = "/workspaces/techminer-api/sphinx/images/collaboration_network.png"
>>> network_plot(network).savefig(file_name)

.. image:: images/collaboration_network.png
    :width: 600px
    :align: center




"""
