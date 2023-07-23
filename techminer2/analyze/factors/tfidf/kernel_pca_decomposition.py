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
>>> decomp = vantagepoint.discover.factor_matrix.tfidf.kernel_pca_decomposition(
...     root_dir="data/regtech/",
...     field='author_keywords',
...     top_n=20,
...     n_components=5,
... )
>>> decomp.df_.round(3)
                                DIM_0  DIM_1  DIM_2  DIM_3  DIM_4
author_keywords                                                  
REGTECH 28:329                  4.375 -0.811  0.010 -0.644  0.207
FINTECH 12:249                  1.981  1.735  0.008  0.214 -0.406
REGULATORY_TECHNOLOGY 07:037   -0.598  0.233  1.933 -0.397  1.078
COMPLIANCE 07:030               0.563 -1.382  0.451  1.332  0.123
REGULATION 05:164               0.152  1.100  0.238  0.682 -0.363
ANTI_MONEY_LAUNDERING 05:034   -0.829 -0.309  0.606 -1.248 -0.069
FINANCIAL_SERVICES 04:168      -0.151  0.479 -0.975 -0.202  0.768
FINANCIAL_REGULATION 04:035    -0.451  0.271 -1.130 -0.261  1.105
ARTIFICIAL_INTELLIGENCE 04:023 -0.511 -0.301  0.275 -0.457 -0.813
RISK_MANAGEMENT 03:014         -0.348  0.534  0.682  0.436 -0.186
INNOVATION 03:012              -0.598  0.384 -0.165  0.075  0.457
BLOCKCHAIN 03:005              -0.389 -0.103 -0.249  0.276 -0.649
SUPTECH 03:004                 -0.123  0.232  0.299  0.307  0.008
SEMANTIC_TECHNOLOGIES 02:041   -0.292  0.459 -0.154  0.190 -0.388
DATA_PROTECTION 02:027         -0.381  0.052 -0.500 -0.122  0.188
SMART_CONTRACTS 02:022         -0.458 -0.225 -0.353 -0.059 -0.189
CHARITYTECH 02:017             -0.539 -0.395 -0.246 -0.731 -0.575
ENGLISH_LAW 02:017             -0.539 -0.395 -0.246 -0.731 -0.575
ACCOUNTABILITY 02:014          -0.432 -0.779 -0.241  0.669  0.139
DATA_PROTECTION_OFFICER 02:014 -0.432 -0.779 -0.241  0.669  0.139


>>> decomp.cosine_similarities_
                                                              cosine_similariries
author_keywords                                                                  
REGTECH 28:329                  FINTECH 12:249 (0.585); COMPLIANCE 07:030 (0.2...
FINTECH 12:249                  REGULATION 05:164 (0.682); REGTECH 28:329 (0.5...
REGULATORY_TECHNOLOGY 07:037    ANTI_MONEY_LAUNDERING 05:034 (0.523); RISK_MAN...
COMPLIANCE 07:030               ACCOUNTABILITY 02:014 (0.693); DATA_PROTECTION...
REGULATION 05:164               SUPTECH 03:004 (0.745); RISK_MANAGEMENT 03:014...
ANTI_MONEY_LAUNDERING 05:034    CHARITYTECH 02:017 (0.711); ENGLISH_LAW 02:017...
FINANCIAL_SERVICES 04:168       FINANCIAL_REGULATION 04:035 (0.964); DATA_PROT...
FINANCIAL_REGULATION 04:035     FINANCIAL_SERVICES 04:168 (0.964); DATA_PROTEC...
ARTIFICIAL_INTELLIGENCE 04:023  CHARITYTECH 02:017 (0.846); ENGLISH_LAW 02:017...
RISK_MANAGEMENT 03:014          SUPTECH 03:004 (0.956); REGULATION 05:164 (0.7...
INNOVATION 03:012               FINANCIAL_REGULATION 04:035 (0.717); DATA_PROT...
BLOCKCHAIN 03:005               SMART_CONTRACTS 02:022 (0.715); SEMANTIC_TECHN...
SUPTECH 03:004                  RISK_MANAGEMENT 03:014 (0.956); REGULATION 05:...
SEMANTIC_TECHNOLOGIES 02:041    REGULATION 05:164 (0.710); BLOCKCHAIN 03:005 (...
DATA_PROTECTION 02:027          FINANCIAL_REGULATION 04:035 (0.877); FINANCIAL...
SMART_CONTRACTS 02:022          CHARITYTECH 02:017 (0.752); ENGLISH_LAW 02:017...
CHARITYTECH 02:017              ENGLISH_LAW 02:017 (1.000); ARTIFICIAL_INTELLI...
ENGLISH_LAW 02:017              CHARITYTECH 02:017 (1.000); ARTIFICIAL_INTELLI...
ACCOUNTABILITY 02:014           DATA_PROTECTION_OFFICER 02:014 (1.000); COMPLI...
DATA_PROTECTION_OFFICER 02:014  ACCOUNTABILITY 02:014 (1.000); COMPLIANCE 07:0...

>>> file_name = "sphinx/_static/vantagepoint/discover/factor_matrix/tfidf/kernel_pca_decomposition_fig.html"
>>> decomp.fig_('DIM_0', 'DIM_1').write_html(file_name)

.. raw:: html

    <iframe src="../../../../_static/vantagepoint/discover/factor_matrix/tfidf/kernel_pca_decomposition_fig.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

>>> file_name = "sphinx/_static/vantagepoint/discover/factor_matrix/tfidf/kernel_pca_decomposition_mds_map.html"
>>> decomp.MDS_().write_html(file_name)

.. raw:: html

    <iframe src="../../../../_static/vantagepoint/discover/factor_matrix/tfidf/kernel_pca_decomposition_mds_map.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

>>> file_name = "sphinx/_static/vantagepoint/discover/factor_matrix/tfidf/kernel_pca_decomposition_tnse_map.html"
>>> decomp.TSNE_().write_html(file_name)

.. raw:: html

    <iframe src="../../../../_static/vantagepoint/discover/factor_matrix/tfidf/kernel_pca_decomposition_tnse_map.html"
    height="600px" width="100%" frameBorder="0"></iframe>
    

"""
from typing import Literal

import numpy as np
import pandas as pd
from sklearn.decomposition import KernelPCA

from ....performance_analysis.tfidf import tfidf
from ..compute_cosine_similarity import compute_cosine_similarity
from ..results import Results


def kernel_pca_decomposition(
    #
    # TF PARAMS:
    field: str,
    is_binary: bool = False,
    cooc_within: int = 1,
    #
    # TF-IDF parameters:
    norm: Literal["l1", "l2", None] = None,
    use_idf=False,
    smooth_idf=False,
    sublinear_tf=False,
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

    tfidf_matrix = tfidf(
        #
        # TF PARAMS:
        field=field,
        is_binary=is_binary,
        cooc_within=cooc_within,
        #
        # ITEM FILTERS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        #
        # TF-IDF parameters:
        norm=norm,
        use_idf=use_idf,
        smooth_idf=smooth_idf,
        sublinear_tf=sublinear_tf,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    matrix_values = tfidf_matrix.T

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
    matrix_values.index.name = tfidf_matrix.columns.name

    cosine_similarities = compute_cosine_similarity(matrix_values)

    return Results(
        df_=matrix_values,
        cosine_similarities_=cosine_similarities,
    )
