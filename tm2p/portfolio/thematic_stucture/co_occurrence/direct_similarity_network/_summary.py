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
    >>> from tm2p.portfolio.thematic_stucture.co_occurrence.first_order_network import Summary
    >>> df = (
    ...     Summary()
    ...     #
    ...     # UNIT OF ANALYSIS:
    ...     .with_co_occurrence_unit(CoOccurrenceUnit.KW)
    ...     #
    ...     .having_items_in_top(20)
    ...     .having_items_ordered_by(ItemOrderBy.OCC)
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     .using_minimum_item_co_occurrence(1)
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


    >>> df = (
    ...     Summary()
    ...     #
    ...     # UNIT OF ANALYSIS:
    ...     .with_co_occurrence_unit(CoOccurrenceUnit.KW)
    ...     #
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

"""

import pandas as pd  # type: ignore

from tm2p._intern import ParamsMixin

from ._cluster_to_items import ClusterToItems

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
