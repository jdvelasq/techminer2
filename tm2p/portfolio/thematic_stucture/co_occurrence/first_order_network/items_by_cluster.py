"""
ItemsByCluster
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
    >>> from tm2p.portfolio.thematic_stucture.co_occurrence.first_order_network import ItemsByCluster
    >>> df = (
    ...     ItemsByCluster()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.CONCEPT_NORM)
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
    >>> print(df.to_string())  # doctest: +NORMALIZE_WHITESPACE
                                    0                     1                              2                                  3                    4                   5
    0               fintech 157:34856     finance 050:10972                china 033:06419  sustainable development 018:02898  consumers 017:03475  research 014:03510
    1  financial technology 052:09484  innovation 033:07734           the impact 021:04968                 the role 015:02528
    2    financial services 031:07105  technology 026:04985             evidence 018:03900
    3                 banks 031:06740  blockchain 017:04405  fintech development 015:03625
    4                  data 026:05921
    5       the development 026:05689
    6               banking 025:04625
    7   financial inclusion 022:04623

    >>> df = (
    ...     ItemsByCluster()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.CONCEPT_NORM)
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
    >>> print(df.to_string())  # doctest: +NORMALIZE_WHITESPACE
                          0           1                    2                        3          4         5
    0               fintech     finance                china  sustainable development  consumers  research
    1  financial technology  innovation           the impact                 the role
    2    financial services  technology             evidence
    3                 banks  blockchain  fintech development
    4                  data
    5       the development
    6               banking
    7   financial inclusion

"""

import pandas as pd  # type: ignore

from tm2p._intern import ParamsMixin

from .cluster_to_items import ClusterToItems


class ItemsByCluster(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        c2i = ClusterToItems().update(**self.params.__dict__).run()

        df = pd.DataFrame.from_dict(c2i, orient="index").T
        df = df.fillna("")
        df = df.sort_index(axis=1)

        return df
