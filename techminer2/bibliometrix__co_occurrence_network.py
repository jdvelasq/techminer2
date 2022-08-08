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



>>> file_name = "sphinx/_static/bibliometrix__co_occurrence_network_mds_map.html"
>>> nnet.mds_map_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__co_occurrence_network_mds_map.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> file_name = "sphinx/_static/bibliometrix__co_occurrence_network_tsne_map.html"
>>> nnet.tsne_map_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__co_occurrence_network_tsne_map.html" height="600px" width="100%" frameBorder="0"></iframe>


"""
import os.path
from dataclasses import dataclass

from sklearn.manifold import MDS, TSNE

from ._association_index import association_index
from ._cluster_abstracts_report import cluster_abstracts_report
from ._clusters_concordances import clusters_concordances
from ._create_directory import create_directory
from ._get_network_graph_communities import get_network_graph_communities
from ._get_network_graph_degree_plot import get_network_graph_degree_plot
from ._get_network_graph_indicators import get_network_graph_indicators
from ._get_network_graph_manifold_map import get_network_graph_manifold_map
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
    mds_map_: None
    tsne_map_: None


def bibliometrix__co_occurrence_network(
    criterion,
    topics_length=None,
    topic_min_occ=None,
    normalization="association",
    # summarize=False,
    directory_for_results="co-occurrence_network/",
    n_keywords=10,
    # n_abstracts=50,
    # n_phrases_per_algorithm=5,
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
        "raw_author_keywords",
        "raw_index_keywords",
        "raw_title_words",
        "raw_abstract_words",
        "raw_words",
        "author_keywords",
        "index_keywords",
        "title_words",
        "abstract_words",
        "words",
    ]:
        raise ValueError(
            "criterion must be one of: "
            "{'author_keywords', 'index_keywords', 'title_words', 'abstract_words', 'words', "
            "{'raw_author_keywords', 'raw_index_keywords', 'raw_title_words', 'raw_abstract_words', "
            "'raw_words'}"
        )

    matrix = vantagepoint__co_occ_matrix(
        criterion=criterion,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_min_citations=0,
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
        nx_iterations=nx_iterations,
        delta=delta,
    )
    results.degree_plot_ = get_network_graph_degree_plot(graph)

    results.mds_map_ = get_network_graph_manifold_map(
        matrix_list=matrix_list,
        graph=graph,
        manifold_method=MDS(n_components=2),
    )

    results.tsne_map_ = get_network_graph_manifold_map(
        matrix_list=matrix_list,
        graph=graph,
        manifold_method=TSNE(n_components=2),
    )

    create_directory(
        base_directory=directory,
        target_directory=directory_for_results,
    )

    # if summarize is True:
    #     directory_for_summarization = os.path.join(
    #         directory_for_results, "summarization"
    #     )
    #     clusters_summarization(
    #         criterion=criterion,
    #         communities=results.communities_,
    #         directory_for_summarization=directory_for_summarization,
    #         n_keywords=n_keywords,
    #         n_abstracts=n_abstracts,
    #         n_phrases_per_algorithm=n_phrases_per_algorithm,
    #         directory=directory,
    #         database=database,
    #         start_year=start_year,
    #         end_year=end_year,
    #         **filters,
    #     )

    directory_for_abstracts = os.path.join(directory_for_results, "abstracts")
    cluster_abstracts_report(
        criterion=criterion,
        communities=results.communities_,
        directory_for_abstracts=directory_for_abstracts,
        n_keywords=n_keywords,
        # n_abstracts=n_abstracts,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    directory_for_concordances = os.path.join(directory_for_results, "concordances")
    clusters_concordances(
        communities=results.communities_,
        directory_for_concordances=directory_for_concordances,
        n_keywords=n_keywords,
        # n_abstracts=n_abstracts,
        directory=directory,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    return results
