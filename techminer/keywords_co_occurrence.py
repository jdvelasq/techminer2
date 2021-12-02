"""
Keywords co-occurrence (conceptual structure)
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> coc_matrix = co_occurrence_matrix(column='author_keywords', min_occ=6,directory=directory)
>>> coc_matrix.head()
author_keywords                 fintech  ... regulatory sandbox
#d                                  139  ...                6  
#c                                 1285  ...               26  
author_keywords        #d  #c            ...                   
fintech                139 1285     139  ...                  6
financial technologies 28  225       14  ...                  1
financial inclusion    17  339       15  ...                  1
blockchain             17  149       13  ...                  1
innovation             13  249       10  ...                  0
<BLANKLINE>
[5 rows x 23 columns]

>>> network = co_occurrence_network(coc_matrix)
>>> network_communities(network)
cluster                           CLUST_0  ...                          CLUST_2
rn                                         ...                                 
0                        fintech 139:1285  ...  financial technologies 028:0225
1            financial inclusion 017:0339  ...    financial innovation 008:0044
2                     blockchain 017:0149  ...     financial stability 006:0022
3                     regulation 011:0084  ...               ecosystem 006:0016
4           peer-to-peer lending 008:0073  ...                   china 006:0018
5               cryptocurrencies 008:0036  ...                                 
6                   crowdfunding 008:0116  ...                                 
7                       covid-19 008:0036  ...                                 
8                           risk 007:0015  ...                                 
9                        finance 007:0052  ...                                 
10            regulatory sandbox 006:0026  ...                                 
11                perceived risk 006:0016  ...                                 
12       artificial intelligence 006:0030  ...                                 
<BLANKLINE>
[13 rows x 3 columns]

>>> file_name = "/workspaces/techminer-api/sphinx/images/keyword_co_occurrence_network.png"
>>> network_plot(network).savefig(file_name)

.. image:: images/keyword_co_occurrence_network.png
    :width: 600px
    :align: center




"""
