# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Documents by Theme Frame
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
    >>> from techminer2.packages.topic_modeling.user import DocumentsByThemeDataFrame
    >>> (
    ...     DocumentsByThemeDataFrame()
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
    ... ).head()
    cluster                                                    0  ...         9
    article                                                       ...
    Alt R., 2018, ELECTRON MARK, V28, P235              0.033339  ...  0.033337
    Anagnostopoulos I., 2018, J ECON BUS, V100, P7      0.006668  ...  0.006668
    Anshari M., 2019, ENERGY PROCEDIA, V156, P234       0.012502  ...  0.012501
    Arner D.W., 2017, NORTHWEST J INTL LAW BUS, V37...  0.918166  ...  0.009092
    Belanche D., 2019, IND MANAGE DATA SYS, V119, P...  0.010001  ...  0.010001
    <BLANKLINE>
    [5 rows x 10 columns]



"""
import pandas as pd  # type: ignore

from ...._internals.mixins import ParamsMixin
from ....database.metrics.tfidf import DataFrame as TfIdfDataFrame


class DocumentsByThemeDataFrame(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        tf_matrix = TfIdfDataFrame().update(**self.params.__dict__).run()

        self.params.decomposition_algorithm.fit(tf_matrix)

        frame = pd.DataFrame(
            self.params.decomposition_algorithm.transform(tf_matrix),
            index=tf_matrix.index,
            columns=range(self.params.decomposition_algorithm.n_components),
        )
        frame.columns.name = "cluster"
        frame.index.name = "article"

        return frame
