# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Terms to Cluster Mapping
===============================================================================


## >>> from techminer2.analyze.co_occurrence_network import terms_to_clusters_mapping
## >>> mapping = terms_to_clusters_mapping(
## ...     .set_analysis_params(
## ...         algorithm_or_dict="louvain",
## ...         association_index="association",
## ...     ).set_format_params(
## ...         retain_counters=True,
## ...     #
## ...     ).set_item_params(
## ...         field="author_keywords",
## ...         top_n=20,
## ...         occ_range=(None, None),
## ...         gc_range=(None, None),
## ...         custom_terms=None,
## ...     #
## ...     ).set_database_params(
## ...         root_dir="example/", 
## ...         database="main",
## ...         year_filter=(None, None),
## ...         cited_by_filter=(None, None),
## ...     #
## ...     ).build()
## ... )
## >>> from pprint import pprint
## >>> pprint(mapping)
{'ARTIFICIAL_INTELLIGENCE 02:0327': 3,
 'BANKING 02:0291': 1,
 'BLOCKCHAIN 02:0305': 0,
 'BUSINESS_MODELS 02:0759': 0,
 'CASE_STUDY 02:0340': 0,
 'CROWDFUNDING 03:0335': 0,
 'CYBER_SECURITY 02:0342': 0,
 'FINANCE 02:0309': 3,
 'FINANCIAL_INCLUSION 03:0590': 0,
 'FINANCIAL_SERVICES 04:0667': 1,
 'FINANCIAL_TECHNOLOGY 03:0461': 1,
 'FINTECH 31:5168': 0,
 'INNOVATION 07:0911': 1,
 'LENDINGCLUB 02:0253': 2,
 'MARKETPLACE_LENDING 03:0317': 2,
 'PEER_TO_PEER_LENDING 02:0253': 2,
 'REGTECH 02:0266': 0,
 'ROBOTS 02:0289': 3,
 'SHADOW_BANKING 02:0253': 2,
 'TECHNOLOGY 02:0310': 1}



"""
from ...internals.nx.internal__cluster_graph import internal__cluster_graph
from ...internals.nx.internal__terms_to_clusters_mapping import (
    internal__terms_to_clusters_mapping,
)
from ..cross_co_occurrence.internals.create_co_occurrence_nx_graph import (
    _create_co_occurrence_nx_graph,
)


def terms_to_clusters_mapping(
    #
    # PARAMS:
    field,
    retain_counters=True,
    #
    # COLUMN PARAMS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_terms=None,
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
    """:meta private:"""

    nx_graph = _create_co_occurrence_nx_graph(
        #
        # FUNCTION PARAMS:
        rows_and_columns=field,
        #
        # COLUMN PARAMS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_terms=custom_terms,
        #
        # NETWORK PARAMS:
        association_index=association_index,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    nx_graph = internal__cluster_graph(
        #
        # FUNCTION PARAMS:
        nx_graph=nx_graph,
        #
        # NETWORK CLUSTERING:
        algorithm_or_dict=algorithm_or_dict,
    )

    mapping = internal__terms_to_clusters_mapping(
        #
        # FUNCTION PARAMS:
        nx_graph=nx_graph,
        retain_counters=retain_counters,
    )

    return mapping
