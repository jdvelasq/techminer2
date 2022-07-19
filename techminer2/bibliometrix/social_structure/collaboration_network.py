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



>>> directory = "data/regtech/"

>>> from techminer2.bbx.social_structure import collaboration_network
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

    <iframe src="../../_static/collaboration_network_plot.html" height="600px" width="100%" frameBorder="0"></iframe>

>>> nnet.communities_.head()
               CL_00            CL_01  ...                    CL_08            CL_09
0     Arner DW 7:220  Brennan R 3:008  ...  Anagnostopoulos I 1:110  Baxter LG 1:023
1   Buckley RP 6:217     Ryan P 3:008  ...                                          
2  Barberis JN 4:146    Crane M 2:008  ...                                          
3  Zetzsche DA 4:092                   ...                                          
4      Veidt R 1:040                   ...                                          
<BLANKLINE>
[5 rows x 10 columns]


>>> file_name = "sphinx/_static/collaboration_network_degree_plot.html"
>>> nnet.degree_plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/collaboration_network_degree_plot.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> nnet.indicators_.head()
                   group  betweenness  closeness  pagerank
Arner DW 7:220         0     0.001949   0.210526  0.091395
Buckley RP 6:217       0     0.001949   0.210526  0.085773
Barberis JN 4:146      0     0.000000   0.168421  0.051275
Zetzsche DA 4:092      0     0.001949   0.210526  0.063693
Brennan R 3:008        1     0.000000   0.105263  0.067520

"""

from ...network import network

collaboration_network = network
