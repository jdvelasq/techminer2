"""
Clustering by coupling.
===============================================================================


>>> directory = "data/regtech/"

>>> from techminer2 import bibliometrix__coupling_network
>>> nnet = bibliometrix__coupling_network(
...     unit_of_analysis="article",
...     coupling_measured_by='local_references',
...     top_n=50,
...     metric="local_citations",
...     directory=directory,
...     method="louvain",
...     nx_k=0.5,
...     nx_iteratons=10,
...     delta=1.0,    
... )

>>> file_name = "sphinx/_static/bibliometrix_coupling_network_plot_by_references.html"
>>> nnet.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/bibliometrix_coupling_network_plot_by_references.html" height="600px" width="100%" frameBorder="0"></iframe>

>>> nnet.communities_.head()
                                               CL_00  ...                                              CL_19
0  Arner DW, 2019, EUR BUS ORG LAW REV, V20, P55 ...  ...  Thilakarathne DJ, 2020, LECT NOTES COMPUT SCI,...
1     Buckley RP, 2020, J BANK REGUL, V21, P26 1:017  ...                                                   
2  Kavassalis P, 2018, J RISK FINANC, V19, P39 1:014  ...                                                   
3  Micheler E, 2020, EUR BUS ORG LAW REV, V21, P3...  ...                                                   
4  Ryan P, 2020, ICEIS - PROC INT CONF ENTERP INF...  ...                                                   
<BLANKLINE>
[5 rows x 20 columns]



>>> file_name = "sphinx/_static/bibliometrix_coupling_network_plot_by_references_degree_plot.html"
>>> nnet.degree_plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/bibliometrix_coupling_network_plot_by_references_degree_plot.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> nnet.indicators_.head()
                                                    group  ...  pagerank
Abi-Lahoud E, 2018, CEUR WORKSHOP PROC, V2044 1...      7  ...  0.003851
Anagnostopoulos I, 2018, J ECON BUS, V100, P7 1...      1  ...  0.036072
Arner DW, 2017, NORTHWEST J INTL LAW BUS, V37, ...      1  ...  0.009836
Arner DW, 2019, EUR BUS ORG LAW REV, V20, P55 1...      0  ...  0.019796
Arner DW, 2020, EUR BUS ORG LAW REV, V21, P7 1:040      1  ...  0.041074
<BLANKLINE>
[5 rows x 4 columns]


"""
from dataclasses import dataclass

from .bibliometrix__coupling_matrix_list import bibliometrix__coupling_matrix_list
from ._get_network_graph_communities import get_network_graph_communities
from ._get_network_graph_degree_plot import get_network_graph_degree_plot
from ._get_network_graph_indicators import get_network_graph_indicators
from ._get_network_graph_plot import network_graph_plot
from ._matrix_list_2_network_graph import matrix_list_2_network_graph
from ._network_community_detection import network_community_detection


@dataclass(init=False)
class _Results:
    communities_: None
    indicators_: None
    plot_: None
    degree_plot_: None


def bibliometrix__coupling_network(
    unit_of_analysis,
    coupling_measured_by,
    top_n=250,
    metric="local_citations",
    directory="./",
    method="louvain",
    nx_k=0.5,
    nx_iteratons=10,
    delta=1.0,
):
    """Clustering by coupling."""

    matrix_list = bibliometrix__coupling_matrix_list(
        unit_of_analysis=unit_of_analysis,
        coupling_measured_by=coupling_measured_by,
        top_n=top_n,
        metric=metric,
        directory=directory,
    )

    graph = matrix_list_2_network_graph(matrix_list)
    graph = network_community_detection(graph, method=method)

    result = _Results()

    result.communities_ = get_network_graph_communities(graph)
    result.indicators_ = get_network_graph_indicators(graph)
    result.plot_ = network_graph_plot(
        graph,
        nx_k=nx_k,
        nx_iterations=nx_iteratons,
        delta=delta,
    )
    result.degree_plot_ = get_network_graph_degree_plot(graph)

    return result
