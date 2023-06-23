# flake8: noqa
"""
PCA Factor Matrix
===============================================================================

Factor matrix obtained by appliying PCA to the co-occurrence matrix. 

**Algorithm:**

1. Computes the co-occurrence matrix of the specified field.

2. Optionally, normalize the co-occurrence matrix.

3. Applies PCA to the co-occurrence matrix.

4. Returns the factor matrix.


>>> import techminer2plus
>>> cooc_matrix = techminer2plus.analyze.matrix.co_occurrence_matrix(
...     root_dir="data/regtech/",
...     columns='author_keywords',
...     col_top_n=20,
... )

>>> pca_factor_matrix = techminer2plus.analyze.matrix.pca_factor_matrix(
...     cooc_matrix,
... )
>>> pca_factor_matrix.table_.round(3)
                                DIM_00  DIM_01  DIM_02  ...  DIM_17  DIM_18  DIM_19
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



# pylint: disable=line-too-long
"""
import pandas as pd
from sklearn.decomposition import PCA

from ...classes import PcaFactorMatrix
from .matrix_normalization import matrix_normalization


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def pca_factor_matrix(
    #
    # Specific params:
    cooc_matrix,
    estimator=None,
    association_index=None,
):
    """Creates a PCA factor matrix from the co-occurrence matrix.


    # pylint: disable=line-too-long
    """
    cooc_matrix = matrix_normalization(cooc_matrix, association_index)
    matrix = cooc_matrix.matrix_

    if estimator is None:
        estimator = PCA()

    estimator.fit(matrix)

    transformed_matrix = estimator.transform(matrix)
    columns = [f"DIM_{i:>02d}" for i in range(transformed_matrix.shape[1])]

    matrix = pd.DataFrame(
        transformed_matrix,
        index=matrix.index,
        columns=columns,
    )
    matrix.index.name = cooc_matrix.rows_

    factor_matrix = PcaFactorMatrix()
    factor_matrix.table_ = matrix
    factor_matrix.field_ = cooc_matrix.columns_
    factor_matrix.explained_variance_ = estimator.explained_variance_
    factor_matrix.explained_variance_ratio_ = (
        estimator.explained_variance_ratio_
    )
    factor_matrix.prompt_ = "TODO"

    return factor_matrix
