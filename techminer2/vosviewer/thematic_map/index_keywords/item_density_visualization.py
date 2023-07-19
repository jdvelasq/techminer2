# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
.. _index_keywords_item_density_visualization:

Item Density Visualization
===============================================================================



>>> from techminer2 import vosviewer
>>> root_dir = "data/regtech/"
>>> vosviewer.co_occurrence.index_keywords.item_density_visualization(
...     root_dir=root_dir,
...     top_n=10, 
...     bandwidth=0.1,
... ).write_html("sphinx/_static/index_keywords_item_density_visualization.html")

.. raw:: html

    <iframe src="../../../../../_static/index_keywords_item_density_visualization.html" height="600px" width="100%" frameBorder="0"></iframe>

"""


from ...nx_create_co_occurrence_graph import nx_create_co_occurrence_graph

# from ...visualize_item_density import visualize_item_density

FIELD = "index_keywords"


def item_density_visualization(
    #
    # COLUMN PARAMS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_items=None,
    #
    # NETWORK PARAMS:
    algorithm_or_estimator="louvain",
    bandwidth="silverman",
    colorscale="Aggrnyl",
    opacity=0.6,
    #
    n_labels=None,
    # color="#7793a5",
    nx_k=None,
    nx_iterations=10,
    nx_random_state=0,
    # node_size_min=30,
    # node_size_max=70,
    textfont_size_min=10,
    textfont_size_max=20,
    # edge_width_min=0.8,
    # edge_width_max=3.0,
    xaxes_range=None,
    yaxes_range=None,
    show_axes=False,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    #
    # TODO: REMOVE DEPENDENCES:
    color = "#7793a5"
    node_size_min = 30
    node_size_max = 70
    edge_width_min = 0.8
    edge_width_max = 3.0

    nx_graph = nx_create_co_occurrence_graph(
        #
        # FUNCTION PARAMS:
        rows_and_columns=FIELD,
        #
        # COLUMN PARAMS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        #
        # NETWORK PARAMS:
        algorithm_or_estimator=algorithm_or_estimator,
        normalization_index=None,
        color=color,
        nx_k=nx_k,
        nx_iterations=nx_iterations,
        nx_random_state=nx_random_state,
        node_size_min=node_size_min,
        node_size_max=node_size_max,
        textfont_size_min=textfont_size_min,
        textfont_size_max=textfont_size_max,
        edge_width_min=edge_width_min,
        edge_width_max=edge_width_max,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    return visualize_item_density(
        #
        # FUNCTION PARAMS:
        nx_graph=nx_graph,
        #
        # NETWORK PARAMS:
        bandwidth=bandwidth,
        colorscale=colorscale,
        opacity=opacity,
        # n_labels=n_labels,
        xaxes_range=xaxes_range,
        yaxes_range=yaxes_range,
        show_axes=show_axes,
    )
