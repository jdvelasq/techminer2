"""
Collaboration Network
===============================================================================

.. note:: 
    A collaboration network is a generic co-occurrence network where the analized column
    is restricted to the following columns in the dataset:

    * Authors.

    * Institutions.

    * Countries.

    As a consequence, many implemented plots and analysis are valid for analyzing a 
    co-occurrence network, including heat maps and other plot types.


>>> from techminer2 import *
>>> directory = "data/regtech/"

>>> from .collaboration_network import collaboration_network
>>> nnet = collaboration_network(
...     "authors",
...     top_n=20,
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
               CL_01            CL_02  ...           CL_04               CL_05
0     Arner DW 7:220  Brennan R 3:008  ...   Mayer N 2:002  Abi-Lahoud E 1:000
1   Buckley RP 6:217     Ryan P 3:008  ...  Aubert J 1:001     Muckley C 1:000
2  Barberis JN 4:146    Crane M 2:008  ...                                    
3  Zetzsche DA 4:092                   ...                                    
4                                      ...                                    
<BLANKLINE>
[5 rows x 8 columns]

>>> file_name = "sphinx/_static/collaboration_network_degree_plot.html"
>>> nnet.degree_plot_.write_html(file_name)

.. raw:: html

    <iframe src="_static/collaboration_network_degree_plot.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> nnet.indicators_.head()
                   group  betweenness  closeness  pagerank
Arner DW 7:220         1          0.0   0.136364  0.058399
Buckley RP 6:217       1          0.0   0.136364  0.054505
Barberis JN 4:146      1          0.0   0.136364  0.035625
Zetzsche DA 4:092      1          0.0   0.136364  0.039265
Brennan R 3:008        2          0.0   0.090909  0.049926


"""

from .network import network

collaboration_network = network
