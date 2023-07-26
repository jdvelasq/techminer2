# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Factor Matrix
===============================================================================

>>> from techminer2.factor_analysis.co_occurrences.svd import factor_matrix
>>> matrix = factor_matrix(
...     #
...     # COOC PARAMS:
...     rows_and_columns='author_keywords',
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
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> matrix.df_.round(3)
                                 DIM_0  DIM_1  DIM_2  DIM_3  DIM_4
author_keywords                                                   
REGTECH 28:329                  32.386 -2.485 -1.392 -1.399 -0.071
FINTECH 12:249                  17.168  5.393 -0.732  0.675 -0.980
REGULATORY_TECHNOLOGY 07:037     3.545  0.616  6.915  0.165  1.871
COMPLIANCE 07:030                8.944 -4.299  0.859  3.624  0.706
REGULATION 05:164                6.700  3.392  1.139  1.775 -0.391
ANTI_MONEY_LAUNDERING 05:034     1.327 -1.020  3.811 -2.947 -0.378
FINANCIAL_SERVICES 04:168        3.996  1.500 -1.309 -1.515  2.409
FINANCIAL_REGULATION 04:035      2.615  0.848 -1.156 -1.895  3.335
ARTIFICIAL_INTELLIGENCE 04:023   2.957 -0.974  2.301 -1.151 -1.531
RISK_MANAGEMENT 03:014           3.757  1.615  2.561  1.484 -0.306
INNOVATION 03:012                1.692  1.174  0.770 -0.161  1.392
BLOCKCHAIN 03:005                2.774 -0.325  0.065  0.395 -0.975
SUPTECH 03:004                   4.187  0.704  0.940  0.998 -0.108
SEMANTIC_TECHNOLOGIES 02:041     2.892  1.421 -0.076  0.347 -0.755
DATA_PROTECTION 02:027           2.232  0.167 -0.649 -0.771  0.597
SMART_CONTRACTS 02:022           1.783 -0.695 -0.377 -0.461 -0.302
CHARITYTECH 02:017               1.924 -1.240  0.640 -2.148 -1.203
ENGLISH_LAW 02:017               1.924 -1.240  0.640 -2.148 -1.203
ACCOUNTABILITY 02:014            2.303 -2.416 -0.205  1.386  0.745
DATA_PROTECTION_OFFICER 02:014   2.303 -2.416 -0.205  1.386  0.745

>>> matrix.cosine_similarities_
                                                              cosine_similariries
author_keywords                                                                  
REGTECH 28:329                  BLOCKCHAIN 03:005 (0.927); FINTECH 12:249 (0.9...
FINTECH 12:249                  SEMANTIC_TECHNOLOGIES 02:041 (0.971); REGULATI...
REGULATORY_TECHNOLOGY 07:037    RISK_MANAGEMENT 03:014 (0.782); ANTI_MONEY_LAU...
COMPLIANCE 07:030               ACCOUNTABILITY 02:014 (0.926); DATA_PROTECTION...
REGULATION 05:164               SEMANTIC_TECHNOLOGIES 02:041 (0.962); SUPTECH ...
ANTI_MONEY_LAUNDERING 05:034    ARTIFICIAL_INTELLIGENCE 04:023 (0.799); CHARIT...
FINANCIAL_SERVICES 04:168       DATA_PROTECTION 02:027 (0.944); FINANCIAL_REGU...
FINANCIAL_REGULATION 04:035     FINANCIAL_SERVICES 04:168 (0.938); DATA_PROTEC...
ARTIFICIAL_INTELLIGENCE 04:023  CHARITYTECH 02:017 (0.858); ENGLISH_LAW 02:017...
RISK_MANAGEMENT 03:014          SUPTECH 03:004 (0.921); REGULATION 05:164 (0.9...
INNOVATION 03:012               FINANCIAL_SERVICES 04:168 (0.805); REGULATION ...
BLOCKCHAIN 03:005               REGTECH 28:329 (0.927); SUPTECH 03:004 (0.897)...
SUPTECH 03:004                  REGULATION 05:164 (0.956); FINTECH 12:249 (0.9...
SEMANTIC_TECHNOLOGIES 02:041    FINTECH 12:249 (0.971); REGULATION 05:164 (0.9...
DATA_PROTECTION 02:027          FINANCIAL_SERVICES 04:168 (0.944); REGTECH 28:...
SMART_CONTRACTS 02:022          REGTECH 28:329 (0.920); BLOCKCHAIN 03:005 (0.8...
CHARITYTECH 02:017              ENGLISH_LAW 02:017 (1.000); ARTIFICIAL_INTELLI...
ENGLISH_LAW 02:017              CHARITYTECH 02:017 (1.000); ARTIFICIAL_INTELLI...
ACCOUNTABILITY 02:014           DATA_PROTECTION_OFFICER 02:014 (1.000); COMPLI...
DATA_PROTECTION_OFFICER 02:014  ACCOUNTABILITY 02:014 (1.000); COMPLIANCE 07:0...

>>> matrix.fig_('DIM_0', 'DIM_1').write_html(
...     "sphinx/_static/factor_analysis/co_occurrences/svd/map.html"
... )

.. raw:: html

    <iframe src="../../../../_static/factor_analysis/co_occurrences/svd/map.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

>>> matrix.MDS_().write_html(
...     "sphinx/_static/factor_analysis/co_occurrences/svd/mds.html"
... )

.. raw:: html

    <iframe src="../../../../_static/factor_analysis/co_occurrences/svd/mds.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

>>> matrix.TSNE_().write_html(
...     "sphinx/_static/factor_analysis/co_occurrences/svd/tsne.html"
... )

.. raw:: html

    <iframe src="../../../../_static/factor_analysis/co_occurrences/svd/tsne.html" 
    height="600px" width="100%" frameBorder="0"></iframe>


"""
import numpy as np
import pandas as pd
from sklearn.decomposition import TruncatedSVD

from ....co_occurrence_analysis.co_occurrence_matrix import co_occurrence_matrix
from ....normalize_co_occurrence_matrix import normalize_co_occurrence_matrix
from ...compute_cosine_similarity import compute_cosine_similarity
from ...results import Results


def factor_matrix(
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
    # SVD PARAMS:
    n_components=None,
    algorithm="randomized",
    n_iter=5,
    n_oversamples=10,
    power_iteration_normalizer="auto",
    random_state=0,
    tol=0.0,
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

    estimator = TruncatedSVD(
        n_components=n_components,
        algorithm=algorithm,
        n_iter=n_iter,
        n_oversamples=n_oversamples,
        power_iteration_normalizer=power_iteration_normalizer,
        random_state=random_state,
        tol=tol,
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
