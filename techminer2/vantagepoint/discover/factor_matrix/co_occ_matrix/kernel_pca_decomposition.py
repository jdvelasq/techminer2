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
>>> decomp = vantagepoint.discover.factor_matrix.co_occ_matrix.kernel_pca_decomposition(
...     root_dir="data/regtech/",
...     rows_and_columns='author_keywords',
...     top_n=20,
...     n_components=5,
... )
>>> decomp.df_.round(3)
                                 DIM_0  DIM_1  DIM_2  DIM_3  DIM_4
author_keywords                                                   
REGTECH 28:329                  27.114 -2.512 -0.067 -1.633  0.379
FINTECH 12:249                  11.927  5.381 -0.382  0.657 -0.995
REGULATORY_TECHNOLOGY 07:037    -2.275  0.710  6.022 -0.410  2.329
COMPLIANCE 07:030                3.563 -4.286  0.788  3.675  0.388
REGULATION 05:164                1.280  3.410  0.569  1.854 -0.744
ANTI_MONEY_LAUNDERING 05:034    -4.296 -0.963  2.453 -3.119 -0.277
FINANCIAL_SERVICES 04:168       -1.277  1.490 -2.557 -0.979  1.950
FINANCIAL_REGULATION 04:035     -2.712  0.842 -2.698 -1.279  2.822
ARTIFICIAL_INTELLIGENCE 04:023  -2.568 -0.938  1.186 -1.150 -1.847
RISK_MANAGEMENT 03:014          -1.732  1.653  1.876  1.397 -0.448
INNOVATION 03:012               -3.693  1.191 -0.367  0.089  1.115
BLOCKCHAIN 03:005               -2.548 -0.318 -0.814  0.643 -1.435
SUPTECH 03:004                  -1.127  0.720  0.470  1.011 -0.113
SEMANTIC_TECHNOLOGIES 02:041    -2.363  1.425 -0.773  0.531 -0.973
DATA_PROTECTION 02:027          -3.002  0.165 -1.579 -0.456  0.390
SMART_CONTRACTS 02:022          -3.457 -0.694 -1.231 -0.210 -0.511
CHARITYTECH 02:017              -3.436 -1.225 -0.475 -1.993 -1.398
ENGLISH_LAW 02:017              -3.436 -1.225 -0.475 -1.993 -1.398
ACCOUNTABILITY 02:014           -2.981 -2.413 -0.973  1.682  0.383
DATA_PROTECTION_OFFICER 02:014  -2.981 -2.413 -0.973  1.682  0.383

>>> decomp.cosine_similarities_
                                                              cosine_similariries
