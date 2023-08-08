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


>>> from techminer2.bibliographic_coupling.sources import metrics
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
INTELL SYST ACCOUNT FINANCE M       8     0.227273   0.666667  0.136659
J FINANC CRIME                      8     0.227273   0.666667  0.171511
HELIYON                             7     0.060606   0.631579  0.108737
J RISK FINANC                       6     0.409091   0.666667  0.098537
J ANTITRUST ENFORC                  5     0.000000   0.571429  0.077062
J FINANCIAL DATA SCI                5     0.000000   0.571429  0.064969
FINANCIAL INNOV                     4     0.000000   0.480000  0.053444
J BANK REGUL                        4     0.000000   0.480000  0.053444
J ECON BUS                          3     0.318182   0.480000  0.083187
ICEIS - PROC INT CONF ENTERP        1     0.000000   0.413793  0.022098
J MONEY LAUND CONTROL               1     0.000000   0.413793  0.060133
J RISK MANG FINANCIAL INST          1     0.000000   0.333333  0.035109
NORTHWEST J INTL LAW BUS            1     0.000000   0.333333  0.035109



"""
from ...nx_compute_metrics import nx_compute_metrics
from ...nx_create_bibliographic_coupling_graph import nx_create_bibliographic_coupling_graph

UNIT_OF_ANALYSIS = "source_abbr"


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
