# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Terms by Cluster Frame
===============================================================================


## >>> from techminer2.pkgs.co_occurrence_network import terms_by_cluster_frame
## >>> (
## ...     terms_by_cluster_frame()
## ...     #
## ...     # FIELD:
## ...     .with_field("author_keywords")
## ...     .having_terms_in_top(20)
## ...     .having_terms_ordered_by("OCC")
## ...     .having_term_occurrences_between(None, None)
## ...     .having_term_citations_between(None, None)
## ...     .having_terms_in(None)
## ...     #
## ...     # NETWORK:
## ...     .using_clustering_algorithm_or_dict("louvain")
## ...     .using_association_index("association")
## ...     #
## ...     # DATABASE:
## ...     .where_directory_is("example/")
## ...     .where_database_is("main")
## ...     .where_record_years_between(None, None)
## ...     .where_record_citations_between(None, None)
## ...     .where_records_match(None)
## ...     #
## ...     .build()
## ... )

                             0  ...                                3
0              FINTECH 31:5168  ...  ARTIFICIAL_INTELLIGENCE 02:0327
1  FINANCIAL_INCLUSION 03:0590  ...                  FINANCE 02:0309
2         CROWDFUNDING 03:0335  ...                   ROBOTS 02:0289
3      BUSINESS_MODELS 02:0759  ...                                 
4       CYBER_SECURITY 02:0342  ...                                 
5           CASE_STUDY 02:0340  ...                                 
6           BLOCKCHAIN 02:0305  ...                                 
7              REGTECH 02:0266  ...                                 
<BLANKLINE>
[8 rows x 4 columns]


"""
from ....internals.nx.cluster_nx_graph import internal__cluster_nx_graph
from ....internals.nx.extract_communities_to_frame import (
    internal__extract_communities_to_frame,
)
from ...co_occurrence_matrix.internals.create_co_occurrence_nx_graph import (
    _create_co_occurrence_nx_graph,
)


def terms_by_cluster_frame(
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

    nx_graph = internal__cluster_nx_graph(
        #
        # FUNCTION PARAMS:
        nx_graph=nx_graph,
        #
        # NETWORK CLUSTERING:
        algorithm_or_dict=algorithm_or_dict,
    )

    return internal__extract_communities_to_frame(
        #
        # FUNCTION PARAMS:
        nx_graph=nx_graph,
        conserve_counters=True,
    )
