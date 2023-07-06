# flake8: noqa
# pylint: disable=line-too-long
"""
.. _factor_matrix_pca:

Factor Matrix PCA
===============================================================================

Factor matrix obtained by appliying PCA to the co-occurrence matrix. 

**Algorithm:**

1. Computes the co-occurrence matrix of the specified field.

2. Optionally, normalize the co-occurrence matrix.

3. Applies PCA (or another technique) to the co-occurrence matrix.

4. Returns the factor matrix.




* Preparation

>>> import techminer2plus as tm2p
>>> root_dir = "data/regtech/"


* Object oriented interface

>>> (
...     tm2p.records(root_dir=root_dir)
...     .co_occurrence_matrix(
...         columns='author_keywords',
...         col_top_n=20,
...     )
...     .factor_matrix_pca()
... )
FactorMatrix(cooc_matrix='CoocMatrix(columns='author_keywords',
    rows='author_keywords', dims=(20, 20))', estimator=PCA(random_state=0),
    shape=(20, 20))

* Functional interface

>>> cooc_matrix = tm2p.co_occurrence_matrix(
...     root_dir="data/regtech/",
...     columns='author_keywords',
...     col_top_n=20,
... )
>>> factor_matrix = tm2p.factor_matrix_pca(
...     cooc_matrix,
... )
>>> factor_matrix
FactorMatrix(cooc_matrix='CoocMatrix(columns='author_keywords',
    rows='author_keywords', dims=(20, 20))', estimator=PCA(random_state=0),
    shape=(20, 20))

    
* Results:

>>> factor_matrix.df_.round(3)
component                       DIM_00  DIM_01  DIM_02  ...  DIM_17  DIM_18  DIM_19
explained_variance             53.8582 4.8660  3.6888   ... 0.0000  0.0000  0.0000 
explained_variance_ratio        0.7569  0.0684  0.0518  ...  0.0000  0.0000  0.0000
author_keywords                                         ...                        
REGTECH 28:329                  27.114  -2.512  -0.067  ...     0.0     0.0     0.0
FINTECH 12:249                  11.927   5.381  -0.382  ...     0.0    -0.0     0.0
REGULATORY_TECHNOLOGY 07:037    -2.275   0.710   6.022  ...     0.0    -0.0    -0.0
COMPLIANCE 07:030                3.563  -4.286   0.788  ...     0.0    -0.0     0.0
REGULATION 05:164                1.280   3.410   0.569  ...     0.0     0.0    -0.0
ANTI_MONEY_LAUNDERING 05:034    -4.296  -0.963   2.453  ...    -0.0    -0.0    -0.0
FINANCIAL_SERVICES 04:168       -1.277   1.490  -2.557  ...    -0.0     0.0    -0.0
FINANCIAL_REGULATION 04:035     -2.712   0.842  -2.698  ...    -0.0     0.0    -0.0
ARTIFICIAL_INTELLIGENCE 04:023  -2.568  -0.938   1.186  ...    -0.0    -0.0     0.0
RISK_MANAGEMENT 03:014          -1.732   1.653   1.876  ...    -0.0    -0.0    -0.0
INNOVATION 03:012               -3.693   1.191  -0.367  ...     0.0    -0.0     0.0
BLOCKCHAIN 03:005               -2.548  -0.318  -0.814  ...    -0.0     0.0     0.0
SUPTECH 03:004                  -1.127   0.720   0.470  ...     0.0    -0.0     0.0
SEMANTIC_TECHNOLOGIES 02:041    -2.363   1.425  -0.773  ...    -0.0    -0.0     0.0
DATA_PROTECTION 02:027          -3.002   0.165  -1.579  ...     0.0     0.0     0.0
SMART_CONTRACTS 02:022          -3.457  -0.694  -1.231  ...     0.0    -0.0     0.0
CHARITYTECH 02:017              -3.436  -1.225  -0.475  ...    -0.0    -0.0     0.0
ENGLISH_LAW 02:017              -3.436  -1.225  -0.475  ...    -0.0    -0.0     0.0
ACCOUNTABILITY 02:014           -2.981  -2.413  -0.973  ...    -0.0     0.0    -0.0
DATA_PROTECTION_OFFICER 02:014  -2.981  -2.413  -0.973  ...    -0.0     0.0    -0.0
<BLANKLINE>
[20 rows x 20 columns]



"""
import textwrap
from dataclasses import dataclass
from typing import Literal

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA

from .matrix_normalization import matrix_normalization


@dataclass
class FactorMatrix:
    """Factor matrix."""

    #
    # FUNCTION PARAMS:
    cooc_matrix_repr: str
    estimator_repr: str
    #
    # RESULTS:
    df_: pd.DataFrame
    explained_variance_: np.ndarray
    explained_variance_ratio_: np.ndarray

    def __repr__(self):
        text = "FactorMatrix("
        text += f"cooc_matrix='{self.cooc_matrix_repr}'"
        text += f", estimator={self.estimator_repr}"
        text += f", shape={self.df_.shape}"
        text += ")"
        text = textwrap.fill(text, width=75, subsequent_indent="    ")
        return text


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def factor_matrix_pca(
    #
    # FUNCTION PARAMS:
    cooc_matrix_or_tfidf,
    association_index=None,
    #
    # PCA PARAMS:
    n_components=None,
    whiten=False,
    svd_solver="auto",
    tol=0.0,
    iterated_power="auto",
    n_oversamples=10,
    power_iteration_normalizer="auto",
    random_state=0,
):
    """Creates a factor matrix from the co-occurrence matrix.


    # pylint: disable=line-too-long
    """

    if repr(cooc_matrix_or_tfidf)[:5] == "TFIDF":
        matrix = cooc_matrix_or_tfidf.df_.T
    else:
        cooc_matrix_or_tfidf = matrix_normalization(
            cooc_matrix_or_tfidf, association_index
        )
        matrix = cooc_matrix_or_tfidf.df_

    if n_components is None:
        n_components = min(min(matrix.shape) - 1, 100)

    estimator = PCA(
        n_components=n_components,
        whiten=whiten,
        svd_solver=svd_solver,
        tol=tol,
        iterated_power=iterated_power,
        n_oversamples=n_oversamples,
        power_iteration_normalizer=power_iteration_normalizer,
        random_state=random_state,
    )

    estimator.fit(matrix)
    transformed_matrix = estimator.transform(matrix)

    columns = [
        (f"DIM_{i_component:>02d}", round(ev, 4), round(evratio, 4))
        for i_component, (ev, evratio) in enumerate(
            zip(
                estimator.explained_variance_,
                estimator.explained_variance_ratio_,
            )
        )
    ]
    columns = pd.MultiIndex.from_tuples(
        columns,
        names=["component", "explained_variance", "explained_variance_ratio"],
    )

    ## columns = [f"DIM_{i:>02d}" for i in range(transformed_matrix.shape[1])]

    matrix = pd.DataFrame(
        transformed_matrix,
        index=matrix.index,
        columns=columns,
    )
    matrix.index.name = cooc_matrix_or_tfidf.rows

    return FactorMatrix(
        cooc_matrix_repr=repr(cooc_matrix_or_tfidf)
        .replace("\n", "")
        .replace("    ", "   ")
        .replace("   ", "  ")
        .replace("  ", " "),
        estimator_repr=repr(estimator),
        #
        # RESULTS:
        df_=matrix,
        explained_variance_=estimator.explained_variance_,
        explained_variance_ratio_=(estimator.explained_variance_ratio_),
    )
