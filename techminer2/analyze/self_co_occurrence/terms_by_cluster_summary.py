# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Terms by Cluster Summary
===============================================================================


## >>> from techminer2.analyze.co_occurrence_network import terms_by_cluster_summary
## >>> (
## ...     terms_by_cluster_summary(
## ...     .set_analysis_params(
## ...         algorithm_or_dict="louvain",
## ...         association_index="association",
## ...     #
## ...     ).set_format_params(
## ...         conserve_counters=False,
## ...     .set_item_params(
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
   Cluster  ...                                              Terms
0        0  ...  FINTECH; FINANCIAL_INCLUSION; CROWDFUNDING; BU...
1        1  ...  INNOVATION; FINANCIAL_SERVICES; FINANCIAL_TECH...
2        2  ...  MARKETPLACE_LENDING; LENDINGCLUB; PEER_TO_PEER...
3        3  ...           ARTIFICIAL_INTELLIGENCE; FINANCE; ROBOTS
<BLANKLINE>
[4 rows x 4 columns]



"""
from ...internals.nx.internal__cluster_graph import internal__cluster_graph
from ...internals.nx.internal__summarize_communities import (
    internal__summarize_communities,
)
from ..cross_co_occurrence.internals.create_co_occurrence_nx_graph import (
    _create_co_occurrence_nx_graph,
)


def terms_by_cluster_summary(
    #
    # PARAMS:
    field,
    #
    # SUMMARY PARAMS:
    conserve_counters=False,
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

    return internal__summarize_communities(
        #
        # SUMMARY PARAMS:
        nx_graph=nx_graph,
        conserve_counters=conserve_counters,
    )
