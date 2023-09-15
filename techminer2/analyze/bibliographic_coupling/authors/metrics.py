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


>>> from techminer2.analyze.bibliographic_coupling.authors import metrics
>>> metrics(
...     #
...     # COLUMN PARAMS:
...     top_n=20, 
...     citations_min=0,
...     documents_min=2,
...     custom_items=None,
...     #
...     # NETWORK PARAMS:
...     algorithm_or_dict="louvain",
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
                   Degree  Betweenness  Closeness  PageRank
Grassi L               15     0.253190   0.818182  0.132104
Lanfranchi D           15     0.253190   0.818182  0.132104
Breymann W              9     0.044818   0.642857  0.022192
Brennan R               8     0.000000   0.562500  0.072379
Crane M                 8     0.000000   0.562500  0.072379
Hamdan A                8     0.000000   0.562500  0.028881
Ryan P                  8     0.000000   0.562500  0.072379
Sarea A                 8     0.000000   0.562500  0.028881
Turki M                 8     0.000000   0.562500  0.028881
Anagnostopoulos I       7     0.245565   0.620690  0.027620
Arner DW                7     0.036259   0.600000  0.060146
Buckley RP              7     0.036259   0.600000  0.060146
Weber RH                5     0.000000   0.529412  0.047361
Zetzsche DA             5     0.000000   0.529412  0.047361
Barberis JN             3     0.000000   0.428571  0.018552
Lin W                   3     0.000000   0.486486  0.043228
Singh C                 3     0.000000   0.486486  0.043228
Butler T                2     0.111111   0.409091  0.034649
OBrien L                1     0.000000   0.295082  0.027529



"""
from ....nx_compute_metrics import nx_compute_metrics
from ....nx_create_bibliographic_coupling_graph import nx_create_bibliographic_coupling_graph

UNIT_OF_ANALYSIS = "authors"


def metrics(
    #
    # COLUMN PARAMS:
    top_n=None,
    citations_min=0,
    documents_min=2,
    custom_items=None,
    #
    # NETWORK PARAMS:
    algorithm_or_dict="louvain",
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
    # NODES:
    node_size_min = 30
    node_size_max = 70
    textfont_size_min = 10
    textfont_size_max = 20
    textfont_opacity_min = 0.35
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

    nx_graph = nx_create_bibliographic_coupling_graph(
        #
        # FUNCTION PARAMS:
        unit_of_analysis=UNIT_OF_ANALYSIS,
        #
        # COLUMN PARAMS:
        top_n=top_n,
        citations_min=citations_min,
        documents_min=documents_min,
        custom_items=custom_items,
        #
        # NETWORK CLUSTERING:
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

    return nx_compute_metrics(
        #
        # FUNCTION PARAMS:
        nx_graph=nx_graph,
    )
