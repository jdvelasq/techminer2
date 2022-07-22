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

>>> from techminer2 import bibliometrix__collaboration_network
>>> nnet = bibliometrix__collaboration_network(
...     "authors",
...     top_n=20,
...     directory=directory,
...     method="louvain",
...     nx_k=0.5,
...     nx_iteratons=10,
...     delta=1.0,    
... )


>>> file_name = "sphinx/_static/bibliometrix__collaboration_network.html"
>>> nnet.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../_static/bibliometrix__collaboration_network.html" height="600px" width="100%" frameBorder="0"></iframe>

>>> nnet.communities_.head()
               CL_00            CL_01  ...         CL_08          CL_09
0     Arner DW 7:220  Brennan R 3:008  ...  Das SR 2:028  Mayer N 2:002
1   Buckley RP 6:217     Ryan P 3:008  ...                             
2  Barberis JN 4:146    Crane M 2:008  ...                             
3  Zetzsche DA 4:092                   ...                             
4      Veidt R 1:040                   ...                             
<BLANKLINE>
[5 rows x 10 columns]


>>> file_name = "sphinx/_static/bibliometrix__collaboration_network_degree_plot.html"
>>> nnet.degree_plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../_static/bibliometrix__collaboration_network_degree_plot.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> nnet.indicators_.head()
                         group  betweenness  closeness  pagerank
Anagnostopoulos I 1:110      5          0.0   0.000000  0.009524
Baxter LG 1:023              6          0.0   0.000000  0.009524
Lamb GW 1:037                3          0.0   0.052632  0.063492
Lui A 1:037                  3          0.0   0.052632  0.063492
Veidt R 1:040                0          0.0   0.168421  0.065063


"""
from dataclasses import dataclass

from ._association_index import association_index
from ._get_network_graph_communities import get_network_graph_communities
from ._get_network_graph_degree_plot import get_network_graph_degree_plot
from ._get_network_graph_indicators import get_network_graph_indicators
from ._get_network_graph_plot import network_graph_plot
from ._matrix_2_matrix_list import matrix_2_matrix_list
from ._matrix_list_2_network_graph import matrix_list_2_network_graph
from ._network_community_detection import network_community_detection
from .vantagepoint__co_occ_matrix import vantagepoint__co_occ_matrix


@dataclass(init=False)
class _Results:
    communities_: None
    indicators_: None
    plot_: None
    degree_plot_: None


def bibliometrix__collaboration_network(
    column,
    top_n=None,
    directory="./",
    database="documents",
    normalization="association",
    method="louvain",
    nx_k=0.5,
    nx_iteratons=10,
    delta=1.0,
):
    """Collaboration network"""

    matrix = vantagepoint__co_occ_matrix(
        column=column,
        row=None,
        top_n=top_n,
        directory=directory,
        database=database,
    )

    matrix = association_index(matrix, association=normalization)
    matrix_list = matrix_2_matrix_list(matrix)

    graph = matrix_list_2_network_graph(matrix_list)
    graph = network_community_detection(graph, method=method)

    results = _Results()
    results.communities_ = get_network_graph_communities(graph)
    results.indicators_ = get_network_graph_indicators(graph)
    results.plot_ = network_graph_plot(
        graph,
        nx_k=nx_k,
        nx_iteratons=nx_iteratons,
        delta=delta,
    )
    results.degree_plot_ = get_network_graph_degree_plot(graph)

    return results
