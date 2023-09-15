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


>>> from techminer2.analyze.bibliographic_coupling.countries import metrics
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
Italy                     17     0.066615   1.000000  0.115188
Germany                   16     0.021272   0.944444  0.107878
Luxembourg                16     0.021272   0.944444  0.043972
United Kingdom            16     0.021272   0.944444  0.104464
Bahrain                   15     0.007546   0.894737  0.037805
Ireland                   15     0.007546   0.894737  0.052082
Jordan                    15     0.007546   0.894737  0.029672
Malaysia                  15     0.007546   0.894737  0.031769
Switzerland               15     0.042023   0.894737  0.102429
United Arab Emirates      15     0.007546   0.894737  0.042778
United States             14     0.028298   0.850000  0.096350
Australia                 13     0.008578   0.809524  0.044504
China                     13     0.002941   0.809524  0.046904
Greece                    12     0.000000   0.772727  0.052907
Japan                     11     0.000000   0.739130  0.037619
South Africa              11     0.000000   0.739130  0.016777
Hong Kong                  6     0.000000   0.607143  0.025606
Spain                      3     0.000000   0.548387  0.011296



"""
from ....nx_compute_metrics import nx_compute_metrics
from ....nx_create_bibliographic_coupling_graph import nx_create_bibliographic_coupling_graph

UNIT_OF_ANALYSIS = "countries"


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
