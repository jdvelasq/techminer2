# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

import numpy as np
import pandas as pd
from sklearn.decomposition import TruncatedSVD

from ..science_mapping.co_occurrence.co_occurrence_matrix import co_occurrence_matrix
from ..science_mapping.co_occurrence.normalize_co_occurrence_matrix import (
    normalize_co_occurrence_matrix,
)


def factor_svd_cooc_embedding(
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
    """Creates a factor matrix from the co-occurrence matrix.

    :meta private:
    """
    #
    # Co-occurrence matrix
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

    #
    # Decomposition:
    if n_components is None:
        n_components = min(min(matrix_values.shape) - 1, 100)

    estimator = TruncatedSVD(
        n_components=n_components,
        algorithm="randomized",
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

    return matrix_values
