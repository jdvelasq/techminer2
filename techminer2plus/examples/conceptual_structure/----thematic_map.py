# flake8: noqa
"""
Thematic Map
===============================================================================


>>> directory = "data/regtech/"

>>> import techminer2plus
>>> nnet = techminer2plus.examples.conceptual_structure.thematic_map(
...     field="author_keywords",
...     top_n=60,
...     directory=directory,
...     community_clustering="louvain",
...     network_viewer_dict={'nx_k': 0.5, 'nx_iterations': 10},
... )


>>> file_name = "sphinx/_static/examples/thematic_map_plot.html"
>>> nnet.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/examples/thematic_map_plot.html" height="600px" width="100%" frameBorder="0"></iframe>

>>> nnet.communities_.head()
                   CL_00  ...           CL_05
0         REGTECH 28:329  ...   DOGMAS 01:005
1      COMPLIANCE 07:030  ...    MILES 01:005
2      BLOCKCHAIN 03:005  ...  NEOLOGY 01:005
3  SMART_CONTRACT 02:022  ...                
4  ACCOUNTABILITY 02:014  ...                
<BLANKLINE>
[5 rows x 6 columns]

>>> file_name = "sphinx/_static/examples/thematic_map_degree_plot.html"
>>> nnet.degree_plot_.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/examples/thematic_map_degree_plot.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> nnet.metrics_.table_.head()
                                        Degree  ...  PageRank
REGTECH 28:329                              41  ...  0.083245
FINTECH 12:249                              27  ...  0.052162
REGULATION 05:164                           16  ...  0.031134
COMPLIANCE 07:030                           15  ...  0.031375
REGULATORY_TECHNOLOGY (REGTECH) 04:030      14  ...  0.031678
<BLANKLINE>
[5 rows x 4 columns]


# >>> file_name = "sphinx/_static/examples/thematic_map_mds_map.html"
# >>> nnet.mds_map_.write_html(file_name)

# .. raw:: html

#     <iframe src="../../../_static/examples/thematic_map_mds_map.html" height="600px" width="100%" frameBorder="0"></iframe>


# >>> file_name = "sphinx/_static/examples/thematic_map_tsne_map.html"
# >>> nnet.tsne_map_.write_html(file_name)

# .. raw:: html

#     <iframe src="../../../_static/examples/co_occurrence_network_tsne_map.html" height="600px" width="100%" frameBorder="0"></iframe>



# pylint: disable=line-too-long
"""
# from .co_word_network import co_word_network


# pylint: disable=too-many-arguments
def thematic_map(
    # 'co_occ_matrix' params:
    field,
    top_n=None,
    occ_range=None,
    gc_range=None,
    custom_items=None,
    # 'cluster_field' params:
    community_clustering="louvain",
    # report:
    directory_for_results="thematic_map/",
    n_keywords=10,
    # Results params:
    network_viewer_dict=None,
    network_degree_plot_dict=None,
    # Database params:
    directory="./",
    database="main",
    year_filter=None,
    citer_by_filter=None,
    **filters,
):
    """Thematic map network analysis"""

    return co_word_network(
        # 'co_occ_matrix' params:
        field=field,
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        # 'cluster_column' params:
        normalization="association",
        community_clustering=community_clustering,
        # report:
        directory_for_results=directory_for_results,
        # Results params:
        network_viewer_dict=network_viewer_dict,
        network_degree_plot_dict=network_degree_plot_dict,
        # Database params:
        root_dir=directory,
        database=database,
        year_filter=year_filter,
        cited_by_filter=citer_by_filter,
        **filters,
    )
