# flake8: noqa
# pylint: disable=line-too-long
"""
.. _factor_decomposition_svd:

Factor Decomposition SVD
===============================================================================

Factor matrix obtained by appliying SVD to the co-occurrence matrix. 

**Algorithm:**

1. Computes the co-occurrence matrix of the specified field.

2. Optionally, normalize the co-occurrence matrix.

3. Applies SVD (or another technique) to the co-occurrence matrix.

4. Returns the factor matrix.




* Preparation

>>> import techminer2 as tm2
>>> root_dir = "data/regtech/"


* Object oriented interface

>>> (
...     tm2p.records(root_dir=root_dir)
...     .co_occurrence_matrix(
...         columns='author_keywords',
...         col_top_n=20,
...     )
...     .factor_decomposition_svd()
... )
FactorMatrix(cooc_matrix='CoocMatrix(columns='author_keywords',
    rows='author_keywords', dims=(20, 20))',
    estimator=TruncatedSVD(n_components=19, random_state=0), shape=(20,
    19))

* Functional interface

>>> cooc_matrix = tm2p.co_occurrence_matrix(
...     root_dir="data/regtech/",
...     columns='author_keywords',
...     col_top_n=20,
... )
>>> factor_matrix = tm2p.factor_decomposition_svd(
...     cooc_matrix,
... )
>>> factor_matrix
FactorMatrix(cooc_matrix='CoocMatrix(columns='author_keywords',
    rows='author_keywords', dims=(20, 20))',
    estimator=TruncatedSVD(n_components=19, random_state=0), shape=(20,
    19))

    
* Results:

>>> factor_matrix.df_.round(3)
                                DIM_000  DIM_001  ...  DIM_017  DIM_018
author_keywords                                   ...                  
REGTECH 28:329                   32.386   -2.485  ...    0.017      0.0
FINTECH 12:249                   17.168    5.393  ...   -0.006      0.0
REGULATORY_TECHNOLOGY 07:037      3.545    0.616  ...   -0.062      0.0
COMPLIANCE 07:030                 8.944   -4.299  ...   -0.026      0.0
REGULATION 05:164                 6.700    3.392  ...   -0.149      0.0
ANTI_MONEY_LAUNDERING 05:034      1.327   -1.020  ...    0.042      0.0
FINANCIAL_SERVICES 04:168         3.996    1.500  ...    0.086     -0.0
FINANCIAL_REGULATION 04:035       2.615    0.848  ...   -0.100     -0.0
ARTIFICIAL_INTELLIGENCE 04:023    2.957   -0.974  ...   -0.103     -0.0
RISK_MANAGEMENT 03:014            3.757    1.615  ...    0.235     -0.0
INNOVATION 03:012                 1.692    1.174  ...    0.115     -0.0
BLOCKCHAIN 03:005                 2.774   -0.325  ...    0.138     -0.0
SUPTECH 03:004                    4.187    0.704  ...   -0.015     -0.0
SEMANTIC_TECHNOLOGIES 02:041      2.892    1.421  ...   -0.068      0.0
DATA_PROTECTION 02:027            2.232    0.167  ...    0.045     -0.0
SMART_CONTRACTS 02:022            1.783   -0.695  ...   -0.108      0.0
CHARITYTECH 02:017                1.924   -1.240  ...    0.007     -0.0
ENGLISH_LAW 02:017                1.924   -1.240  ...    0.007     -0.0
ACCOUNTABILITY 02:014             2.303   -2.416  ...    0.005      0.0
DATA_PROTECTION_OFFICER 02:014    2.303   -2.416  ...    0.005      0.0
<BLANKLINE>
[20 rows x 19 columns]


"""
import textwrap
from dataclasses import dataclass
from typing import Literal

import numpy as np
import pandas as pd
from sklearn.decomposition import TruncatedSVD

from .factor_decomposition_2d_map import factor_decomposition_2d_map
from .vantagepoint.analyze.discover.matrix.matrix_normalization import (
    matrix_normalization,
)


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

    def __repr__(self):
        text = "FactorMatrix("
        text += f"cooc_matrix='{self.cooc_matrix_repr}'"
        text += f", estimator={self.estimator_repr}"
        text += f", shape={self.df_.shape}"
        text += ")"
        text = textwrap.fill(text, width=75, subsequent_indent="    ")
        return text

    def factor_decomposition_2d_map(
        self,
        #
        # Plot params:
        dim_x=0,
        dim_y=1,
        node_color="#556f81",
        node_size_min=12,
        node_size_max=50,
        textfont_size_min=8,
        textfont_size_max=20,
        xaxes_range=None,
        yaxes_range=None,
    ):
        return factor_decomposition_2d_map(
            factor_matrix=self,
            #
            # Plot params:
            dim_x=dim_x,
            dim_y=dim_y,
            node_color=node_color,
            node_size_min=node_size_min,
            node_size_max=node_size_max,
            textfont_size_min=textfont_size_min,
            textfont_size_max=textfont_size_max,
            xaxes_range=xaxes_range,
            yaxes_range=yaxes_range,
        )


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def factor_decomposition_svd(
    #
    # FUNCTION PARAMS:
    cooc_matrix_or_tfidf,
    association_index=None,
    #
    # SVD PARAMS:
    n_components=None,
    algorithm="randomized",
    n_iter=5,
    n_oversamples=10,
    power_iteration_normalizer="auto",
    random_state=0,
    tol=0.0,
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

    estimator = TruncatedSVD(
        n_components=n_components,
        algorithm=algorithm,
        n_iter=n_iter,
        n_oversamples=n_oversamples,
        power_iteration_normalizer=power_iteration_normalizer,
        random_state=random_state,
        tol=tol,
    )

    estimator.fit(matrix)
    transformed_matrix = estimator.transform(matrix)

    columns = [
        f"DIM_{i_component:>03d}" for i_component in range(n_components)
    ]

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
    )
