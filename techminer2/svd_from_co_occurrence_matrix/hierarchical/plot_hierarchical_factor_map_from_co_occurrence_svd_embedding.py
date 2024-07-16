# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Factor Map
===============================================================================

>>> # grey colors: https://www.w3schools.com/colors/colors_shades.asp

>>> from techminer2.tech_mining.svd.cooc_matrix.hierarchical import factor_map
>>> factor_map(
...     #
...     # PARAMS:
...     field="nlp_phrases",
...     association_index=None,
...     #
...     # ITEM PARAMS:
...     top_n=20,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_items=None,
...     #
...     # SVD PARAMS:
...     n_components=5,
...     algorithm="randomized",
...     n_iter=5,
...     n_oversamples=10,
...     power_iteration_normalizer="auto",
...     random_state=0,
...     tol=0.0,
...     #
...     # HIERARCHICAL PARAMS:
...     n_clusters=6,
...     metric=None,
...     memory=None,
...     connectivity=None,
...     compute_full_tree="auto",
...     linkage="ward",
...     distance_threshold=None,
...     #
...     # LAYOUT:
...     nx_k=None,
...     nx_iterations=30,
...     nx_random_state=0,
...     #
...     # NODES:
...     node_color="#7793a5",
...     node_size_range=(30, 70),
...     textfont_size_range=(10, 20),
...     textfont_opacity_range=(0.35, 1.00),
...     #
...     # EDGES:
...     edge_top_n=None,
...     edge_similarity_min=None,
...     edge_widths=(2, 2, 4, 6),
...     edge_colors=("#7793a5", "#7793a5", "#7793a5", "#7793a5"),
...     #
...     # AXES:
...     xaxes_range=None,
...     yaxes_range=None,
...     show_axes=False,
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... ).write_html("sphinx/_static/analyze/svd/cooc_matrix/hierarchical/factor_map.html")

.. raw:: html

    <iframe src="../../../../_static/analyze/svd/cooc_matrix/hierarchical/factor_map.html"
    height="600px" width="100%" frameBorder="0"></iframe>

"""
from typing import Literal

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

from ...correlation.correlation_map import correlation_map
from .compute_hierarchical_cluster_centers_from_co_occurrence_svd_embedding import (
    compute_hierarchical_cluster_centers_from_co_occurrence_svd_embedding,
)
from .generate_hierarchical_communities_from_co_occurrence_svd_embedding import (
    generate_hierarchical_communities_from_co_occurrence_svd_embedding,
)


def plot_hierarchical_factor_map_from_co_occurrence_svd_embedding(
    #
    # PARAMS:
    field,
    association_index=None,
    #
    # ITEM PARAMS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_items=None,
    #
    # SVD PARAMS:
    n_components=None,
    algorithm="randomized",
    n_iter=5,
    n_oversamples=10,
    power_iteration_normalizer="auto",
    random_state=0,
    tol=0.0,
    #
    # HIERARCHICAL PARAMS:
    n_clusters=None,
    metric=None,
    memory=None,
    connectivity=None,
    compute_full_tree="auto",
    linkage="ward",
    distance_threshold=None,
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
    """Auto-correlation Map.

    :meta private:
    """

    centers = compute_hierarchical_cluster_centers_from_co_occurrence_svd_embedding(
        #
        # PARAMS:
        field=field,
        association_index=association_index,
        #
        # ITEM PARAMS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        #
        # SVD PARAMS:
        n_components=n_components,
        algorithm=algorithm,
        n_iter=n_iter,
        n_oversamples=n_oversamples,
        power_iteration_normalizer=power_iteration_normalizer,
        random_state=random_state,
        tol=tol,
        #
        # HIERARCHICAL PARAMS:
        n_clusters=n_clusters,
        metric=metric,
        memory=memory,
        connectivity=connectivity,
        compute_full_tree=compute_full_tree,
        linkage=linkage,
        distance_threshold=distance_threshold,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    members = generate_hierarchical_communities_from_co_occurrence_svd_embedding(
        #
        # PARAMS:
        field=field,
        association_index=association_index,
        #
        # ITEM PARAMS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        #
        # SVD PARAMS:
        n_components=n_components,
        algorithm=algorithm,
        n_iter=n_iter,
        n_oversamples=n_oversamples,
        power_iteration_normalizer=power_iteration_normalizer,
        random_state=random_state,
        tol=tol,
        #
        # HIERARCHICAL PARAMS:
        n_clusters=n_clusters,
        metric=metric,
        memory=memory,
        connectivity=connectivity,
        compute_full_tree=compute_full_tree,
        linkage=linkage,
        distance_threshold=distance_threshold,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    names = []
    for cluster in members.columns:
        cluster_members = members[cluster].head(4).tolist()
        cluster_members = [member for member in cluster_members if member != ""]
        cluster_members = "<br>".join(cluster_members)
        names.append(cluster_members)

    similarity = pd.DataFrame(
        cosine_similarity(centers),
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
