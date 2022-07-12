"""
Collaboration Network
===============================================================================

>>> from techminer2 import *
>>> directory = "data/regtech/"

>>> from .collaboration_network import collaboration_network
>>> nnet = collaboration_network(
...     "author_keywords",
...     top_n=30,
...     directory=directory,
...     method="louvain",
...     nx_k=0.5,
...     nx_iteratons=10,
...     delta=1.0,    
... )


>>> file_name = "sphinx/_static/collaboration_network_plot.html"
>>> nnet.plot_.write_html(file_name)

.. raw:: html

    <iframe src="_static/collaboration_network_plot.html" height="600px" width="100%" frameBorder="0"></iframe>

>>> nnet.communities_.head()
                        CL_00  ...                    CL_02
0              regtech 70:462  ...      crowdfunding 04:030
1              fintech 42:406  ...  cryptocurrencies 04:029
2           blockchain 18:109  ...          innovate 04:029
3    financial service 05:135  ...          big data 04:027
4  financial inclusion 05:068  ...       p2p lending 03:026
<BLANKLINE>
[5 rows x 5 columns]


>>> file_name = "sphinx/_static/collaboration_network_degree_plot.html"
>>> nnet.degree_plot_.write_html(file_name)

.. raw:: html

    <iframe src="_static/collaboration_network_degree_plot.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> nnet.indicators_.head()
                                group  betweenness  closeness  pagerank
regtech 70:462                      0     0.201186   1.000000  0.186638
fintech 42:406                      0     0.154593   0.966667  0.142002
blockchain 18:109                   0     0.066441   0.783784  0.064016
artificial intelligence 13:065      1     0.044990   0.725000  0.046675
compliance 12:020                   3     0.015157   0.617021  0.034109

"""

from .network import network

collaboration_network = network
