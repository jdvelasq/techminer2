"""
Co-occurrence Network
===============================================================================


>>> directory = "data/regtech/"

>>> from techminer2 import bibliometrix__co_occurrence_network
>>> nnet = bibliometrix__co_occurrence_network(
...     "author_keywords",
...     top_n=20,
...     directory=directory,
...     method="louvain",
...     nx_k=0.5,
...     nx_iterations=10,
...     delta=1.0,    
... )


>>> file_name = "sphinx/_static/bibliometrix__co_occurrence_network.html"
>>> nnet.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__co_occurrence_network.html" height="600px" width="100%" frameBorder="0"></iframe>

>>> nnet.communities_.head()
                                      CL_00  ...                         CL_03
0                            regtech 70:462  ...      financial service 05:135
1  regulatory technologies (regtech) 12:047  ...    financial inclusion 05:068
2                         compliance 12:020  ...  anti-money laundering 04:030
3             financial technologies 09:032  ...   financial innovation 04:007
4               financial regulation 08:091  ...                              
<BLANKLINE>
[5 rows x 4 columns]

>>> file_name = "sphinx/_static/bibliometrix__co_occurrence_network_degree_plot.html"
>>> nnet.degree_plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__co_occurrence_network_degree_plot.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> nnet.indicators_.head()
                              group  betweenness  closeness  pagerank
accountability 04:022             0     0.002144   0.575758  0.028473
anti-money laundering 04:030      3     0.002437   0.575758  0.024950
big data 04:027                   1     0.006391   0.655172  0.067873
crowdfunding 04:030               1     0.014529   0.678571  0.093820
cryptocurrencies 04:029           1     0.011062   0.655172  0.058695


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


def bibliometrix__co_occurrence_network(
    column,
    top_n=None,
    directory="./",
    database="documents",
    normalization="association",
    method="louvain",
    nx_k=0.5,
    nx_iterations=10,
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
        nx_iteratons=nx_iterations,
        delta=delta,
    )
    results.degree_plot_ = get_network_graph_degree_plot(graph)

    return results
