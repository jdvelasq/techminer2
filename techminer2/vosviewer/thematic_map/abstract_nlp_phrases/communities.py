# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
.. _abstract_nlp_phrases_communities:

Communities
===============================================================================


>>> from techminer2 import vosviewer
>>> root_dir = "data/regtech/"
>>> vosviewer.thematic_map.abstract_nlp_phrases.communities(
...     root_dir=root_dir,
...     top_n=20, 
... )
                                 CL_0  ...                          CL_2
0        REGULATORY_TECHNOLOGY 17:266  ...  REGULATORY_COMPLIANCE 07:198
1             FINANCIAL_SECTOR 07:169  ...   FINANCIAL_TECHNOLOGY 05:173
2         FINANCIAL_REGULATION 06:330  ...       MACHINE_LEARNING 04:007
3      GLOBAL_FINANCIAL_CRISIS 06:177  ...     DIGITAL_INNOVATION 03:164
4  FINANCIAL_SERVICES_INDUSTRY 05:315  ...                              
5       INFORMATION_TECHNOLOGY 05:177  ...                              
6            FINANCIAL_MARKETS 03:151  ...                              
7                      REGTECH 03:034  ...                              
<BLANKLINE>
[8 rows x 3 columns]


"""
from ...nx_create_co_occurrence_graph import nx_create_co_occurrence_graph
from ...nx_extract_communities_as_data_frame import nx_extract_communities_as_data_frame

FIELD = "abstract_nlp_phrases"


def communities(
    #
    # COLUMN PARAMS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_items=None,
    #
    # NETWORK PARAMS:
    algorithm_or_dict="louvain",
    #
    # LAYOUT:
    nx_k=None,
    nx_iterations=10,
    nx_random_state=0,
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
    textfont_size_min = 10
    textfont_size_max = 20

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
        # NETWORK CLUSTERING:
        algorithm_or_dict=algorithm_or_dict,
        association_index="association",
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
        #
        # EDGES:
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