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


>>> from techminer2.science_mapping.co_occurrence import concept_grid
>>> chart = concept_grid(
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
from ...core.network.nx_concept_grid import nx_concept_grid
from ...core.network.co_occurrence_network.create_graph_from_co_occurrence_network import (
    create_graph_from_co_occurrence_network,
)


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
    """
    :meta private:
    """
    # --------------------------------------------------------------------------
    # TODO: REMOVE DEPENDENCES:
    #
    #
    # NODES:
    node_size_range = (30, 70)
    textfont_size_range = (10, 20)
    #
    # EDGES:
    edge_width_range = (0.8, 3.0)
    #
    # LAYOUT:
    nx_k = None
    nx_iterations = 10
    nx_random_state = 0
    #
    # --------------------------------------------------------------------------

    nx_graph = create_graph_from_co_occurrence_network(
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
        # NETWORK CLUSTERING:
        algorithm_or_dict=algorithm_or_dict,
        association_index=association_index,
        #
        # LAYOUT:
        nx_k=nx_k,
        nx_iterations=nx_iterations,
        nx_random_state=nx_random_state,
        #
        # NODES:
        node_size_range=node_size_range,
        textfont_size_range=textfont_size_range,
        #
        # EDGES:
        edge_width_range=edge_width_range,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    return nx_concept_grid(
        nx_graph=nx_graph,
        conserve_counters=conserve_counters,
        n_head=n_head,
        fontsize=fontsize,
    )
