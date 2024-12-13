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

>>> from sklearn.decomposition import PCA
>>> from sklearn.cluster import KMeans
>>> from techminer2.factor_analysis.tfidf import cluster_to_terms_mapping
>>> mapping = cluster_to_terms_mapping(
...     #
...     # PARAMS:
...     field="author_keywords",
...     #
...     # TF PARAMS:
...     is_binary=True,
...     cooc_within=1,
...     #
...     # TF-IDF PARAMS:
...     norm=None,
...     use_idf=False,
...     smooth_idf=False,
...     sublinear_tf=False,
...     #
...     # TERM PARAMS:
...     top_n=20,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_terms=None,
...     #
...     # DESOMPOSITION PARAMS:
...     decomposition_estimator = PCA(
...         n_components=5,
...         whiten=False,
...         svd_solver="auto",
...         tol=0.0,
...         iterated_power="auto",
...         n_oversamples=10,
...         power_iteration_normalizer="auto",
...         random_state=0, 
...     ),
...     #
...     # CLUSTERING:
...     clustering_estimator_or_dict = KMeans(
...         n_clusters=6,
...         init="k-means++",
...         n_init=10,
...         max_iter=300,
...         tol=0.0001,
...         algorithm="elkan",
...         random_state=0,
...     ),
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> from pprint import pprint
>>> pprint(mapping)
{0: ['FINANCIAL_INCLUSION 03:0590',
     'CROWDFUNDING 03:0335',
     'CYBER_SECURITY 02:0342',
     'CASE_STUDY 02:0340',
     'BLOCKCHAIN 02:0305'],
 1: ['MARKETPLACE_LENDING 03:0317',
     'LENDINGCLUB 02:0253',
     'PEER_TO_PEER_LENDING 02:0253',
     'SHADOW_BANKING 02:0253'],
 2: ['FINANCIAL_SERVICES 04:0667',
     'FINANCIAL_TECHNOLOGY 03:0461',
     'BUSINESS_MODELS 02:0759',
     'REGTECH 02:0266'],
 3: ['INNOVATION 07:0911', 'TECHNOLOGY 02:0310', 'BANKING 02:0291'],
 4: ['ARTIFICIAL_INTELLIGENCE 02:0327', 'FINANCE 02:0309', 'ROBOTS 02:0289'],
 5: ['FINTECH 31:5168']}

"""
from .terms_to_cluster_mapping import terms_to_cluster_mapping


def cluster_to_terms_mapping(
    #
    # PARAMS:
    field,
    #
    # TF PARAMS:
    is_binary: bool = True,
    cooc_within: int = 1,
    #
    # TERM PARAMS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_terms=None,
    #
    # TF-IDF parameters:
    norm=None,
    use_idf=False,
    smooth_idf=False,
    sublinear_tf=False,
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
        #
        # TF PARAMS:
        is_binary=is_binary,
        cooc_within=cooc_within,
        #
        # TERM PARAMS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_terms=custom_terms,
        #
        # TF-IDF parameters:
        norm=norm,
        use_idf=use_idf,
        smooth_idf=smooth_idf,
        sublinear_tf=sublinear_tf,
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
