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


## >>> from techminer2.analyze.co_occurrence_network import NetworkMetrics
## >>> (
## ...     NetworkMetrics()
## ...     .set_analysis_params(
## ...         association_index="association",
## ...     #
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
## ... ).head()
                            Degree  Betweenness  Closeness  PageRank
FINTECH 31:5168                 18     0.761793   0.950000  0.240341
FINANCIAL_SERVICES 04:0667       7     0.056725   0.612903  0.065863
INNOVATION 07:0911               6     0.036452   0.593750  0.083155
FINANCE 02:0309                  5     0.015984   0.575758  0.038939
TECHNOLOGY 02:0310               5     0.028655   0.575758  0.042338


"""
from ....internals.nx.internal__compute_network_metrics import (
    internal__compute_network_metrics,
)
from ...co_occurrence_matrix.internals.create_co_occurrence_nx_graph import (
    _create_co_occurrence_nx_graph,
)


def network_metrics(
    #
    # PARAMS:
    field,
    #
    # COLUMN PARAMS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_terms=None,
    #
    # NETWORK PARAMS:
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

    return internal__compute_network_metrics(
        #
        # FUNCTION PARAMS:
        nx_graph=nx_graph,
    )
