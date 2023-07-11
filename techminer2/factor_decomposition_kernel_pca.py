# flake8: noqa
# pylint: disable=line-too-long
"""
.. _factor_decomposition_kernel_pca:

Factor Decomposition Kernel PCA
===============================================================================

Factor matrix obtained by appliying SVD to the co-occurrence matrix. 

**Algorithm:**

1. Computes the co-occurrence matrix of the specified field.

2. Optionally, normalize the co-occurrence matrix.

3. Applies Kernel PCA (or another technique) to the co-occurrence matrix.

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
...     .factor_decomposition_kernel_pca()
... )
FactorMatrix(cooc_matrix='CoocMatrix(columns='author_keywords',
    rows='author_keywords', dims=(20, 20))',
    estimator=KernelPCA(n_components=19, random_state=0), shape=(20, 19))

* Functional interface

>>> cooc_matrix = tm2p.co_occurrence_matrix(
...     root_dir="data/regtech/",
...     columns='author_keywords',
...     col_top_n=20,
... )
>>> factor_matrix = tm2p.factor_decomposition_kernel_pca(
...     cooc_matrix,
... )
>>> factor_matrix
FactorMatrix(cooc_matrix='CoocMatrix(columns='author_keywords',
    rows='author_keywords', dims=(20, 20))',
    estimator=KernelPCA(n_components=19, random_state=0), shape=(20, 19))

    
* Results:

>>> factor_matrix.df_.round(3)
                                DIM_00  DIM_01  DIM_02  ...  DIM_16  DIM_17  DIM_18
author_keywords                                         ...                        
REGTECH 28:329                  27.114  -2.512  -0.067  ...   0.024     0.0     0.0
FINTECH 12:249                  11.927   5.381  -0.382  ...  -0.006     0.0     0.0
REGULATORY_TECHNOLOGY 07:037    -2.275   0.710   6.022  ...  -0.062     0.0     0.0
COMPLIANCE 07:030                3.563  -4.286   0.788  ...  -0.034     0.0     0.0
REGULATION 05:164                1.280   3.410   0.569  ...  -0.146     0.0     0.0
ANTI_MONEY_LAUNDERING 05:034    -4.296  -0.963   2.453  ...   0.043     0.0     0.0
FINANCIAL_SERVICES 04:168       -1.277   1.490  -2.557  ...   0.073     0.0     0.0
FINANCIAL_REGULATION 04:035     -2.712   0.842  -2.698  ...  -0.089     0.0     0.0
ARTIFICIAL_INTELLIGENCE 04:023  -2.568  -0.938   1.186  ...  -0.105     0.0     0.0
RISK_MANAGEMENT 03:014          -1.732   1.653   1.876  ...   0.242     0.0     0.0
INNOVATION 03:012               -3.693   1.191  -0.367  ...   0.107     0.0     0.0
BLOCKCHAIN 03:005               -2.548  -0.318  -0.814  ...   0.139     0.0     0.0
SUPTECH 03:004                  -1.127   0.720   0.470  ...  -0.025     0.0     0.0
SEMANTIC_TECHNOLOGIES 02:041    -2.363   1.425  -0.773  ...  -0.085     0.0     0.0
DATA_PROTECTION 02:027          -3.002   0.165  -1.579  ...   0.027     0.0     0.0
SMART_CONTRACTS 02:022          -3.457  -0.694  -1.231  ...  -0.119     0.0     0.0
CHARITYTECH 02:017              -3.436  -1.225  -0.475  ...   0.003     0.0     0.0
ENGLISH_LAW 02:017              -3.436  -1.225  -0.475  ...   0.003     0.0     0.0
ACCOUNTABILITY 02:014           -2.981  -2.413  -0.973  ...   0.005     0.0     0.0
DATA_PROTECTION_OFFICER 02:014  -2.981  -2.413  -0.973  ...   0.005     0.0     0.0
<BLANKLINE>
[20 rows x 19 columns]




"""
import textwrap
from dataclasses import dataclass

import pandas as pd
from sklearn.decomposition import KernelPCA

from .factor_decomposition_2d_map import factor_decomposition_2d_map
from .vantagepoint.discover.matrix.matrix_normalization import (
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
def factor_decomposition_kernel_pca(
    #
    # FUNCTION PARAMS:
    cooc_matrix_or_tfidf,
    association_index=None,
    #
    # DECOMPOSITION PARAMS:
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

    estimator.fit(matrix)
    transformed_matrix = estimator.transform(matrix)

    columns = [
        f"DIM_{i_component:>02d}" for i_component in range(n_components)
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
