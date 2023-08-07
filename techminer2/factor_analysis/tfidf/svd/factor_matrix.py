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

>>> from techminer2.factor_analysis.tfidf.svd import factor_matrix
>>> matrix = factor_matrix(
...     #
...     # TF PARAMS:
...     field='author_keywords',
...     is_binary=False,
...     cooc_within=1,
...     #
...     # TF-IDF parameters:
...     norm=None,
...     use_idf=False,
...     smooth_idf=False,
...     sublinear_tf=False,
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
REGTECH 28:329                  5.128 -0.801 -0.459 -0.521 -0.030
FINTECH 12:249                  2.718  1.739 -0.241  0.251 -0.410
REGULATORY_TECHNOLOGY 07:037    0.561  0.199  2.279  0.062  0.783
COMPLIANCE 07:030               1.416 -1.386  0.283  1.350  0.296
REGULATION 05:164               1.061  1.094  0.376  0.661 -0.164
ANTI_MONEY_LAUNDERING 05:034    0.210 -0.329  1.256 -1.097 -0.158
FINANCIAL_SERVICES 04:168       0.633  0.484 -0.432 -0.564  1.009
FINANCIAL_REGULATION 04:035     0.414  0.274 -0.381 -0.706  1.396
ARTIFICIAL_INTELLIGENCE 04:023  0.468 -0.314  0.759 -0.429 -0.641
RISK_MANAGEMENT 03:014          0.595  0.521  0.844  0.553 -0.128
INNOVATION 03:012               0.268  0.379  0.254 -0.060  0.583
BLOCKCHAIN 03:005               0.439 -0.105  0.022  0.147 -0.408
SUPTECH 03:004                  0.663  0.227  0.310  0.371 -0.045
SEMANTIC_TECHNOLOGIES 02:041    0.458  0.458 -0.025  0.129 -0.316
DATA_PROTECTION 02:027          0.353  0.054 -0.214 -0.287  0.250
SMART_CONTRACTS 02:022          0.282 -0.224 -0.124 -0.172 -0.126
CHARITYTECH 02:017              0.305 -0.400  0.211 -0.800 -0.504
ENGLISH_LAW 02:017              0.305 -0.400  0.211 -0.800 -0.504
ACCOUNTABILITY 02:014           0.365 -0.779 -0.067  0.516  0.312
DATA_PROTECTION_OFFICER 02:014  0.365 -0.779 -0.067  0.516  0.312


>>> matrix.cosine_similarities_
                                                              cosine_similariries
author_keywords                                                                  
REGTECH 28:329                  SMART_CONTRACTS 02:022 (0.777); FINTECH 12:249...
FINTECH 12:249                  SEMANTIC_TECHNOLOGIES 02:041 (0.922); REGULATI...
REGULATORY_TECHNOLOGY 07:037    RISK_MANAGEMENT 03:014 (0.717); INNOVATION 03:...
COMPLIANCE 07:030               ACCOUNTABILITY 02:014 (0.924); DATA_PROTECTION...
REGULATION 05:164               SUPTECH 03:004 (0.906); SEMANTIC_TECHNOLOGIES ...
ANTI_MONEY_LAUNDERING 05:034    ARTIFICIAL_INTELLIGENCE 04:023 (0.823); CHARIT...
FINANCIAL_SERVICES 04:168       FINANCIAL_REGULATION 04:035 (0.956); DATA_PROT...
FINANCIAL_REGULATION 04:035     FINANCIAL_SERVICES 04:168 (0.956); DATA_PROTEC...
ARTIFICIAL_INTELLIGENCE 04:023  ANTI_MONEY_LAUNDERING 05:034 (0.823); CHARITYT...
RISK_MANAGEMENT 03:014          SUPTECH 03:004 (0.897); REGULATION 05:164 (0.8...
INNOVATION 03:012               FINANCIAL_SERVICES 04:168 (0.746); FINANCIAL_R...
BLOCKCHAIN 03:005               REGTECH 28:329 (0.689); SEMANTIC_TECHNOLOGIES ...
SUPTECH 03:004                  REGULATION 05:164 (0.906); RISK_MANAGEMENT 03:...
SEMANTIC_TECHNOLOGIES 02:041    FINTECH 12:249 (0.922); REGULATION 05:164 (0.8...
DATA_PROTECTION 02:027          FINANCIAL_SERVICES 04:168 (0.913); FINANCIAL_R...
SMART_CONTRACTS 02:022          REGTECH 28:329 (0.777); CHARITYTECH 02:017 (0....
CHARITYTECH 02:017              ENGLISH_LAW 02:017 (1.000); ARTIFICIAL_INTELLI...
ENGLISH_LAW 02:017              CHARITYTECH 02:017 (1.000); ARTIFICIAL_INTELLI...
ACCOUNTABILITY 02:014           DATA_PROTECTION_OFFICER 02:014 (1.000); COMPLI...
DATA_PROTECTION_OFFICER 02:014  ACCOUNTABILITY 02:014 (1.000); COMPLIANCE 07:0...

>>> matrix.fig_('DIM_0', 'DIM_1').write_html(
...     "sphinx/_static/factor_analysis/tfidf/svd/map.html"
... )

.. raw:: html

    <iframe src="../../../../_static/factor_analysis/tfidf/svd/map.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

>>> matrix.MDS_().write_html(
...     "sphinx/_static/factor_analysis/tfidf/svd/mds.html"
... )

.. raw:: html

    <iframe src="../../../../_static/factor_analysis/tfidf/svd/mds.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

>>> matrix.TSNE_().write_html(
...     "sphinx/_static/factor_analysis/tfidf/svd/tsne.html"
... )

.. raw:: html

    <iframe src="../../../../_static/factor_analysis/tfidf/svd/tsne.html" 
    height="600px" width="100%" frameBorder="0"></iframe>


"""
from typing import Literal

import numpy as np
import pandas as pd
from sklearn.decomposition import TruncatedSVD

from ....compute_cosine_similarity import compute_cosine_similarity
from ....performance_analysis.tfidf import tfidf
from ...results import Results


def factor_matrix(
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
    """Creates a factor matrix from the co-occurrence matrix.

    :meta private:
    """

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
    matrix_values.index.name = tfidf_matrix.columns.name

    cosine_similarities = compute_cosine_similarity(matrix_values)

    return Results(
        df_=matrix_values,
        cosine_similarities_=cosine_similarities,
    )
