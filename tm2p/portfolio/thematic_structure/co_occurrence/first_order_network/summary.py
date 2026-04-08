"""
Summary
===============================================================================

Smoke tests:
    >>> from sklearn.cluster import AgglomerativeClustering
    >>> estimator = AgglomerativeClustering(
    ...     n_clusters=6,
    ...     metric="precomputed",
    ...     linkage="average",  #       linkage ∈ {"average", "complete", "single"}
    ...     distance_threshold=None,  # always None
    ...     compute_full_tree=True,  #  always
    ...     compute_distances=True,  #  always True
    ... )
    >>> from tm2p.enum import Field, AssociationIndex, ItemOrderBy
    >>> from tm2p.portfolio.thematic_structure.co_occurrence.first_order_network import Summary
    >>> df = (
    ...     Summary()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.AUTHKW_NORM)
    ...     .having_items_in_top(20)
    ...     .having_items_ordered_by(ItemOrderBy.OCC)
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # NETWORK:
    ...     .using_association_index(AssociationIndex.JACCARD)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering(estimator)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> print(df.to_string()) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
       CLUSTER  NUM_ITEMS  PERCENTAGE                                                                                                                       ITEMS
    0        0          4        20.0  financial technology 015:02734; financial literacy 005:00665; economic growth 005:00660; sustainable development 005:00604
    1        1          4        20.0                  blockchain 011:02023; artificial intelligence 008:01915; crowdfunding 007:01245; digital finance 005:02052
    2        2          4        20.0                                 banking 010:02599; innovation 009:01703; financial services 007:01673; technology 007:01409
    3        3          3        15.0                                                                green finance 011:02844; covid-19 006:01224; banks 005:00769
    4        4          3        15.0                                                                china 009:01947; regtech 006:01481; sustainability 006:01357
    5        5          2        10.0                                                                            fintech 117:25478; financial inclusion 017:03823

    >>> df = (
    ...     Summary()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.AUTHKW_NORM)
    ...     .having_items_in_top(20)
    ...     .having_items_ordered_by(ItemOrderBy.OCC)
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(False)
    ...     #
    ...     # NETWORK:
    ...     .using_association_index(AssociationIndex.JACCARD)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering(estimator)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> print(df.to_string()) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
       CLUSTER  NUM_ITEMS  PERCENTAGE                                                                               ITEMS
    0        0          4        20.0  financial technology; financial literacy; economic growth; sustainable development
    1        1          4        20.0                  blockchain; artificial intelligence; crowdfunding; digital finance
    2        2          4        20.0                                 banking; innovation; financial services; technology
    3        3          3        15.0                                                      green finance; covid-19; banks
    4        4          3        15.0                                                      china; regtech; sustainability
    5        5          2        10.0                                                        fintech; financial inclusion

"""

import pandas as pd  # type: ignore

from tm2p._intern import ParamsMixin

from .cluster_to_items import ClusterToItems

CLUSTER = "CLUSTER"
NUM_ITEMS = "NUM_ITEMS"
PERCENTAGE = "PERCENTAGE"
ITEMS = "ITEMS"


class Summary(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        communities = ClusterToItems().update(**self.params.__dict__).run()
        communities_len = {}
        communities_perc = {}
        communities_dict = {}

        total = float(sum(len(communities[key]) for key in communities))

        for key, values in communities.items():
            communities_len[key] = len(values)
            communities_perc[key] = round(communities_len[key] / total * 100, 1)
            communities_dict[key] = "; ".join(values)

        summary = pd.DataFrame(
            {
                CLUSTER: list(communities_dict.keys()),
                NUM_ITEMS: communities_len.values(),
                PERCENTAGE: communities_perc.values(),
                ITEMS: communities_dict.values(),
            }
        )

        summary = summary.sort_values(CLUSTER, ascending=True)
        summary = summary.reset_index(drop=True)

        return summary
