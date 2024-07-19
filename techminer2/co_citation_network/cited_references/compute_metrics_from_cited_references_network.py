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


>>> from techminer2.science_mapping.co_citation.cited_references import metrics
>>> metrics(
...     #
...     # COLUMN PARAMS:
...     top_n=30, 
...     citations_threshold=None,
...     custom_terms=None,
...     #
...     # NETWORK PARAMS:
...     algorithm_or_dict="louvain",
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... ).head()
                                                Degree  ...  PageRank
Burtch G., 2013, INF SYST RES 1:4                   15  ...  0.049734
Lin M., 2013, MANAGE SCI 1:7                        15  ...  0.050008
Dahlberg T., 2008, ELECT COMMER RES APPL 1:3        14  ...  0.046468
Burtch G., 2014, MIS QUART MANAGE INF SYST 1:4      12  ...  0.040113
Belleflamme P., 2014, J BUS VENTURING 1:3           11  ...  0.037319
<BLANKLINE>
[5 rows x 4 columns]

"""
from ..._core.nx.nx_compute_metrics import nx_compute_metrics
from ..._core.nx.nx_create_co_citation_graph import nx_create_co_citation_graph

UNIT_OF_ANALYSIS = "cited_references"


def compute_metrics_from_cited_references_network(
    #
    # COLUMN PARAMS:
    top_n=None,
    citations_threshold=None,
    custom_terms=None,
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
    # NODES:
    node_size_range = (30, 70)
    textfont_size_range = (10, 20)
    textfont_opacity_range = (0.35, 1.00)
    #
    # EDGES:
    edge_color = "#7793a5"
    edge_width_range = (0.8, 3.0)
    #
    # LAYOUT:
    nx_k = None
    nx_iterations = 10
    nx_random_state = 0
    # --------------------------------------------------------------------------

    nx_graph = nx_create_co_citation_graph(
        #
        # FUNCTION PARAMS:
        unit_of_analysis=UNIT_OF_ANALYSIS,
        #
        # COLUMN PARAMS:
        top_n=top_n,
        citations_threshold=citations_threshold,
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
        node_size_range=node_size_range,
        textfont_size_range=textfont_size_range,
        textfont_opacity_range=textfont_opacity_range,
        #
        # EDGES:
        edge_color=edge_color,
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
