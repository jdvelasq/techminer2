"""
ItemsByDimension
===============================================================================

Smoke test:
    >>> from sklearn.decomposition import PCA
    >>> pca = PCA(
    ...     n_components=5,
    ...     whiten=False,
    ...     svd_solver="auto",
    ...     tol=0.0,
    ...     iterated_power="auto",
    ...     n_oversamples=10,
    ...     power_iteration_normalizer="auto",
    ...     random_state=0,
    ... )
    >>> from tm2p.enum import Field, ItemOrderBy
    >>> from tm2p.portfolio.thematic_stucture.factorial_analysis.second_order import ItemsByDimension
    >>> df = (
    ...     ItemsByDimension()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.CONCEPT_NORM)
    ...     .having_items_in_top(50)
    ...     .having_items_ordered_by(ItemOrderBy.OCC)
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     .using_minimum_item_co_occurrence(1)
    ...     #
    ...     # DECOMPOSITION:
    ...     .using_decomposition_algorithm(pca)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> df.head()  # doctest: +NORMALIZE_WHITESPACE
    DIM                                    0          1  ...         3         4
    columns                                              ...
    fintech 157:34856               0.838984  12.652016  ...  7.137741  4.177661
    financial technology 052:09484  1.031366   2.259151  ...  6.964852  1.549411
    finance 050:10972              -1.875993   7.172343  ...  3.458193  2.022143
    innovation 033:07734           -0.726116   4.471920  ...  0.631075  0.660265
    china 033:06419                -3.778033   1.666304  ...  1.417483 -0.394586
    <BLANKLINE>
    [5 rows x 5 columns]


"""

import numpy as np
import pandas as pd  # type: ignore

from tm2p._intern import ParamsMixin
from tm2p.portfolio.thematic_stucture.co_occurrence.matrix.matrix import Matrix


class ItemsByDimension(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        decomposition_algorithm = self.params.decomposition_algorithm

        matrix = Matrix().update(**self.params.__dict__).run()
        matrix = matrix.astype(float)

        decomposition_algorithm.fit(matrix)  # type: ignore
        components = decomposition_algorithm.components_  # type: ignore
        eigenvalues = decomposition_algorithm.explained_variance_  # type: ignore
        loadings = components.T * np.sqrt(eigenvalues)
        loadings = varimax(loadings)

        embedding = pd.DataFrame(
            loadings,
            index=matrix.columns,
            columns=list(range(decomposition_algorithm.n_components)),  # type: ignore
        )
        embedding.columns.name = "DIM"

        return embedding


def varimax(Phi, gamma=1.0, q=20, tol=1e-6):

    _, k = Phi.shape
    R = np.eye(k)
    for _ in range(q):
        d = np.diag(
            Phi @ R @ np.diag(np.diag((Phi @ R).T @ (Phi @ R)) ** (gamma / 2 - 1))
        )
        u, s, vh = np.linalg.svd(Phi.T @ (Phi @ R - d))
        R_new = u @ vh
        if np.max(np.abs(R - R_new)) < tol:
            break
        R = R_new
    return Phi @ R
