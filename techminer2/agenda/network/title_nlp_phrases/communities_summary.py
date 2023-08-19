# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Communities Summary
===============================================================================


>>> from techminer2.agenda.network.title_nlp_phrases import communities_summary
>>> communities_summary(
...     #
...     # AGENDA PARAMS:
...     occ_range=(1, None),
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
   Cluster  ...                                              Terms
0    CL_00  ...  CHARITABLE_ORGANISATIONS; MACHINE_LEARNING; RE...
1    CL_01  ...                    FINTECH_SUSTAINABILITY; REGTECH
2    CL_02  ...        CONSUMER_COMPLAINTS; REGULATORY_ENFORCEMENT
3    CL_03  ...                 FIRM_PERFORMANCE; REGTECH_ADOPTION
4    CL_04  ...                              FINANCIAL_DEVELOPMENT
5    CL_05  ...                                    ISLAMIC_FINANCE
6    CL_06  ...                                    PRIVATE_SECTORS
7    CL_07  ...                                  IMAGINARY_FAILURE
8    CL_08  ...                               REGTECH_DEVELOPMENTS
9    CL_09  ...                         REGTECH_POTENTIAL_BENEFITS
10   CL_10  ...                                     REGTECH_S_RISE
11   CL_11  ...                        SMART_REGULATORY_COMPLIANCE
<BLANKLINE>
[12 rows x 4 columns]



"""
from ....nx_communities_summary import nx_communities_summary
from ....nx_create_co_occurrence_graph import nx_create_co_occurrence_graph
from ....performance import performance_metrics

UNIT_OF_ANALYSIS = "title_nlp_phrases"


def communities_summary(
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

    return nx_communities_summary(
        #
        # SUMMARY PARAMS:
        nx_graph=nx_graph,
        conserve_counters=False,
    )
