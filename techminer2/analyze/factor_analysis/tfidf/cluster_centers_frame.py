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
>>> from techminer2.factor_analysis.tfidf import cluster_centers_frame
>>> cluster_centers_frame(
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
dim             0         1         2         3         4
cluster                                                  
0       -0.201359 -0.145628 -0.537202 -0.307006 -0.472928
1       -0.237531 -0.943339  0.790967  0.032676 -0.003779
2       -0.203930  0.314080 -0.207809  0.815849 -0.031831
3       -0.254730  1.080850  0.568245 -0.299478 -0.064949
4       -0.474124  0.044653 -0.408102 -0.313095  0.858150
5        4.959197 -0.131331 -0.127054 -0.021353  0.127476


"""
from .terms_by_dimension_frame import terms_by_dimension_frame
from .terms_to_cluster_mapping import terms_to_cluster_mapping


def cluster_centers_frame(
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

    embedding = terms_by_dimension_frame(
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
