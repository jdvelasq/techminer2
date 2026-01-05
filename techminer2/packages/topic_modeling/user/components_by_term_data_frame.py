# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Components by Term Frame
===============================================================================

Example:
    >>> from sklearn.decomposition import LatentDirichletAllocation
    >>> lda = LatentDirichletAllocation(
    ...     n_components=10,
    ...     learning_decay=0.7,
    ...     learning_offset=50.0,
    ...     max_iter=10,
    ...     batch_size=128,
    ...     evaluate_every=-1,
    ...     perp_tol=0.1,
    ...     mean_change_tol=0.001,
    ...     max_doc_update_iter=100,
    ...     random_state=0,
    ... )
    >>> from techminer2.packages.topic_modeling.user import ComponentsByTermDataFrame
    >>> df = (
    ...     ComponentsByTermDataFrame()
    ...     #
    ...     # FIELD:
    ...     .with_field("raw_descriptors")
    ...     .having_terms_in_top(50)
    ...     .having_terms_ordered_by("OCC")
    ...     .having_term_occurrences_between(None, None)
    ...     .having_term_citations_between(None, None)
    ...     .having_terms_in(None)
    ...     #
    ...     # DECOMPOSITION:
    ...     .using_decomposition_algorithm(lda)
    ...     .using_top_terms_by_theme(5)
    ...     #
    ...     # TFIDF:
    ...     .using_binary_term_frequencies(False)
    ...     .using_row_normalization(None)
    ...     .using_idf_reweighting(False)
    ...     .using_idf_weights_smoothing(False)
    ...     .using_sublinear_tf_scaling(False)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("examples/fintech/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> df  # doctest: +SKIP
    term       FINTECH 38:6131  ...  REGULATION 03:0461
    component                   ...
    0                 8.362389  ...            2.099995
    1                 3.334489  ...            0.100000
    2                 2.099949  ...            0.100000
    3                 0.100000  ...            0.100000
    4                 0.100000  ...            0.100000
    5                 4.837552  ...            0.100000
    6                 4.779077  ...            0.100000
    7                 3.100090  ...            0.100000
    8                 1.186569  ...            1.100005
    9                11.099884  ...            0.100000
    <BLANKLINE>
    [10 rows x 50 columns]


"""
import pandas as pd  # type: ignore

from techminer2._internals.mixins import ParamsMixin
from techminer2.database.metrics.tfidf import DataFrame as TfIdfDataFrame


class ComponentsByTermDataFrame(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        tf_matrix = TfIdfDataFrame().update(**self.params.__dict__).run()

        self.params.decomposition_algorithm.fit(tf_matrix)

        frame = pd.DataFrame(
            self.params.decomposition_algorithm.components_,
            index=range(self.params.decomposition_algorithm.n_components),
            columns=tf_matrix.columns,
        )

        frame.columns.name = "term"
        frame.index.name = "component"

        return frame
