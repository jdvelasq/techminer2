# flake8: noqa
"""
2D-SVD Map (*) --- ChatGPT
===============================================================================

Plots the 2D-SVD of the normalized co-occurrence. The plot is based on the
MDS technique used in T-LAB's words associations.

**Algorithm**


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
>>> # computes the SVD
>>> from techminer2 import tlab
>>> svd_map = tlab.word_associations.svd_map(norm_co_occ_matrix)
>>> file_name = "sphinx/_static/tlab__word_associations__svd_map.html"
>>> svd_map.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/tlab__word_associations__svd_map.html"
    height="800px" width="100%" frameBorder="0"></iframe>


>>> svd_map.table_.head()
                              Dim_00     Dim_01
row                                            
REGTECH 28:329             12.838699  10.370912
FINTECH 12:249             10.707965  -7.875859
COMPLIANCE 07:030           6.678769  -3.670698
REGULATION 05:164           5.799039  -0.255470
FINANCIAL_SERVICES 04:168   3.325509  -0.983070



# pylint: disable=line-too-long
"""

from ..singular_value_decomposition import singular_value_decomposition


# pylint: disable=too-many-arguments
def svd_map(
    obj,
    # SVD parameters
    algorithm="randomized",
    n_iter=5,
    n_oversamples=10,
    power_iteration_normalizer="auto",
    random_state=0,
    tol=0.0,
    # Map parameters
    node_size_min=12,
    node_size_max=50,
    textfont_size_min=8,
    textfont_size_max=20,
    xaxes_range=None,
    yaxes_range=None,
):
    """2D SVD Map."""

    return singular_value_decomposition(
        obj,
        dim_x=0,
        dim_y=1,
        # Technique parameters
        is_2d=True,
        # SVD parameters
        algorithm=algorithm,
        n_iter=n_iter,
        n_oversamples=n_oversamples,
        power_iteration_normalizer=power_iteration_normalizer,
        random_state=random_state,
        tol=tol,
        # Map parameters
        node_size_min=node_size_min,
        node_size_max=node_size_max,
        textfont_size_min=textfont_size_min,
        textfont_size_max=textfont_size_max,
        xaxes_range=xaxes_range,
        yaxes_range=yaxes_range,
    )
