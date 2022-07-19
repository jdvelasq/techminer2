"""
Co-Words Network
===============================================================================


>>> directory = "data/regtech/"

>>> from techminer2 import co_words_network
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

    <iframe src="../../../_static/co_words_network_plot.html" height="600px" width="100%" frameBorder="0"></iframe>

>>> nnet.communities_.head()
                            CL_00  ...                    CL_02
0                  regtech 70:462  ...        regulation 06:120
1                  fintech 42:406  ...      crowdfunding 04:030
2               blockchain 18:109  ...  cryptocurrencies 04:029
3  artificial intelligence 13:065  ...        innovation 04:029
4               compliance 12:020  ...          big data 04:027
<BLANKLINE>
[5 rows x 3 columns]

>>> file_name = "sphinx/_static/co_words_network_degree_plot.html"
>>> nnet.degree_plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/co_words_network_degree_plot.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> nnet.indicators_.head()
                                group  betweenness  closeness  pagerank
regtech 70:462                      0     0.131537   1.000000  0.214240
fintech 42:406                      0     0.131537   1.000000  0.167876
blockchain 18:109                   0     0.060777   0.826087  0.077431
artificial intelligence 13:065      0     0.053314   0.791667  0.059587
compliance 12:020                   0     0.007317   0.612903  0.038065


"""

from ....network import network

co_words_network = network
