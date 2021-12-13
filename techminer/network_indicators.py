"""
Network Indicators
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/co_occurrence_network_map.png"
>>> coc_matrix = co_occurrence_matrix(column='author_keywords', min_occ=7,directory=directory)
>>> network = co_occurrence_network(coc_matrix)
>>> network_indicators(network)
                        num_documents  global_citations  ...  closeness  pagerank
node                                                     ...                     
bank                               12               185  ...   0.681818  0.051579
blockchain                         17               149  ...   0.714286  0.068868
covid-19                            8                36  ...   0.535714  0.021563
crowdfunding                        8               116  ...   0.625000  0.032711
cryptocurrencies                    8                36  ...   0.576923  0.042013
finance                             7                52  ...   0.750000  0.051353
financial inclusion                17               339  ...   0.714286  0.065640
financial innovation                8                44  ...   0.652174  0.034354
financial service                  11               300  ...   0.750000  0.056295
financial technologies             28               225  ...   0.750000  0.080270
fintech                           139              1285  ...   1.000000  0.270653
innovation                         13               249  ...   0.681818  0.055722
peer-to-peer lending                8                73  ...   0.600000  0.026159
regulation                         11                84  ...   0.714286  0.060199
risk                                7                15  ...   0.714286  0.041586
technology                          7               192  ...   0.652174  0.041034
<BLANKLINE>
[16 rows x 6 columns]

"""


def network_indicators(network):
    indicators = network["indicators"].copy()
    indicators = indicators.set_index("node")
    return indicators
