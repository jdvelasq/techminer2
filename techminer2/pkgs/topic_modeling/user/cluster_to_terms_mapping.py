# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Cluster to Terms Mapping
===============================================================================


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
>>> from techminer2.pkgs.topic_modeling.user import ClusterToTermsMapping
>>> mapping = (
...     ClusterToTermsMapping()
...     #
...     # FIELD:
...     .with_field("descriptors")
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
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     .where_records_match(None)
...     #
...     .build()
... )
>>> import pprint
>>> pprint.pprint(mapping) # doctest: +ELLIPSIS
{0: ['FINTECH 46:7183',
     'FINANCIAL_TECHNOLOGY 17:2359',
     'FINANCE 21:3481',
     'TECHNOLOGY 13:1594',
...



"""
from ...._internals.mixins import ParamsMixin
from .components_by_term_data_frame import ComponentsByTermDataFrame


class ClusterToTermsMapping(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):
        """:meta private:"""

        theme_term_matrix = (
            ComponentsByTermDataFrame().update(**self.params.__dict__).build()
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
