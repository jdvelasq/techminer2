# flake8: noqa
"""
.. _kernel_pca_factor_matrix:

Kernel PCA Factor Matrix
===============================================================================

Factor matrix obtained by appliying KernelPCA to the co-occurrence matrix. 

**Algorithm:**

1. Computes the co-occurrence matrix of the specified field.

2. Optionally, normalize the co-occurrence matrix.

3. Applies Kernel PCA to the co-occurrence matrix.

4. Returns the factor matrix.


>>> import techminer2plus
>>> cooc_matrix = techminer2plus.matrix.co_occurrence_matrix(
...     root_dir="data/regtech/",
...     columns='author_keywords',
...     col_top_n=20,
... )

>>> kpca_factor_matrix = techminer2plus.factor_matrix.kernel_pca_factor_matrix(
...     cooc_matrix,
... )
>>> kpca_factor_matrix
KernelPCAFactorMatrix(field='author_keywords', shape=(20, 17))

>>> kpca_factor_matrix.table_.round(3)
                                DIM_00  DIM_01  DIM_02  ...  DIM_14  DIM_15  DIM_16
author_keywords                                         ...                        
REGTECH 28:329                  27.114  -2.512  -0.067  ...  -0.009   0.109   0.024
FINTECH 12:249                  11.927   5.381  -0.382  ...   0.119  -0.256  -0.006
REGULATORY_TECHNOLOGY 07:037    -2.275   0.710   6.022  ...   0.167   0.054  -0.062
COMPLIANCE 07:030                3.563  -4.286   0.788  ...  -0.215  -0.083  -0.034
REGULATION 05:164                1.280   3.410   0.569  ...  -0.070  -0.006  -0.146
ANTI_MONEY_LAUNDERING 05:034    -4.296  -0.963   2.453  ...  -0.100  -0.030   0.043
FINANCIAL_SERVICES 04:168       -1.277   1.490  -2.557  ...  -0.369   0.153   0.073
FINANCIAL_REGULATION 04:035     -2.712   0.842  -2.698  ...   0.527  -0.164  -0.089
ARTIFICIAL_INTELLIGENCE 04:023  -2.568  -0.938   1.186  ...  -0.262   0.129  -0.105
RISK_MANAGEMENT 03:014          -1.732   1.653   1.876  ...  -0.012  -0.306   0.242
INNOVATION 03:012               -3.693   1.191  -0.367  ...  -0.333   0.107   0.107
BLOCKCHAIN 03:005               -2.548  -0.318  -0.814  ...   0.470   0.241   0.139
SUPTECH 03:004                  -1.127   0.720   0.470  ...   0.048   0.231  -0.025
SEMANTIC_TECHNOLOGIES 02:041    -2.363   1.425  -0.773  ...   0.080   0.524  -0.085
DATA_PROTECTION 02:027          -3.002   0.165  -1.579  ...  -0.500   0.120   0.027
SMART_CONTRACTS 02:022          -3.457  -0.694  -1.231  ...  -0.306  -0.522  -0.119
CHARITYTECH 02:017              -3.436  -1.225  -0.475  ...   0.181  -0.120   0.003
ENGLISH_LAW 02:017              -3.436  -1.225  -0.475  ...   0.181  -0.120   0.003
ACCOUNTABILITY 02:014           -2.981  -2.413  -0.973  ...   0.201  -0.031   0.005
DATA_PROTECTION_OFFICER 02:014  -2.981  -2.413  -0.973  ...   0.201  -0.031   0.005
<BLANKLINE>
[20 rows x 17 columns]

# pylint: disable=line-too-long
"""
import textwrap
from dataclasses import dataclass

import pandas as pd
from sklearn.decomposition import KernelPCA

from .matrix_normalization import matrix_normalization


@dataclass
class KernelPcaFactorMatrix:
    """KernelPCA factor matrix."""

    field_: str
    table_: pd.DataFrame
    prompt_: str

    def __repr__(self):
        text = "KernelPCAFactorMatrix("
        text += f"field='{self.field_}'"
        text += f", shape={self.table_.shape}"
        text += ")"
        text = textwrap.fill(text, width=75, subsequent_indent="    ")
        return text


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def kernel_pca_factor_matrix(
    #
    # Specific params:
    cooc_matrix,
    estimator=None,
    association_index=None,
):
    """Creates a Kernel PCA factor matrix from the co-occurrence matrix.


    # pylint: disable=line-too-long
    """
    cooc_matrix = matrix_normalization(cooc_matrix, association_index)
    matrix = cooc_matrix.matrix_

    if estimator is None:
        estimator = KernelPCA()

    estimator.fit(matrix)

    transformed_matrix = estimator.transform(matrix)
    columns = [f"DIM_{i:>02d}" for i in range(transformed_matrix.shape[1])]

    matrix = pd.DataFrame(
        transformed_matrix,
        index=matrix.index,
        columns=columns,
    )
    matrix.index.name = cooc_matrix.rows_

    return KernelPcaFactorMatrix(
        table_=matrix,
        field_=cooc_matrix.columns_,
        prompt_="TODO",
    )
