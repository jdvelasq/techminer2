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

>>> from sklearn.decomposition import PCA
>>> from sklearn.cluster import KMeans
>>> from techminer2.factor_analysis.co_occurrence import terms_to_cluster_mapping
>>> mapping = terms_to_cluster_mapping(
...     #
...     # PARAMS:
...     field="author_keywords",
...     association_index=None,
...     #
...     # ITEM PARAMS:
...     top_n=20,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_terms=None,
...     #
...     # DESOMPOSITION:
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
{'ARTIFICIAL_INTELLIGENCE 02:0327': 0,
 'BANKING 02:0291': 3,
 'BLOCKCHAIN 02:0305': 1,
 'BUSINESS_MODELS 02:0759': 0,
 'CASE_STUDY 02:0340': 1,
 'CROWDFUNDING 03:0335': 1,
 'CYBER_SECURITY 02:0342': 1,
 'FINANCE 02:0309': 0,
 'FINANCIAL_INCLUSION 03:0590': 1,
 'FINANCIAL_SERVICES 04:0667': 3,
 'FINANCIAL_TECHNOLOGY 03:0461': 3,
 'FINTECH 31:5168': 4,
 'INNOVATION 07:0911': 5,
 'LENDINGCLUB 02:0253': 2,
 'MARKETPLACE_LENDING 03:0317': 2,
 'PEER_TO_PEER_LENDING 02:0253': 2,
 'REGTECH 02:0266': 0,
 'ROBOTS 02:0289': 0,
 'SHADOW_BANKING 02:0253': 2,
 'TECHNOLOGY 02:0310': 3}


"""
from .._core.terms_to_cluster_mapping import _terms_to_cluster_mapping
from .terms_by_dimension_frame import terms_by_dimension_frame


def terms_to_cluster_mapping(
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

    embedding = terms_by_dimension_frame(
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
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    mapping = _terms_to_cluster_mapping(
        terms_by_dimmension=embedding,
        clustering_estimator_or_dict=clustering_estimator_or_dict,
    )

    return mapping
