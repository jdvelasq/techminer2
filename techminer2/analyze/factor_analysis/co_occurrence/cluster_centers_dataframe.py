# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Cluster Centers Frame
===============================================================================

>>> from sklearn.decomposition import PCA
>>> from sklearn.cluster import KMeans
>>> from techminer2.analyze.factor_analysis.co_occurrence import cluster_centers_frame
>>> (
...     ClusterCentersDataFrame()
...     .set_analysis_params(
...         association_index=None,
...         decomposition_estimator = PCA(
...             n_components=5,
...             whiten=False,
...             svd_solver="auto",
...             tol=0.0,
...             iterated_power="auto",
...             n_oversamples=10,
...             power_iteration_normalizer="auto",
...             random_state=0, 
...         ),
...         clustering_estimator_or_dict = KMeans(
...             n_clusters=6,
...             init="k-means++",
...             n_init=10,
...             max_iter=300,
...             tol=0.0001,
...             algorithm="elkan",
...             random_state=0,
...         ),
...     #
...     ).set_item_params(
...         field="author_keywords",
...         top_n=20,
...         occ_range=(None, None),
...         gc_range=(None, None),
...         custom_terms=None,
...     #
...     ).set_database_params(
...         root_dir="example/", 
...         database="main",
...         year_filter=(None, None),
...         cited_by_filter=(None, None),
...     #
...     ).build()
... )
dim              0         1         2         3         4
cluster                                                   
0        -2.295491  0.081013 -1.030189  0.325448  1.224114
1        -1.497389 -0.514843 -1.479097 -0.659790 -0.908773
2        -1.169941 -2.758694  2.169137  0.055023 -0.042967
3        -1.848206  1.992721  0.417640  0.670726 -0.381834
4        28.659528 -0.524730 -0.513789 -0.042977  0.238539
5         2.377465  5.757771  2.713115 -1.188306 -0.116040

"""
from .terms_by_dimension_dataframe import terms_by_dimension_frame
from .terms_to_cluster_mapping import terms_to_cluster_mapping


def cluster_centers_frame(
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

    n_clusters = len(set(t2c_mapping.values()))
    embedding = embedding.iloc[:, :n_clusters]
    embedding["cluster"] = embedding.index.map(t2c_mapping)
    embedding = embedding.groupby("cluster").mean()

    return embedding
