# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Cluster to Terms Mapping
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
    >>> from techminer2.packages.topic_modeling.user import ClusterToTermsMapping
    >>> mapping = (
    ...     ClusterToTermsMapping()
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
    ...     .where_root_directory("examples/small/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> import pprint
    >>> pprint.pprint(mapping) # doctest: +SKIP
    {0: ['FINTECH 38:6131',
         'FINANCIAL_TECHNOLOGY 11:1519',
         'TECHNOLOGY 10:1220',
         'BANKS 08:1049',
         'REGULATORS 08:0974',
         'CONSUMERS 07:0925',
         'FINANCIAL_INSTITUTIONS 03:0464',
         'THE_DEVELOPMENT 08:1193',
         'BANKING 04:0481',
         'CUSTOMERS 04:0599',
         'FINANCIAL_REGULATION 03:0461',
         'REGULATION 03:0461',
    ...



"""
from techminer2._internals import ParamsMixin
from techminer2.analyze.topic_modeling.user.components_by_term_data_frame import (
    ComponentsByTermDataFrame,
)


class ClusterToTermsMapping(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        theme_term_matrix = (
            ComponentsByTermDataFrame().update(**self.params.__dict__).run()
        )

        mapping = {}
        for i_row in range(theme_term_matrix.shape[0]):
            sorting_indices = theme_term_matrix.iloc[i_row, :].sort_values(
                ascending=False
            )
            theme_term_matrix = theme_term_matrix[sorting_indices.index]
            if self.params.top_n is not None:
                mapping[i_row] = list(theme_term_matrix.columns[: self.params.top_n])
            else:
                mapping[i_row] = list(theme_term_matrix.columns)

        return mapping
