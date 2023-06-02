# flake8: noqa
"""
Co-occurrence Network
===============================================================================


>>> root_dir = "data/regtech/"

>>> from techminer2 import bibliometrix
>>> nnet = bibliometrix.conceptual_structure.co_occurrence_network(
...     field="author_keywords",
...     top_n=50,
...     root_dir=root_dir,
...     method="louvain",
...     network_viewer_dict={'nx_k': 0.5, 'nx_iterations': 10},
... )


>>> file_name = "sphinx/_static/bibliometrix__co_occurrence_network.html"
>>> nnet.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__co_occurrence_network.html" height="600px" width="100%" frameBorder="0"></iframe>

>>> nnet.communities_.head()
                            CL_00  ...                              CL_04
0                  regtech 28:329  ...                  innovation 03:012
1               compliance 07:030  ...                 coronavirus 01:011
2  artificial intelligence 04:023  ...        digital technologies 01:011
3    anti-money laundering 03:021  ...  regulations and compliance 01:011
4               blockchain 03:005  ...              smart treasury 01:011
<BLANKLINE>
[5 rows x 5 columns]

>>> file_name = "sphinx/_static/bibliometrix__co_occurrence_network_degree_plot.html"
>>> nnet.degree_plot_.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__co_occurrence_network_degree_plot.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> nnet.metrics_.table_.head()
                              Degree  Betweenness  Closeness  PageRank
regtech 28:329                    38     0.478025   0.816667  0.091289
fintech 12:249                    25     0.131540   0.671233  0.056730
regulatory technology 07:037      21     0.327307   0.636364  0.049180
regulation 05:164                 15     0.032893   0.590361  0.034642
compliance 07:030                 14     0.042971   0.583333  0.034957

# pylint: disable=line-too-long
"""
# import os.path

# from sklearn.manifold import MDS, TSNE

# from ..._cluster_abstracts_report import cluster_abstracts_report
# from ..._clusters_concordances import clusters_concordances

# from ..._get_network_graph_communities import get_network_graph_communities
# from ..._get_network_graph_degree_plot import get_network_graph_degree_plot

from ...classes import CoWordsNetwork

# from ..._get_network_graph_indicators import get_network_graph_indicators
# from ..._get_network_graph_manifold_map import get_network_graph_manifold_map
# from ..._get_network_graph_plot import get_network_graph_plot
# from ..._matrix_2_matrix_list import matrix_2_matrix_list
# from ..._matrix_list_2_network_graph import matrix_list_2_network_graph
# from ...create_directory import create_directory
from ...utils import check_keywords

# from ..._network_community_detection import network_community_detection
from ...vantagepoint.analyze import (
    association_index,
    cluster_field,
    cluster_items,
    co_occ_matrix,
    network_degree_plot,
    network_metrics,
    network_viewer,
)


def co_occurrence_network(
    # 'co_occ_matrix' params:
    field,
    top_n=None,
    occ_range=None,
    gc_range=None,
    custom_items=None,
    # 'cluster_field' params:
    normalization="association",
    method="louvain",
    # report:
    directory_for_results="co-occurrence_network/",
    # Results params:
    network_viewer_dict=None,
    network_degree_plot_dict=None,
    # Database params:
    root_dir="./",
    database="documents",
    year_range=None,
    cited_by_range=None,
    **filters,
):
    """Co-occurrence network."""

    check_keywords(field)

    if network_degree_plot_dict is None:
        network_degree_plot_dict = {}

    if network_viewer_dict is None:
        network_viewer_dict = {}

    coc_matrix = co_occ_matrix(
        columns=field,
        col_top_n=top_n,
        col_occ_range=occ_range,
        col_gc_range=gc_range,
        col_custom_items=custom_items,
        # Database params:
        root_dir=root_dir,
        database=database,
        year_filter=year_range,
        cited_by_filter=cited_by_range,
        **filters,
    )

    norm_coc_matrix = association_index(coc_matrix, index_name=normalization)
    graph = cluster_field(norm_coc_matrix, community_clustering=method)

    network = CoWordsNetwork()
    network.degree_plot_ = network_degree_plot(
        graph=graph, **network_degree_plot_dict
    )

    network.communities_ = cluster_items(graph=graph)
    network.metrics_ = network_metrics(graph=graph)

    network.plot_ = network_viewer(graph=graph, **network_viewer_dict)

    ###

    # coc_keywords_network.mds_map_ = get_network_graph_manifold_map(
    #     matrix_list=matrix_list,
    #     graph=graph,
    #     manifold_method=MDS(n_components=2),
    # )

    # coc_keywords_network.tsne_map_ = get_network_graph_manifold_map(
    #     matrix_list=matrix_list,
    #     graph=graph,
    #     manifold_method=TSNE(n_components=2),
    # )

    # create_directory(
    #     base_dir=root_dir,
    #     target_dir=directory_for_results,
    # )

    # directory_for_abstracts = os.path.join(directory_for_results, "abstracts")

    # cluster_abstracts_report(
    #     criterion=field,
    #     communities=coc_keywords_network.communities_,
    #     directory_for_abstracts=directory_for_abstracts,
    #     n_keywords=n_keywords,
    #     directory=root_dir,
    #     database=database,
    #     start_year=year_range,
    #     end_year=cited_by_range,
    #     **filters,
    # )

    # directory_for_concordances = os.path.join(
    #     directory_for_results, "concordances"
    # )
    # clusters_concordances(
    #     communities=coc_keywords_network.communities_,
    #     directory_for_concordances=directory_for_concordances,
    #     n_keywords=n_keywords,
    #     directory=root_dir,
    #     start_year=year_range,
    #     end_year=cited_by_range,
    #     **filters,
    # )

    return network
