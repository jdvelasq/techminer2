# flake8: noqa
"""
2D-MDS Map --- ChatGPT
===============================================================================

Plots the 2D-MDS of the normalized co-occurrence. The plot is based on the
MDS technique used in T-LAB's words associations.



>>> root_dir = "data/regtech/"
>>> # ------------------------- Algorithm -------------------------
>>> # computes the co-occurrence matrix
>>> from techminer2 import vantagepoint
>>> co_occ_matrix = vantagepoint.analyze.co_occ_matrix(
...     columns='author_keywords',
...     col_top_n=20,
...     root_dir=root_dir,
... )
>>> # normalizes the co-occurrence matrix
>>> norm_co_occ_matrix = vantagepoint.analyze.association_index(
...     co_occ_matrix, "mutualinfo"
... )
>>> # computes the MDS
>>> from techminer2 import tlab
>>> mds_map = tlab.word_associations.mds_map(norm_co_occ_matrix)
>>> file_name = "sphinx/_static/tlab__word_associations__mds_map.html"
>>> mds_map.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/tlab__word_associations__mds_map.html"
    height="800px" width="100%" frameBorder="0"></iframe>


>>> mds_map.table_.head()
                              Dim_00    Dim_01
row                                           
REGTECH 28:329            -10.779058  9.743817
FINTECH 12:249             -6.773880 -8.215191
COMPLIANCE 07:030          -3.922014 -3.169216
REGULATION 05:164          -3.313712  0.581496
FINANCIAL_SERVICES 04:168   0.070459  1.912509




# pylint: disable=line-too-long
"""

# from ..comparison.multidimensional_scaling import multidimensional_scaling


# pylint: disable=too-many-arguments
def mds_map(
    obj,
    # MDS parameters
    metric=True,
    n_init=4,
    max_iter=300,
    eps=0.001,
    n_jobs=None,
    random_state=0,
    dissimilarity="euclidean",
    # Map parameters
    node_size_min=12,
    node_size_max=50,
    textfont_size_min=8,
    textfont_size_max=20,
    xaxes_range=None,
    yaxes_range=None,
):
    """2D SVD Map."""

    return multidimensional_scaling(
        obj,
        dim_x=0,
        dim_y=1,
        # Technique parameters
        is_2d=True,
        # MDS parameters
        metric=metric,
        n_init=n_init,
        max_iter=max_iter,
        eps=eps,
        n_jobs=n_jobs,
        random_state=random_state,
        dissimilarity=dissimilarity,
        # Map parameters
        node_size_min=node_size_min,
        node_size_max=node_size_max,
        textfont_size_min=textfont_size_min,
        textfont_size_max=textfont_size_max,
        xaxes_range=xaxes_range,
        yaxes_range=yaxes_range,
    )
