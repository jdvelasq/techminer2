# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Kernel PCA Factor Decomposition
===============================================================================

>>> from techminer2 import vantagepoint
>>> root_dir = "data/regtech/"
>>> factors = vantagepoint.explore.concept_grid.co_occ_matrix.kernel_pca_decomposition(
...     root_dir="data/regtech/",
...     rows_and_columns='author_keywords',
...     top_n=20,
...     n_components=5,
... )
>>> factors.centers_.round(3)
       DIM_0  DIM_1  DIM_2  DIM_3  DIM_4
CL_0  -0.076  0.330  0.060  0.251  0.206
CL_1  -2.312 -0.364 -0.182  0.172 -0.456
CL_2   7.233  2.579  1.000  4.195  2.943
CL_3  16.498  3.313  5.874  1.000  2.437
CL_4  -7.692  0.422 -4.046 -1.167  1.000

>>> print(factors.communities_.to_markdown())
|    | CL_0                         | CL_1                           | CL_2               | CL_3                   | CL_4                   |
|---:|:-----------------------------|:-------------------------------|:-------------------|:-----------------------|:-----------------------|
|  0 | REGTECH 28:329               | ANTI_MONEY_LAUNDERING 05:034   | CHARITYTECH 02:017 | SMART_CONTRACTS 02:022 | DATA_PROTECTION 02:027 |
|  1 | FINTECH 12:249               | ARTIFICIAL_INTELLIGENCE 04:023 | ENGLISH_LAW 02:017 |                        |                        |
|  2 | REGULATORY_TECHNOLOGY 07:037 | INNOVATION 03:012              |                    |                        |                        |
|  3 | COMPLIANCE 07:030            | BLOCKCHAIN 03:005              |                    |                        |                        |
|  4 | REGULATION 05:164            | SEMANTIC_TECHNOLOGIES 02:041   |                    |                        |                        |
|  5 | FINANCIAL_SERVICES 04:168    | ACCOUNTABILITY 02:014          |                    |                        |                        |
|  6 | FINANCIAL_REGULATION 04:035  | DATA_PROTECTION_OFFICER 02:014 |                    |                        |                        |
|  7 | RISK_MANAGEMENT 03:014       |                                |                    |                        |                        |
|  8 | SUPTECH 03:004               |                                |                    |                        |                        |


>>> file_name = "sphinx/_static/concept_cooc_kernel_pca_map.html"
>>> factors.fig_("DIM_0", "DIM_1").write_html(file_name)

.. raw:: html

    <iframe src="../../../../_static/concept_cooc_kernel_pca_map.html" height="600px" width="100%" frameBorder="0"></iframe>


"""
from typing import Literal

from ....discover.factor_matrix.co_occ_matrix.kernel_pca_decomposition import (
    kernel_pca_decomposition as factor_kernel_pca_decomposition,
)
from ..factor_clustering import factor_clustering


def kernel_pca_decomposition(
    #
    # COOC PARAMS:
    rows_and_columns,
    association_index=None,
    #
    # ITEM PARAMS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_items=None,
    #
    # KERNEL PCA PARAMS:
    n_components=None,
    kernel="linear",
    gamma=None,
    degree=3,
    coef0=1,
    kernel_params=None,
    alpha=1.0,
    fit_inverse_transform=False,
    eigen_solver="auto",
    tol=0,
    max_iter=None,
    iterated_power="auto",
    remove_zero_eig=False,
    random_state=0,
    #
    # KMEANS PARAMS:
    kmeans_init="k-means++",
    kmeans_n_init=10,
    kmeans_max_iter=300,
    kmeans_tol=0.0001,
    kmeans_random_state=0,
    kmeans_algorithm: Literal["lloyd", "elkan", "auto", "full"] = "auto",
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """Creates a factor matrix from the co-occurrence matrix."""

    factor_matrix = factor_kernel_pca_decomposition(
        #
        # COOC PARAMS:
        rows_and_columns=rows_and_columns,
        association_index=association_index,
        #
        # ITEM PARAMS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        #
        # KERNEL PCA PARAMS:
        n_components=n_components,
        kernel=kernel,
        gamma=gamma,
        degree=degree,
        coef0=coef0,
        kernel_params=kernel_params,
        alpha=alpha,
        fit_inverse_transform=fit_inverse_transform,
        eigen_solver=eigen_solver,
        tol=tol,
        max_iter=max_iter,
        iterated_power=iterated_power,
        remove_zero_eig=remove_zero_eig,
        random_state=random_state,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    return factor_clustering(
        factor_matrix=factor_matrix,
        #
        # KMEANS PARAMS:
        n_clusters=n_components,
        init=kmeans_init,
        n_init=kmeans_n_init,
        max_iter=kmeans_max_iter,
        tol=kmeans_tol,
        random_state=kmeans_random_state,
        algorithm=kmeans_algorithm,
    )