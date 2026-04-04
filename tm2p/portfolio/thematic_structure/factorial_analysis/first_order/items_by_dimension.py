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
    >>> from tm2p import Field, ItemOrderBy
    >>> from tm2p.portfolio.thematic_structure.factorial_analysis.first_order import ItemsByDimension
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
    ...     # DECOMPOSITION:
    ...     .using_decomposition_algorithm(pca)
    ...     #
    ...     # TFIDF:
    ...     .using_binary_item_frequencies(False)
    ...     .using_tfidf_norm(None)
    ...     .using_tfidf_smooth_idf(False)
    ...     .using_tfidf_sublinear_tf(False)
    ...     .using_tfidf_use_idf(False)
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
    DIM                                    0         1  ...         3         4
    CONCEPT_NORM                                        ...
    fintech 157:34856              -0.032162 -0.013889  ... -0.061741  0.137496
    financial technology 052:09484 -0.114038 -0.013613  ... -0.407758  0.027168
    finance 050:10972               0.362718 -0.123027  ... -0.088512 -0.103789
    innovation 033:07734            0.182331 -0.022703  ...  0.039805  0.229508
    china 033:06419                 0.091802  0.304775  ... -0.033409 -0.014761
    <BLANKLINE>
    [5 rows x 5 columns]


"""

import numpy as np
import pandas as pd  # type: ignore

from tm2p._intern import ParamsMixin
from tm2p.portfolio.thematic_structure.tfidf.matrix import Matrix


class ItemsByDimension(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        decomposition_algorithm = self.params.decomposition_algorithm

        tfidf = Matrix().update(**self.params.__dict__).run()
        tfidf = tfidf.astype(float)

        decomposition_algorithm.fit(tfidf)  # type: ignore
        components = decomposition_algorithm.components_  # type: ignore
        eigenvalues = decomposition_algorithm.explained_variance_  # type: ignore
        loadings = components.T * np.sqrt(eigenvalues)
        loadings = varimax(loadings)

        embedding = pd.DataFrame(
            loadings,
            index=tfidf.columns,
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
