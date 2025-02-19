# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Terms by Cluster Frame
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
>>> from techminer2.pkgs.topic_modeling.user import TermsByClusterDataFrame
>>> (
...     TermsByClusterDataFrame()
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
...     .where_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     .where_records_match(None)
...     #
...     .build()
... ).head()
cluster                             0  ...                           9
term                                   ...                            
0                     FINTECH 46:7183  ...             FINTECH 46:7183
1        FINANCIAL_TECHNOLOGY 17:2359  ...      ELSEVIER_B_._V 04:0718
2                     FINANCE 21:3481  ...          THIS_PAPER 14:2240
3                  TECHNOLOGY 13:1594  ...           CONSUMERS 06:0804
4                  THIS_STUDY 14:1737  ...  FINANCIAL_SERVICES 11:1862
<BLANKLINE>
[5 rows x 10 columns]


"""
import pandas as pd  # type: ignore

from ...._internals.mixins import ParamsMixin
from .cluster_to_terms_mapping import ClusterToTermsMapping


class TermsByClusterDataFrame(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):
        """:meta private:"""

        mapping = ClusterToTermsMapping().update(**self.params.__dict__).build()

        frame = pd.DataFrame.from_dict(mapping, orient="index").T
        frame = frame.fillna("")
        frame = frame.sort_index(axis=1)
        frame.columns.name = "cluster"
        frame.index.name = "term"
        return frame
