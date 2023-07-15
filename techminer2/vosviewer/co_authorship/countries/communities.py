# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
.. _countries_communities:

Communities
===============================================================================


>>> from techminer2 import vosviewer
>>> root_dir = "data/regtech/"
>>> vosviewer.co_authorship.countries.communities(
...     root_dir=root_dir,
...     top_n=20, 
... )
                   CL_0              CL_1  ...           CL_6            CL_7
0  United Kingdom 7:199   Australia 7:199  ...  Ukraine 1:004  Malaysia 1:003
1   United States 6:059       China 5:027  ...                               
2         Ireland 5:055   Hong Kong 3:185  ...                               
3           Italy 5:005  Luxembourg 2:034  ...                               
4         Germany 4:051       Japan 1:013  ...                               
5     Switzerland 4:045                    ...                               
6          Greece 1:021                    ...                               
<BLANKLINE>
[7 rows x 8 columns]


"""
from ...create_co_occurrence_nx_graph import create_co_occurrence_nx_graph
from ...get_network_communities import get_network_communities

FIELD = "countries"


def communities(
    #
    # COLUMN PARAMS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_items=None,
    #
    # NETWORK PARAMS:
    algorithm_or_estimator="louvain",
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

    nx_graph = create_co_occurrence_nx_graph(
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
        # NETWORK PARAMS:
        algorithm_or_estimator=algorithm_or_estimator,
        normalization_index=None,
        color=color,
        nx_k=nx_k,
        nx_iterations=nx_iterations,
        nx_random_state=nx_random_state,
        node_size_min=node_size_min,
        node_size_max=node_size_max,
        textfont_size_min=textfont_size_min,
        textfont_size_max=textfont_size_max,
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

    return get_network_communities(
        #
        # FUNCTION PARAMS:
        nx_graph=nx_graph,
    )
