# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Terms by Cluster Summary
===============================================================================

## >>> from sklearn.cluster import KMeans
## >>> from techminer2.analyze.document_clustering import terms_by_cluster_summary
## >>> (   
## ...     TermsByClusterSummary()
## ...     #
## ...     # FIELD:
## ...     .with_field("descriptors")
## ...     .having_terms_in_top(50)
## ...     .having_terms_ordered_by("OCC")
## ...     .having_term_occurrences_between(None, None)
## ...     .having_term_citations_between(None, None)
## ...     .having_terms_in(None)
## ...     #
## ...     # COUNTERS:
## ...     .using_term_counters(True)


## ...     .set_analysis_params(
## ...         sklearn_estimator=KMeans(
## ...             n_clusters=4,
## ...             init="k-means++",
## ...             n_init=10,
## ...             max_iter=300,
## ...             tol=0.0001,
## ...             algorithm="lloyd",
## ...             random_state=0,
## ...         ),


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
   Cluster  ...                                              Terms
0        0  ...  INNOVATION 08:0990; FINANCIAL_SERVICES_INDUSTR...
1        1  ...  FINANCIAL_SERVICE 04:1036; NEW_TECHNOLOGIES 02...
2        2  ...                      DISRUPTIVE_INNOVATION 02:0759
3        3  ...  FINTECH 32:5393; FINANCIAL_TECHNOLOGY 18:2519;...
<BLANKLINE>
[4 rows x 4 columns]


"""
import pandas as pd  # type: ignore

from .clusters_to_terms_mapping import clusters_to_terms_mapping


def terms_by_cluster_summary(
    #
    # TF PARAMS:
    field,
    retain_counters=True,
    is_binary: bool = False,
    cooc_within: int = 1,
    #
    # FILTER PARAMS:
    top_n=20,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_terms=None,
    #
    # ESIIMATOR:
    sklearn_estimator=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    sort_by=None,
    **filters,
):
    """:meta private:"""

    mapping = clusters_to_terms_mapping(
        #
        # TF PARAMS:
        field=field,
        retain_counters=retain_counters,
        is_binary=is_binary,
        cooc_within=cooc_within,
        #
        # FILTER PARAMS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_terms=custom_terms,
        #
        # ESIIMATOR:
        sklearn_estimator=sklearn_estimator,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        sort_by=sort_by,
        **filters,
    )

    clusters = sorted(mapping.keys())
    n_terms = [len(mapping[label]) for label in clusters]
    terms = ["; ".join(mapping[label]) for label in clusters]
    percentage = [round(n_term / sum(n_terms) * 100, 1) for n_term in n_terms]

    summary = pd.DataFrame(
        {
            "Cluster": clusters,
            "Num Terms": n_terms,
            "Percentage": percentage,
            "Terms": terms,
        }
    )

    return summary
