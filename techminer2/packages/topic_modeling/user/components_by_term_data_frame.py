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
    >>> (
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
    ...     .where_root_directory_is("example/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    term       FINTECH 44:6942  ...  RESEARCH 03:0821
    component                   ...
    0                11.523877  ...          0.100007
    1                 5.519260  ...          0.100000
    2                 5.100178  ...          0.100000
    3                 0.100000  ...          0.100000
    4                 2.676155  ...          0.100000
    5                 3.704010  ...          0.100000
    6                 5.571897  ...          0.100000
    7                 3.100027  ...          0.100000
    8                 0.100013  ...          0.100000
    9                 7.604582  ...          3.099993
    <BLANKLINE>
    [10 rows x 50 columns]



"""
import pandas as pd  # type: ignore

from ...._internals.mixins import ParamsMixin
from ....database.metrics.tfidf import DataFrame as TfIdfDataFrame


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
