# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Communities
===============================================================================


>>> from techminer2.agenda.network.keywords import communities
>>> communities(
...     #
...     # AGENDA PARAMS:
...     occ_range=(2, None),
...     gc_range=(None, None),
...     time_window=2,
...     growth_percentage_min=50,
...     #
...     # NETWORK PARAMS:
...     algorithm_or_dict="louvain",
...     association_index="association",
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
                                 CL_0  ...                                    CL_3
0         FINANCIAL_REGULATION 05:035  ...  CLASSIFICATION (OF_INFORMATION) 02:003
1                      SUPTECH 03:004  ...                                        
2              DATA_PROTECTION 02:027  ...                                        
3  FINANCIAL_SERVICES_INDUSTRY 02:011  ...                                        
4                   TECHNOLOGY 02:010  ...                                        
5           DIGITAL_INNOVATION 02:001  ...                                        
6                    REPORTING 02:001  ...                                        
<BLANKLINE>
[7 rows x 4 columns]



"""
from ....nx_create_co_occurrence_graph import nx_create_co_occurrence_graph
from ....nx_extract_communities_as_data_frame import nx_extract_communities_as_data_frame
from ....performance import performance_metrics

UNIT_OF_ANALYSIS = "keywords"


def communities(
    #
    # AGENDA PARAMS:
    occ_range=(None, None),
    gc_range=(None, None),
    time_window=2,
    growth_percentage_min=50,
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
    node_size_min = 30
    node_size_max = 70
    textfont_size_min = 10
    textfont_size_max = 20
    textfont_opacity_min = 0.30
    textfont_opacity_max = 1.00
    #
    # EDGES:
    edge_color = "#7793a5"
    edge_width_min = 0.8
    edge_width_max = 3.0
    #
    # LAYOUT:
    nx_k = None
    nx_iterations = 10
    nx_random_state = 0
    #
    # --------------------------------------------------------------------------

    #
    # Computes performance metrics
    metrics = performance_metrics(
        #
        # PERFORMANCE PARAMS:
        field=UNIT_OF_ANALYSIS,
        metric="OCC",
        #
        # ITEM FILTERS:
        top_n=None,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=None,
        #
        # TREND ANALYSIS:
        time_window=time_window,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    ).df_

    #
    # Selects only the items with growth rate >= growth_percentage_min
    metrics = metrics[metrics["growth_percentage"] >= growth_percentage_min]

    #
    # Obtains emergent items
    custom_items = metrics.index.tolist()

    nx_graph = nx_create_co_occurrence_graph(
        #
        # FUNCTION PARAMS:
        rows_and_columns=UNIT_OF_ANALYSIS,
        #
        # COLUMN PARAMS:
        top_n=None,
        custom_items=custom_items,
        #
        # NETWORK CLUSTERING:
        association_index=association_index,
        algorithm_or_dict=algorithm_or_dict,
        #
        # LAYOUT:
        nx_k=nx_k,
        nx_iterations=nx_iterations,
        nx_random_state=nx_random_state,
        #
        # NODES:
        node_size_min=node_size_min,
        node_size_max=node_size_max,
        textfont_size_min=textfont_size_min,
        textfont_size_max=textfont_size_max,
        textfont_opacity_min=textfont_opacity_min,
        textfont_opacity_max=textfont_opacity_max,
        #
        # EDGES:
        edge_color=edge_color,
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

    return nx_extract_communities_as_data_frame(
        #
        # FUNCTION PARAMS:
        nx_graph=nx_graph,
        conserve_counters=True,
    )
