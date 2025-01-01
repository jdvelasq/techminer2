# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Treemap
===============================================================================

## >>> from techminer2.analyze.co_occurrence_network import treemap
## >>> plot = treemap(
## ...     .set_analysis_params(
## ...         association_index="association",
## ...     .set_item_params(
## ...         field="author_keywords",
## ...         top_n=20,
## ...         occ_range=(None, None),
## ...         gc_range=(None, None),
## ...         custom_terms=None,
## ...     #
## ...     ).set_plot_params(
## ...         title=None,
## ...     #
## ...     ).set_database_params(
## ...         root_dir="example/", 
## ...         database="main",
## ...         year_filter=(None, None),
## ...         cited_by_filter=(None, None),
## ...     #
## ...     ).build()
## ... )
## >>> plot.write_html("sphinx/_static/co_occurrence_network/treemap.html")

.. raw:: html

    <iframe src="../_static/co_occurrence_network/treemap.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

"""
from ...internals.nx.nx_assign_colors_to_nodes_by_group_attribute import (
    nx_assign_colors_to_nodes_by_group_attribute,
)
from ...internals.nx.nx_cluster_graph import nx_cluster_graph
from ...internals.nx.nx_plot_node_treemap import nx_plot_node_treemap
from ..cross_co_occurrence.internals.create_co_occurrence_nx_graph import (
    _create_co_occurrence_nx_graph,
)


def treemap(
    #
    # PARAMS:
    field,
    #
    # COLUMN PARAMS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_terms=None,
    #
    # NETWORK PARAMS:
    algorithm_or_dict="louvain",
    association_index="association",
    #
    # DEGREE PLOT:
    title=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """:meta private:"""

    nx_graph = _create_co_occurrence_nx_graph(
        #
        # FUNCTION PARAMS:
        rows_and_columns=field,
        #
        # COLUMN PARAMS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_terms=custom_terms,
        #
        # NETWORK PARAMS:
        association_index=association_index,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    nx_graph = nx_cluster_graph(
        #
        # FUNCTION PARAMS:
        nx_graph=nx_graph,
        #
        # NETWORK CLUSTERING:
        algorithm_or_dict=algorithm_or_dict,
    )

    nx_graph = nx_assign_colors_to_nodes_by_group_attribute(nx_graph)

    return nx_plot_node_treemap(
        #
        # FUNCTION PARAMS:
        nx_graph=nx_graph,
        #
        # CHART PARAMS:
        title=title,
    )
