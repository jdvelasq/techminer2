# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Cluster to Terms Mapping
===============================================================================

## >>> from sklearn.decomposition import PCA
## >>> from sklearn.cluster import KMeans
## >>> from techminer2.analyze.factor_analysis.co_occurrence import cluster_to_terms_mapping
## >>> mapping = (
## ...     ClusterToTermsMapping()
## ...     .set_analysis_params(
## ...         association_index=None,
## ...         decomposition_estimator = PCA(
## ...             n_components=5,
## ...             whiten=False,
## ...             svd_solver="auto",
## ...             tol=0.0,
## ...             iterated_power="auto",
## ...             n_oversamples=10,
## ...             power_iteration_normalizer="auto",
## ...             random_state=0, 
## ...         ),
## ...         clustering_estimator_or_dict = KMeans(
## ...             n_clusters=6,
## ...             init="k-means++",
## ...             n_init=10,
## ...             max_iter=300,
## ...             tol=0.0001,
## ...             algorithm="elkan",
## ...             random_state=0,
## ...         ),
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
{0: ['BUSINESS_MODELS 02:0759',
     'ARTIFICIAL_INTELLIGENCE 02:0327',
     'FINANCE 02:0309',
     'ROBOTS 02:0289',
     'REGTECH 02:0266'],
 1: ['FINANCIAL_INCLUSION 03:0590',
     'CROWDFUNDING 03:0335',
     'CYBER_SECURITY 02:0342',
     'CASE_STUDY 02:0340',
     'BLOCKCHAIN 02:0305'],
 2: ['MARKETPLACE_LENDING 03:0317',
     'LENDINGCLUB 02:0253',
     'PEER_TO_PEER_LENDING 02:0253',
     'SHADOW_BANKING 02:0253'],
 3: ['FINANCIAL_SERVICES 04:0667',
     'FINANCIAL_TECHNOLOGY 03:0461',
     'TECHNOLOGY 02:0310',
     'BANKING 02:0291'],
 4: ['FINTECH 31:5168'],
 5: ['INNOVATION 07:0911']}

"""
from .terms_to_cluster_mapping import terms_to_cluster_mapping


def cluster_to_terms_mapping(
    #
    # PARAMS:
    field,
    association_index=None,
    #
    # TERM PARAMS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_terms=None,
    #
    # DECOMPOSITION:
    decomposition_estimator=None,
    #
    # CLUSTERING:
    clustering_estimator_or_dict=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """:meta private:"""

    t2c_mapping = terms_to_cluster_mapping(
        #
        # FUNCTION PARAMS:
        field=field,
        association_index=association_index,
        #
        # TERM PARAMS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_terms=custom_terms,
        #
        # DECOMPOSITION:
        decomposition_estimator=decomposition_estimator,
        #
        # CLUSTERING:
        clustering_estimator_or_dict=clustering_estimator_or_dict,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    mapping = {}
    for term, cluster in t2c_mapping.items():
        if cluster not in mapping:
            mapping[cluster] = []
        mapping[cluster].append(term)

    return mapping
