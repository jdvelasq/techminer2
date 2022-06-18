"""
Network Indicators
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/images/co_occurrence_network_map.png"
>>> coc_matrix = co_occurrence_matrix(
...     column='author_keywords', 
...     min_occ=7, 
...     directory=directory,
... )
>>> from techminer2.network_api.network import network
>>> network_ = network(coc_matrix)
>>> from techminer2.network_api.network_indicators import network_indicators
>>> network_indicators(network_).head()
                  num_documents  global_citations  ...  closeness  pagerank
node                                               ...                     
bank                         12               185  ...   0.695652  0.050294
block-chain                  17               149  ...   0.695652  0.064299
covid-19                      8                36  ...   0.533333  0.020194
crowdfunding                  8               116  ...   0.615385  0.030571
cryptocurrencies              8                36  ...   0.571429  0.039274
<BLANKLINE>
[5 rows x 6 columns]

"""


def network_indicators(network):
    indicators = network["indicators"].copy()
    indicators = indicators.set_index("node")
    return indicators
