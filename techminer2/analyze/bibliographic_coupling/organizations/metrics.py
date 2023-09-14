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


>>> from techminer2.network.bibliographic_coupling.organizations import metrics
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
                                                    Degree  ...  PageRank
Politec di Milano (ITA)                                 16  ...  0.056480
Kingston Bus Sch (GBR)                                  10  ...  0.024360
European Central B (DEU)                                 9  ...  0.082172
Harvard Univ Weatherhead ctr for International ...       9  ...  0.082172
KS Strategic, London, United Kingdom (GBR)               9  ...  0.082172
Panepistemio Aigaiou, Chios, Greece (GRC)                9  ...  0.082172
Sch of Eng (CHE)                                         9  ...  0.082172
Univ Coll Cork (IRL)                                     9  ...  0.021974
Ahlia Univ (BHR)                                         8  ...  0.019753
Dublin City Univ (IRL)                                   8  ...  0.028294
Univ of Hong Kong (HKG)                                  8  ...  0.071777
Heinrich-Heine-Univ (DEU)                                5  ...  0.056674
UNSW Sydney, Kensington, Australia (AUS)                 5  ...  0.056674
Univ of Luxembourg (LUX)                                 5  ...  0.056674
Univ of Zurich (CHE)                                     5  ...  0.056674
FinTech HK, Hong Kong (HKG)                              3  ...  0.020537
ctr for Law, Markets & Regulation, UNSW Austral...       3  ...  0.020537
Coventry Univ (GBR)                                      2  ...  0.049365
Univ of Westminster (GBR)                                2  ...  0.049365
<BLANKLINE>
[19 rows x 4 columns]



"""
from ....nx_compute_metrics import nx_compute_metrics
from ....nx_create_bibliographic_coupling_graph import nx_create_bibliographic_coupling_graph

UNIT_OF_ANALYSIS = "organizations"


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
