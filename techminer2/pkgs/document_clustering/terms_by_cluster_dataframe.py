# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Terms by Cluster Dataframe
===============================================================================

>>> from sklearn.cluster import KMeans
>>> kmeans = KMeans(
...     n_clusters=4,
...     init="k-means++",
...     n_init=10,
...     max_iter=300,
...     tol=0.0001,
...     algorithm="lloyd",
...     random_state=0,
... )
>>> from techminer2.pkgs.document_clustering import TermsByClusterDataFrame
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
...     # COUNTERS:
...     .using_term_counters(True)
...     #
...     # TFIDF:
...     .using_binary_term_frequencies(False)
...     .using_row_normalization(None)
...     .using_idf_reweighting(False)
...     .using_idf_weights_smoothing(False)
...     .using_sublinear_tf_scaling(False)
...     #
...     # CLUSTERING:
...     .using_clustering_estimator_or_dict(kmeans)
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     .where_records_match(None)
...     #
...     .build()
... ).head(10)
                                         0  ...                            3
0                       THIS_PAPER 14:2240  ...         THE_RESEARCH 05:0839
1                            BANKS 09:1133  ...  INFORMATION_SYSTEMS 04:0830
2  THE_FINANCIAL_SERVICES_INDUSTRY 06:1237  ...                             
3                        CONSUMERS 06:0804  ...                             
4                    ENTREPRENEURS 04:0744  ...                             
5                       INVESTMENT 04:0581  ...                             
6                    THE_POTENTIAL 04:0547  ...                             
7                                           ...                             
8                                           ...                             
9                                           ...                             
<BLANKLINE>
[10 rows x 4 columns]

"""
import pandas as pd  # type: ignore

from ..._internals.mixins import ParamsMixin
from .clusters_to_terms_mapping import ClustersToTermsMapping


class TermsByClusterDataFrame(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):

        mapping = ClustersToTermsMapping().update(**self.params.__dict__).build()
        frame = pd.DataFrame.from_dict(mapping, orient="index").T
        frame = frame.fillna("")
        frame = frame.sort_index(axis=1)
        return frame
