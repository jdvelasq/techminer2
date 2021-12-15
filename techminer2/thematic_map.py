"""
Thematic Map (conceptual structure)
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> coc_matrix = co_occurrence_matrix(
...     column='author_keywords', 
...     association="association",
...     min_occ=6,
...     directory=directory,
... )
>>> coc_matrix.head()
author_keywords                   fintech  ... regulatory sandbox
#d                                    139  ...                6  
#c                                   1285  ...               26  
author_keywords        #d  #c              ...                   
fintech                139 1285  0.007194  ...           0.007194
financial technologies 28  225   0.003597  ...           0.005952
financial inclusion    17  339   0.006348  ...           0.009804
blockchain             17  149   0.005501  ...           0.009804
innovation             13  249   0.005534  ...           0.000000
<BLANKLINE>
[5 rows x 23 columns]

>>> network = co_occurrence_network(
...     coc_matrix, 
...     clustering_method="louvain",
... )
>>> network_communities(network)
cluster                     CLUST_0  ...                           CLUST_2
rn                                   ...                                  
0               innovation 013:0249  ...                  fintech 139:1285
1                     bank 012:0185  ...               blockchain 017:0149
2               regulation 011:0084  ...     peer-to-peer lending 008:0073
3        financial service 011:0300  ...         cryptocurrencies 008:0036
4               technology 007:0192  ...                 covid-19 008:0036
5                     risk 007:0015  ...           perceived risk 006:0016
6                  finance 007:0052  ...  artificial intelligence 006:0030
7           business model 006:0174  ...                                  
<BLANKLINE>
[8 rows x 3 columns]

>>> file_name = "/workspaces/techminer2/sphinx/images/thematic_map_network.png"
>>> network_plot(network).savefig(file_name)

.. image:: images/thematic_map_network.png
    :width: 700px
    :align: center




"""
