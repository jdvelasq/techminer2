"""
Co-occurrence Network
===============================================================================


>>> directory = "data/regtech/"

>>> from techminer2 import bibliometrix
>>> nnet = bibliometrix.conceptual_structure.co_occurrence_network(
...     criterion="author_keywords",
...     topics_length=100,
...     directory=directory,
...     method="louvain",
...     nx_k=0.5,
...     nx_iterations=10,
...     delta=1.0,    
... )
--INFO-- The file 'data/regtech/reports/co-occurrence_network/abstracts/CL_00.txt' was created
--INFO-- The file 'data/regtech/reports/co-occurrence_network/abstracts/CL_01.txt' was created
--INFO-- The file 'data/regtech/reports/co-occurrence_network/abstracts/CL_02.txt' was created
--INFO-- The file 'data/regtech/reports/co-occurrence_network/abstracts/CL_03.txt' was created
--INFO-- The file 'data/regtech/reports/co-occurrence_network/abstracts/CL_04.txt' was created
--INFO-- The file 'data/regtech/reports/co-occurrence_network/abstracts/CL_05.txt' was created
--INFO-- The file 'data/regtech/reports/co-occurrence_network/abstracts/CL_06.txt' was created
--INFO-- The file 'data/regtech/reports/co-occurrence_network/abstracts/CL_07.txt' was created
--INFO-- The file 'data/regtech/reports/co-occurrence_network/abstracts/CL_08.txt' was created
--INFO-- The file 'data/regtech/reports/co-occurrence_network/abstracts/CL_09.txt' was created
--INFO-- The file 'data/regtech/reports/co-occurrence_network/abstracts/CL_10.txt' was created
--INFO-- The file 'data/regtech/reports/co-occurrence_network/abstracts/CL_11.txt' was created
--INFO-- The file 'data/regtech/reports/co-occurrence_network/abstracts/CL_12.txt' was created

>>> file_name = "sphinx/_static/bibliometrix__co_occurrence_network.html"
>>> nnet.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__co_occurrence_network.html" height="600px" width="100%" frameBorder="0"></iframe>

>>> nnet.communities_.head()
                          CL_00  ...                          CL_12
0                regtech 28:329  ...    electronic signature 01:001
1                fintech 12:249  ...  electronic transaction 01:001
2             regulation 05:164  ...                               
3        risk management 03:014  ...                               
4  semantic technologies 02:041  ...                               
<BLANKLINE>
[5 rows x 13 columns]

>>> file_name = "sphinx/_static/bibliometrix__co_occurrence_network_degree_plot.html"
>>> nnet.degree_plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__co_occurrence_network_degree_plot.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> nnet.indicators_.head()
                                   group  betweenness  closeness  pagerank
algorithmic process 01:003             7          0.0   0.412052  0.012485
algorithmic standards 01:021           8          0.0   0.404089  0.010534
algorithmic transparency 01:003        2          0.0   0.406051  0.008777
analytic hierarchy process 01:002      3          0.0   0.404089  0.008727
anomaly detection 01:002               1          0.0   0.267241  0.009048


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

from ..._association_index import association_index
from ..._cluster_abstracts_report import cluster_abstracts_report
from ..._clusters_concordances import clusters_concordances
from ..._create_directory import create_directory
from ..._get_network_graph_communities import get_network_graph_communities
from ..._get_network_graph_degree_plot import get_network_graph_degree_plot
from ..._get_network_graph_indicators import get_network_graph_indicators
from ..._get_network_graph_manifold_map import get_network_graph_manifold_map
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
    mds_map_: None
    tsne_map_: None


def co_occurrence_network(
    criterion,
    topics_length=None,
    topic_min_occ=None,
    normalization="association",
    directory_for_results="co-occurrence_network/",
    n_keywords=10,
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

    matrix = co_occ_matrix(
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
    results.plot_ = get_network_graph_plot(
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
        base_dir=directory,
        target_dir=directory_for_results,
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
        directory=directory,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    return results
