# flake8: noqa
"""
Collaboration Network
===============================================================================

.. note:: 
    A collaboration network is a generic co-occurrence network where the analized column
    is restricted to the following columns in the dataset:

    * Authors.

    * Organizations.

    * Countries.

    As a consequence, many implemented plots and analysis are valid for analyzing a 
    generic co-occurrence network, including heat maps and other plot types.



>>> root_dir = "data/regtech/"

>>> from techminer2 import bibliometrix
>>> nnet = bibliometrix.social_structure.collaboration_network(
...     field="authors",
...     top_n=20,
...     root_dir=root_dir,
...     community_clustering="louvain",
...     network_viewer_dict={'nx_k': 0.5, 'nx_iterations': 10},
... )


>>> file_name = "sphinx/_static/bibliometrix__co_authorship_network_plot.html"
>>> nnet.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../_static/bibliometrix__co_authorship_network_plot.html" height="600px" width="100%" frameBorder="0"></iframe>

>>> nnet.communities_.head()
               CL_00           CL_01  ...          CL_04               CL_05
0     Arner DW 3:185  Hamdan A 2:018  ...    Lin W 2:017      Grassi L 2:002
1   Buckley RP 3:185   Turki M 2:018  ...  Singh C 2:017  Lanfranchi D 2:002
2  Barberis JN 2:161   Sarea A 2:012  ...                                   
3     Weber RH 1:024                  ...                                   
4  Zetzsche DA 1:024                  ...                                   
<BLANKLINE>
[5 rows x 6 columns]

>>> file_name = "sphinx/_static/bibliometrix__co_authorship_network_degree_plot.html"
>>> nnet.degree_plot_.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../_static/bibliometrix__co_authorship_network_degree_plot.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> nnet.metrics_.table_.head()
                   Degree  Betweenness  Closeness  PageRank
Arner DW 3:185          4     0.008333   0.250000  0.072188
Buckley RP 3:185        4     0.008333   0.250000  0.072188
Weber RH 1:024          3     0.000000   0.200000  0.055120
Zetzsche DA 1:024       3     0.000000   0.200000  0.055120
Barberis JN 2:161       2     0.000000   0.166667  0.039502


# pylint: disable=line-too-long
"""

from ...classes import CollaborationNetwork
from ...vantagepoint.analyze import (
    association_index,
    cluster_field,
    cluster_members,
    co_occ_matrix,
    network_degree_plot,
    network_metrics,
    network_viewer,
)


def collaboration_network(
    # 'co_occ_matrix' params:
    field,
    top_n=None,
    occ_range=None,
    gc_range=None,
    custom_items=None,
    # 'cluster_field' params:
    normalization="association",
    community_clustering="louvain",
    # Results params:
    network_viewer_dict=None,
    network_degree_plot_dict=None,
    # Database params:
    root_dir="./",
    database="documents",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Co-authorship network"""

    if field not in [
        "authors",
        "organizations",
        "countries",
    ]:
        raise ValueError(
            "criterion must be one of: "
            "{'authors', 'organizations', 'countries'}"
        )

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
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    norm_coc_matrix = association_index(coc_matrix, index_name=normalization)
    graph = cluster_field(
        norm_coc_matrix, community_clustering=community_clustering
    )

    network = CollaborationNetwork()

    network.degree_plot_ = network_degree_plot(
        graph=graph, **network_degree_plot_dict
    )

    network.communities_ = cluster_members(graph=graph)
    network.metrics_ = network_metrics(graph=graph)

    network.plot_ = network_viewer(graph=graph, **network_viewer_dict)

    return network
