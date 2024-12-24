# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Factor Map
===============================================================================

>>> from sklearn.decomposition import PCA
>>> from sklearn.cluster import KMeans
>>> from techminer2.analyze.factor_analysis.co_occurrence import factor_map
>>> plot = (
...     FactorMap()
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
...         #
...         # CLUSTERING:
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
...     ).set_nx_params(
...         nx_k=None,
...         nx_iterations=30,
...         nx_random_state=0,
...     #
...     ).set_layout_params(
...         node_color="#7793a5",
...         node_size_range=(30, 70),
...         textfont_size_range=(10, 20),
...         textfont_opacity_range=(0.35, 1.00),
...         edge_top_n=None,
...         edge_similarity_min=None,
...         edge_widths=(2, 2, 4, 6),
...         edge_colors=("#7793a5", "#7793a5", "#7793a5", "#7793a5"),
...     #
...     ).set_axes_params(
...         xaxes_range=None,
...         yaxes_range=None,
...         show_axes=False,
...     #
...     ).set_database_params(
...         root_dir="example/", 
...         database="main",
...         year_filter=(None, None),
...         cited_by_filter=(None, None),
...     #
...     ).build()
... )
>>> # plot.write_html("sphinx/_static/factor_analysis/co_occurrence/factor_map.html")

.. raw:: html

    <iframe src="../../_static/factor_analysis/co_occurrence/factor_map.html" 
    height="600px" width="100%" frameBorder="0"></iframe>



"""
import pandas as pd  # type: ignore
from sklearn.metrics.pairwise import cosine_similarity  # type: ignore

from ...correlation_matrix.internals.correlation_map import correlation_map
from .cluster_centers_dataframe import cluster_centers_frame
from .cluster_to_terms_mapping import cluster_to_terms_mapping


def factor_map(
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
    # LAYOUT:
    nx_k=None,
    nx_iterations=30,
    nx_random_state=0,
    #
    # NODES:
    node_color="#7793a5",
    node_size_range=(30, 70),
    textfont_size_range=(10, 20),
    textfont_opacity_range=(0.35, 1.00),
    #
    # EDGES:
    edge_top_n=None,
    edge_similarity_min=None,
    edge_widths=(2, 2, 4, 6),
    edge_colors=("#7793a5", "#7793a5", "#7793a5", "#7793a5"),
    #
    # AXES:
    xaxes_range=None,
    yaxes_range=None,
    show_axes=False,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """:meta private:"""

    cluster_centers = cluster_centers_frame(
        #
        # PARAMS:
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

    mapping = cluster_to_terms_mapping(
        #
        # PARAMS:
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

    mapping = {key: "<br>".join(items[:4]) for key, items in mapping.items()}
    names = [mapping[key] for key in sorted(mapping.keys())]

    similarity = pd.DataFrame(
        cosine_similarity(cluster_centers),
        index=names,
        columns=names,
    )

    return correlation_map(
        similarity=similarity,
        #
        # LAYOUT:
        nx_k=nx_k,
        nx_iterations=nx_iterations,
        nx_random_state=nx_random_state,
        #
        # NODES:
        node_color=node_color,
        node_size_range=node_size_range,
        textfont_size_range=textfont_size_range,
        textfont_opacity_range=textfont_opacity_range,
        #
        # EDGES:
        edge_top_n=edge_top_n,
        edge_similarity_min=edge_similarity_min,
        edge_widths=edge_widths,
        edge_colors=edge_colors,
        #
        # AXES:
        xaxes_range=xaxes_range,
        yaxes_range=yaxes_range,
        show_axes=show_axes,
    )
