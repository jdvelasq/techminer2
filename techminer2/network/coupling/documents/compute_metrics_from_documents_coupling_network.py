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


>>> from techminer2.science_mapping.bibliographic_coupling.documents import metrics
>>> metrics(
...     #
...     # ARTICLE PARAMS:
...     top_n=20, 
...     citations_threshold=0,
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
Anagnostopoulos I., 2018, J ECON BUS 1:202       7  ...  0.108354
Gomber P., 2017, J BUS ECON 1:489                7  ...  0.172423
Gomber P., 2018, J MANAGE INF SYST 1:576         5  ...  0.102747
Hu Z., 2019, SYMMETRY 1:176                      4  ...  0.101092
Ryu H.-S., 2018, IND MANAGE DATA SYS 1:161       4  ...  0.089072
<BLANKLINE>
[5 rows x 4 columns]



"""
from ....core.network.nx_compute_metrics import nx_compute_metrics
from ....core.network.nx_create_bibliographic_coupling_graph_for_documents import (
    nx_create_bibliographic_coupling_graph_for_documents,
)


def compute_metrics_from_documents_coupling_network(
    #
    # ARTICLE PARAMS:
    top_n=None,
    citations_threshold=0,
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
    #
    # --------------------------------------------------------------------------

    nx_graph = nx_create_bibliographic_coupling_graph_for_documents(
        #
        # COLUMN PARAMS:
        top_n=top_n,
        citations_threshold=citations_threshold,
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
