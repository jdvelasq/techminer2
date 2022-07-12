"""
Co-Words Network
===============================================================================

>>> from techminer2 import *
>>> directory = "data/regtech/"

>>> nnet = co_words_network(
...     "author_keywords",
...     top_n=20,
...     directory=directory,
...     method="louvain",
...     nx_k=0.5,
...     nx_iteratons=10,
...     delta=1.0,    
... )


>>> file_name = "sphinx/_static/co_words_network_plot.html"
>>> nnet.plot_.write_html(file_name)

.. raw:: html

    <iframe src="_static/co_words_network_plot.html" height="600px" width="100%" frameBorder="0"></iframe>

>>> nnet.communities_.head()
                            CL_00  ...                    CL_02
0                  regtech 70:462  ...      crowdfunding 04:030
1                  fintech 42:406  ...  cryptocurrencies 04:029
2               blockchain 18:109  ...          big data 04:027
3  artificial intelligence 13:065  ...                         
4               compliance 12:020  ...                         
<BLANKLINE>
[5 rows x 3 columns]

>>> file_name = "sphinx/_static/co_words_network_degree_plot.html"
>>> nnet.degree_plot_.write_html(file_name)

.. raw:: html

    <iframe src="_static/co_words_network_degree_plot.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> nnet.indicators_.head()
                                group  betweenness  closeness  pagerank
regtech 70:462                      0     0.131628   1.000000  0.214319
fintech 42:406                      0     0.131628   1.000000  0.166280
blockchain 18:109                   0     0.061647   0.826087  0.077500
artificial intelligence 13:065      0     0.060429   0.826087  0.061255
compliance 12:020                   0     0.010088   0.633333  0.039735


"""

from .network import network

co_words_network = network
