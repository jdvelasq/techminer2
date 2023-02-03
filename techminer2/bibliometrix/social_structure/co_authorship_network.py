"""
Co-authorship (collaboration) Network
===============================================================================

.. note:: 
    A co-authorship network is a generic co-occurrence network where the analized column
    is restricted to the following columns in the dataset:

    * Authors.

    * Organizations.

    * Countries.

    As a consequence, many implemented plots and analysis are valid for analyzing a 
    generic co-occurrence network, including heat maps and other plot types.



>>> directory = "data/regtech/"

>>> from techminer2 import bibliometrix
>>> nnet = bibliometrix.social_structure.co_authorship_network(
...     criterion="authors",
...     topics_length=20,
...     directory=directory,
...     method="louvain",
...     nx_k=0.5,
...     nx_iterations=10,
...     delta=1.0,    
... )


>>> file_name = "sphinx/_static/bibliometrix__co_authorship_network_plot.html"
>>> nnet.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../_static/bibliometrix__co_authorship_network_plot.html" height="600px" width="100%" frameBorder="0"></iframe>

>>> nnet.communities_.head()
               CL_00            CL_01  ...            CL_07           CL_08
0     Arner DW 3:185  Brennan R 2:014  ...  Baxter LG 1:030  Arman AA 2:000
1   Buckley RP 3:185    Crane M 2:014  ...                                 
2  Barberis JN 2:161     Ryan P 2:014  ...                                 
3     Weber RH 1:024                   ...                                 
4  Zetzsche DA 1:024                   ...                                 
<BLANKLINE>
[5 rows x 9 columns]


>>> file_name = "sphinx/_static/bibliometrix__co_authorship_network_degree_plot.html"
>>> nnet.degree_plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../_static/bibliometrix__co_authorship_network_degree_plot.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> nnet.indicators_.head()
                         group  betweenness  closeness  pagerank
Anagnostopoulos I 1:153      6          0.0   0.000000  0.008596
Baxter LG 1:030              7          0.0   0.000000  0.008596
OBrien L 1:033               3          0.0   0.052632  0.057307
Weber RH 1:024               0          0.0   0.168421  0.068181
Zetzsche DA 1:024            0          0.0   0.168421  0.068181

"""
from dataclasses import dataclass

from ..._association_index import association_index
from ..._get_network_graph_communities import get_network_graph_communities
from ..._get_network_graph_degree_plot import get_network_graph_degree_plot
from ..._get_network_graph_indicators import get_network_graph_indicators
from ..._get_network_graph_plot import get_network_graph_plot
from ..._matrix_2_matrix_list import matrix_2_matrix_list
from ..._matrix_list_2_network_graph import matrix_list_2_network_graph
from ..._network_community_detection import network_community_detection
from ...vantagepoint.analyze.matrix.co_occ_matrix import co_occ_matrix


@dataclass(init=False)
class _Results:
    communities_: None
    indicators_: None
    plot_: None
    degree_plot_: None


def co_authorship_network(
    criterion,
    topics_length=None,
    topic_min_occ=None,
    topic_min_citations=None,
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
    """Co-authorship network"""

    if criterion not in [
        "authors",
        "organizations",
        "countries",
    ]:
        raise ValueError(
            "criterion must be one of: " "{'authors', 'organizations', 'countries'}"
        )

    matrix = co_occ_matrix(
        criterion=criterion,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_min_citations=topic_min_citations,
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
    results.plot_ = get_network_graph_plot(
        graph,
        nx_k=nx_k,
        nx_iterations=nx_iterations,
        delta=delta,
    )
    results.degree_plot_ = get_network_graph_degree_plot(graph)

    return results
