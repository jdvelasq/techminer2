# flake8: noqa
"""
Co-occurrence Network
===============================================================================


Example
-------------------------------------------------------------------------------

>>> root_dir = "data/regtech/"

>>> import techminer2plus
>>> nnet = techminer2plus.report.conceptual_structure.co_occurrence_network(
...     field="author_keywords",
...     top_n=50,
...     root_dir=root_dir,
...     community_clustering="louvain",
...     network_viewer_dict={'nx_k': 0.5, 'nx_iterations': 10},
... )


>>> file_name = "sphinx/_static/bibliometrix__co_occurrence_network.html"
>>> nnet.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__co_occurrence_network.html" height="600px" width="100%" frameBorder="0"></iframe>

>>> nnet.communities_.head()
                            CL_00  ...                           CL_04
0                  REGTECH 28:329  ...    ANTI_MONEY_LAUNDERING 04:023
1               BLOCKCHAIN 03:005  ...  ARTIFICIAL_INTELLIGENCE 04:023
2           SMART_CONTRACT 02:022  ...              CHARITYTECH 02:017
3           ACCOUNTABILITY 02:014  ...              ENGLISH_LAW 02:017
4  DATA_PROTECTION_OFFICER 02:014  ...   COUNTER_TERROR_FINANCE 01:014
<BLANKLINE>
[5 rows x 5 columns]


>>> file_name = "sphinx/_static/bibliometrix__co_occurrence_network_degree_plot.html"
>>> nnet.degree_plot_.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__co_occurrence_network_degree_plot.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> nnet.metrics_.table_.head()
                             Degree  Betweenness  Closeness  PageRank
REGTECH 28:329                   37     0.503565   0.720588  0.090497
FINTECH 12:249                   25     0.135708   0.612500  0.058191
REGULATION 05:164                14     0.036919   0.538462  0.032902
COMPLIANCE 07:030                13     0.016128   0.471154  0.032819
FINANCIAL_REGULATION 04:035      13     0.034042   0.532609  0.029943



# pylint: disable=line-too-long
"""

# from ...check_params import check_keywords
# from ...classes import CoWordsNetwork

# # from ..._network_community_detection import network_community_detection
# from ...vantagepoint.analyze import (
#     co_occurrence_matrix,
#     matrix_normalization,
#     network_clustering,
#     network_communities,
#     network_degree_plot,
#     network_metrics,
#     network_viewer,
# )


def co_occurrence_network(
    # 'co_occurrence_matrix' params:
    field,
    top_n=None,
    occ_range=None,
    gc_range=None,
    custom_items=None,
    # 'cluster_field' params:
    normalization="association",
    community_clustering="louvain",
    # report:
    directory_for_results="co-occurrence_network/",
    # Results params:
    network_viewer_dict=None,
    network_degree_plot_dict=None,
    # Database params:
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Co-occurrence network."""

    check_keywords(field)

    if network_degree_plot_dict is None:
        network_degree_plot_dict = {}

    if network_viewer_dict is None:
        network_viewer_dict = {}

    coc_matrix = co_occurrence_matrix(
        columns=field,
        col_top_n=top_n,
        col_occ_range=occ_range,
        col_gc_range=gc_range,
        col_custom_items=custom_items,
        # Database params:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    norm_coc_matrix = matrix_normalization(
        coc_matrix, index_name=normalization
    )
    graph = network_clustering(
        norm_coc_matrix, community_clustering=community_clustering
    )

    network = CoWordsNetwork()
    network.degree_plot_ = network_degree_plot(
        graph=graph, **network_degree_plot_dict
    )

    network.communities_ = network_communities(graph=graph)
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
