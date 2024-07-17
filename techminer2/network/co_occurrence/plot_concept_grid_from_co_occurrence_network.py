# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Concept Grid
===============================================================================


>>> from techminer2.network.co_occurrence import plot_concept_grid_from_co_occurrence_network
>>> chart = plot_concept_grid_from_co_occurrence_network(
...     #
...     # PARAMS:
...     field='author_keywords',
...     #
...     # SUMMARY PARAMS:
...     conserve_counters=False,
...     #
...     # FILTER PARAMS:
...     top_n=20,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_items=None,
...     #
...     # NETWORK PARAMS:
...     algorithm_or_dict="louvain",
...     association_index="association",
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> chart.render("sphinx/images/analyze/co_occurrence/network/concept_grid", format="png")
'sphinx/images/analyze/co_occurrence/network/concept_grid.png'

.. image:: /images/analyze/co_occurrence/network/concept_grid.png
    :width: 900px
    :align: center

"""
from ...core.nx.nx_cluster_graph import nx_cluster_graph
from ...core.nx.nx_create_co_occurrence_graph import nx_create_co_occurrence_graph
from ...core.nx.nx_plot_concept_grid import nx_plot_concept_grid


def plot_concept_grid_from_co_occurrence_network(
    #
    # PARAMS:
    field,
    #
    # CONCEPT GRID PARAMS:
    conserve_counters=False,
    n_head=None,
    fontsize="9",
    #
    # COLUMN PARAMS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_items=None,
    #
    # NETWORK PARAMS:
    algorithm_or_dict="louvain",
    association_index="association",
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """:meta private:"""

    nx_graph = nx_create_co_occurrence_graph(
        #
        # FUNCTION PARAMS:
        rows_and_columns=field,
        #
        # COLUMN PARAMS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
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

    return nx_plot_concept_grid(
        nx_graph=nx_graph,
        conserve_counters=conserve_counters,
        n_head=n_head,
        fontsize=fontsize,
    )