author_keywords                                                                  
REGTECH 28:329                  FINTECH 12:249 (0.860); COMPLIANCE 07:030 (0.5...
FINTECH 12:249                  REGTECH 28:329 (0.860); REGULATION 05:164 (0.6...
REGULATORY_TECHNOLOGY 07:037    RISK_MANAGEMENT 03:014 (0.635); ANTI_MONEY_LAU...
COMPLIANCE 07:030               REGTECH 28:329 (0.552); FINTECH 12:249 (0.239)...
REGULATION 05:164               FINTECH 12:249 (0.642); RISK_MANAGEMENT 03:014...
ANTI_MONEY_LAUNDERING 05:034    ARTIFICIAL_INTELLIGENCE 04:023 (0.865); CHARIT...
FINANCIAL_SERVICES 04:168       FINANCIAL_REGULATION 04:035 (0.945); DATA_PROT...
FINANCIAL_REGULATION 04:035     FINANCIAL_SERVICES 04:168 (0.945); DATA_PROTEC...
ARTIFICIAL_INTELLIGENCE 04:023  CHARITYTECH 02:017 (0.878); ENGLISH_LAW 02:017...
RISK_MANAGEMENT 03:014          SUPTECH 03:004 (0.931); REGULATORY_TECHNOLOGY ...
INNOVATION 03:012               DATA_PROTECTION 02:027 (0.877); SEMANTIC_TECHN...
BLOCKCHAIN 03:005               SMART_CONTRACTS 02:022 (0.903); SEMANTIC_TECHN...
SUPTECH 03:004                  RISK_MANAGEMENT 03:014 (0.931); SEMANTIC_TECHN...
SEMANTIC_TECHNOLOGIES 02:041    BLOCKCHAIN 03:005 (0.828); INNOVATION 03:012 (...
DATA_PROTECTION 02:027          SMART_CONTRACTS 02:022 (0.930); INNOVATION 03:...
SMART_CONTRACTS 02:022          DATA_PROTECTION 02:027 (0.930); BLOCKCHAIN 03:...
CHARITYTECH 02:017              ENGLISH_LAW 02:017 (1.000); ARTIFICIAL_INTELLI...
ENGLISH_LAW 02:017              CHARITYTECH 02:017 (1.000); ARTIFICIAL_INTELLI...
ACCOUNTABILITY 02:014           DATA_PROTECTION_OFFICER 02:014 (1.000); SMART_...
DATA_PROTECTION_OFFICER 02:014  ACCOUNTABILITY 02:014 (1.000); SMART_CONTRACTS...


>>> file_name = "sphinx/_static/vantagepoint/discover/factor_matrix/co_occ_matrix/kernel_pca_decomposition_fig.html"
>>> decomp.fig_('DIM_0', 'DIM_1').write_html(file_name)

.. raw:: html

    <iframe src="../../../../_static/vantagepoint/discover/factor_matrix/co_occ_matrix/kernel_pca_decomposition_fig.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

>>> file_name = "sphinx/_static/vantagepoint/discover/factor_matrix/co_occ_matrix/kernel_pca_decomposition_mds_map.html"
>>> decomp.MDS_().write_html(file_name)

.. raw:: html

    <iframe src="../../../../_static/vantagepoint/discover/factor_matrix/co_occ_matrix/kernel_pca_decomposition_mds_map.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

>>> file_name = "sphinx/_static/vantagepoint/discover/factor_matrix/co_occ_matrix/kernel_pca_decomposition_tsne_map.html"
>>> decomp.TSNE_().write_html(file_name)

.. raw:: html

    <iframe src="../../../../_static/vantagepoint/discover/factor_matrix/co_occ_matrix/kernel_pca_decomposition_tsne_map.html" 
    height="600px" width="100%" frameBorder="0"></iframe>


"""
import numpy as np
import pandas as pd
from sklearn.decomposition import KernelPCA

from .....analyze.co_occurrences.co_occurrence_matrix import co_occurrence_matrix
from .....normalize_co_occurrence_matrix import normalize_co_occurrence_matrix
from ..compute_cosine_similarity import compute_cosine_similarity
from ..results import Results


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
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """Creates a factor matrix from the co-occurrence matrix."""

    cooc_matrix = co_occurrence_matrix(
        #
        # FUNCTION PARAMS:
        columns=rows_and_columns,
        #
        # COLUMN PARAMS:
        col_top_n=top_n,
        col_occ_range=occ_range,
        col_gc_range=gc_range,
        col_custom_items=custom_items,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    cooc_matrix = normalize_co_occurrence_matrix(cooc_matrix, association_index)

    matrix_values = cooc_matrix.df_

    if n_components is None:
        n_components = min(min(matrix_values.shape) - 1, 100)

    estimator = KernelPCA(
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
    )

    estimator.fit(matrix_values)
    trans_matrix_values = estimator.transform(matrix_values)

    n_zeros = int(np.log10(n_components - 1)) + 1
    fmt = "DIM_{:0" + str(n_zeros) + "d}"
    columns = [fmt.format(i_component) for i_component in range(n_components)]

    matrix_values = pd.DataFrame(
        trans_matrix_values,
        index=matrix_values.index,
        columns=columns,
    )
    matrix_values.index.name = cooc_matrix.df_.index.name

    cosine_similarities = compute_cosine_similarity(matrix_values)

    return Results(
        df_=matrix_values,
        cosine_similarities_=cosine_similarities,
    )
