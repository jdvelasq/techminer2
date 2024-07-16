# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Metrics
===============================================================================


>>> from techminer2.science_mapping.co_authorship.network.organizations import metrics
>>> metrics(
...     #
...     # COLUMN PARAMS:
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
... ).head()
                                            Degree  ...  PageRank
Goethe Univ. of Frankfurt (DEU) 1:576            3  ...  0.067114
Pennsylvania State Univ. (USA) 1:576             3  ...  0.067114
Singapore Manag. Univ. (SMU) (SGP) 1:576         3  ...  0.067114
Univ. of Delaware (USA) 1:576                    3  ...  0.067114
Columbia Graduate Sch. of Bus. (USA) 1:390       2  ...  0.067114
<BLANKLINE>
[5 rows x 4 columns]

"""
from ....core.network.nx_compute_metrics import nx_compute_metrics
from ....core.network.co_occurrence_network.create_graph_from_co_occurrence_network import (
    create_graph_from_co_occurrence_network,
)

FIELD = "organizations"


def compute_metrics_from_organizations_co_occurrence_network(
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
        rows_and_columns=FIELD,
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

    return nx_compute_metrics(
        #
        # FUNCTION PARAMS:
        nx_graph=nx_graph,
    )
