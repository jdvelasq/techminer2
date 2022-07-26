"""
Co-occurrence Network
===============================================================================


>>> directory = "data/regtech/"

>>> from techminer2 import bibliometrix__co_occurrence_network
>>> nnet = bibliometrix__co_occurrence_network(
...     criterion="author_keywords",
...     topics_length=20,
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
0                regtech 69:461  ...     financial services 05:135
1  regulatory technology 12:047  ...    financial inclusion 05:068
2             compliance 12:020  ...  anti-money laundering 04:030
3   financial technology 09:032  ...   financial innovation 04:007
4   financial regulation 08:091  ...                              
<BLANKLINE>
[5 rows x 4 columns]

>>> file_name = "sphinx/_static/bibliometrix__co_occurrence_network_degree_plot.html"
>>> nnet.degree_plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__co_occurrence_network_degree_plot.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> nnet.indicators_.head()
                              group  betweenness  closeness  pagerank
accountability 04:022             0     0.002144   0.575758  0.028472
anti-money laundering 04:030      3     0.002437   0.575758  0.024943
big data 04:027                   1     0.006391   0.655172  0.067830
crowdfunding 04:030               1     0.014529   0.678571  0.093745
cryptocurrency 04:029             1     0.011062   0.655172  0.058653


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
    criterion,
    topics_length=None,
    min_occ_per_topic=None,
    normalization="association",
    method="louvain",
    nx_k=0.5,
    nx_iterations=10,
    delta=1.0,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Co-occurrence network."""

    if criterion not in [
        "author_keywords",
        "index_keywords",
        "title_keywords",
        "abstract_keywords",
        "all_keywords",
    ]:
        raise ValueError(
            f"criterion must be one of: "
            f"'author_keywords', 'index_keywords', 'title_keywords', 'abstract_keywords', 'all_keywords'"
        )

    matrix = vantagepoint__co_occ_matrix(
        criterion=criterion,
        topics_length=topics_length,
        min_occ_per_topic=min_occ_per_topic,
        min_citations_per_topic=0,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
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
