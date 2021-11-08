"""
Similarity matrix --- bubble map
===============================================================================
"""

from sklearn.manifold import MDS

from ._bubble_map import bubble_map

#
# 4q
# clusters
# cmap


def similarity_matrix_bubble_map(
    similarity_matrix,
    clusters,
    mainfold=None,
    color_scheme="4q",
    figsize=(6, 6),
):

    if mainfold is None:
        mainfold = MDS(n_components=2)

    matrix = mainfold.fit_transform(similarity_matrix)
    node_x = matrix[:, 0]
    node_y = matrix[:, 1]
    node_texts = similarity_matrix.index.get_level_values(0)
    node_sizes = similarity_matrix.index.get_level_values(1)

    return bubble_map(
        node_x=node_x,
        node_y=node_y,
        node_clusters=clusters,
        node_texts=node_texts,
        node_sizes=node_sizes,
        x_axis_at=0,
        y_axis_at=0,
        color_scheme=color_scheme,
        xlabel="Dim-0",
        ylabel="Dim-1",
        figsize=figsize,
    )
