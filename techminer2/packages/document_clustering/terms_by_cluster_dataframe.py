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
>>> from techminer2.packages.document_clustering import TermsByClusterDataFrame
>>> (
...     TermsByClusterDataFrame()
...     #
...     # FIELD:
...     .with_field("raw_keywords")
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
...     .using_clustering_algorithm_or_dict(kmeans)
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_range_is(None, None)
...     .where_record_citations_range_is(None, None)
...     .where_records_match(None)
...     #
...     .run()
... ).head(10)
                                 0  ...                         3
0           SUSTAINABILITY 03:0227  ...  CONTENT_ANALYSIS 02:0181
1  SUSTAINABLE_DEVELOPMENT 03:0227  ...    DIGITALIZATION 02:0181
2        LITERATURE_REVIEW 02:0560  ...     POPULAR_PRESS 02:0181
3         FINANCIAL_SYSTEM 02:0385  ...
4             DIGITIZATION 02:0319  ...
5                    CHINA 02:0150  ...
6                                   ...
7                                   ...
8                                   ...
9                                   ...
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

    def run(self):

        mapping = ClustersToTermsMapping().update(**self.params.__dict__).run()
        frame = pd.DataFrame.from_dict(mapping, orient="index").T
        frame = frame.fillna("")
        frame = frame.sort_index(axis=1)
        return frame
