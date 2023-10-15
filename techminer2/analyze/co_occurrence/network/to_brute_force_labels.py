# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
To Brute Force Labels
===============================================================================


>>> from techminer2.analyze.co_occurrence.network import to_brute_force_labels
>>> brute_force_labels = to_brute_force_labels(
...     #
...     # PARAMS:
...     field='author_keywords',
...     #
...     # COLUMN PARAMS:
...     top_n=20,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_items=None,
...     #
...     # NETWORK PARAMS:
...     algorithm_or_dict="louvain",
...     association_index="association",
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> from pprint import pprint
>>> pprint(brute_force_labels)
{'ARTIFICIAL_INTELLIGENCE 02:0327': 0,
 'BANKING 03:0375': 1,
 'BLOCKCHAIN 03:0369': 0,
 'BUSINESS 03:0896': 2,
 'CASE_STUDIES 03:0442': 0,
 'CROWDFUNDING 03:0335': 0,
 'CYBER_SECURITY 02:0342': 0,
 'DIGITALIZATION 03:0434': 1,
 'FINANCIAL_INCLUSION 03:0590': 0,
 'FINANCIAL_INSTITUTION 02:0484': 1,
 'FINANCIAL_SERVICES 04:0667': 2,
 'FINANCIAL_TECHNOLOGY 04:0551': 2,
 'FINTECH 31:5168': 0,
 'FUTURE_RESEARCH 02:0691': 2,
 'INNOVATION 07:0911': 1,
 'MARKETPLACE_LENDING 03:0317': 3,
 'MOBILE_FINTECH_PAYMENT_SERVICES 04:0485': 0,
 'PEER_TO_PEER_LENDING 03:0324': 3,
 'SHADOW_BANKING 03:0643': 3,
 'TECHNOLOGIES 02:0310': 1}

>>> from techminer2.analyze.co_occurrence.network import communities
>>> print(communities(
...     #
...     # PARAMS:
...     field='author_keywords',
...     #
...     # COLUMN PARAMS:
...     top_n=20,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_items=None,
...     #
...     # NETWORK PARAMS:
...     algorithm_or_dict=brute_force_labels,
...     association_index="association",
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... ).to_markdown())
|    | CL_0                                    | CL_1                          | CL_2                         | CL_3                         |
|---:|:----------------------------------------|:------------------------------|:-----------------------------|:-----------------------------|
|  0 | FINTECH 31:5168                         | INNOVATION 07:0911            | FINANCIAL_SERVICES 04:0667   | SHADOW_BANKING 03:0643       |
|  1 | MOBILE_FINTECH_PAYMENT_SERVICES 04:0485 | DIGITALIZATION 03:0434        | FINANCIAL_TECHNOLOGY 04:0551 | PEER_TO_PEER_LENDING 03:0324 |
|  2 | FINANCIAL_INCLUSION 03:0590             | BANKING 03:0375               | BUSINESS 03:0896             | MARKETPLACE_LENDING 03:0317  |
|  3 | CASE_STUDIES 03:0442                    | FINANCIAL_INSTITUTION 02:0484 | FUTURE_RESEARCH 02:0691      |                              |
|  4 | BLOCKCHAIN 03:0369                      | TECHNOLOGIES 02:0310          |                              |                              |
|  5 | CROWDFUNDING 03:0335                    |                               |                              |                              |
|  6 | CYBER_SECURITY 02:0342                  |                               |                              |                              |
|  7 | ARTIFICIAL_INTELLIGENCE 02:0327         |                               |                              |                              |



"""
from ...._common.nx_create_co_occurrence_graph import nx_create_co_occurrence_graph
from ...._common.nx_extract_communities_as_data_frame import (
    nx_extract_communities_as_data_frame,
)


def to_brute_force_labels(
    #
    # PARAMS:
    field,
    #
    # COLUMN PARAMS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_items=None,
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
    node_size_range = (30, 70)
    textfont_size_range = (10, 20)
    #
    # EDGES:
    edge_width_range = (0.8, 3.0)
    #
    # LAYOUT:
    nx_k = None
    nx_iterations = 10
    nx_random_state = 0
    #
    # --------------------------------------------------------------------------

    nx_graph = nx_create_co_occurrence_graph(
        #
        # FUNCTION PARAMS:
        rows_and_columns=field,
        #
        # COLUMN PARAMS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        #
        # NETWORK CLUSTERING:
        algorithm_or_dict=algorithm_or_dict,
        association_index=association_index,
        #
        # LAYOUT:
        nx_k=nx_k,
        nx_iterations=nx_iterations,
        nx_random_state=nx_random_state,
        #
        # NODES:
        node_size_range=node_size_range,
        textfont_size_range=textfont_size_range,
        #
        # EDGES:
        edge_width_range=edge_width_range,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    data_frame = nx_extract_communities_as_data_frame(
        #
        # FUNCTION PARAMS:
        nx_graph=nx_graph,
        conserve_counters=True,
    )

    member2group = {}
    for i_col, col in enumerate(data_frame.columns):
        terms = data_frame[col].to_list()
        terms = [term for term in terms if term != ""]
        # terms = [" ".join(term.split(" ")[:-1]) for term in terms]
        for term in terms:
            member2group[term] = i_col

    return member2group
