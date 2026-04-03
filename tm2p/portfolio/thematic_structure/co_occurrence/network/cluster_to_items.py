"""
ClusterToItems
===============================================================================

Smoke tests:
    >>> from tm2p import Field, AssociationIndex, ItemOrderBy
    >>> from tm2p.synthesize.netw.co_occur import ClusterToItems
    >>> mapping = (
    ...     ClusterToItems()
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
    ...     .using_association_index(AssociationIndex.NONE)
    ...     .using_clustering_algorithm_or_dict("louvain")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> from pprint import pprint
    >>> pprint(mapping)
    {0: ['fintech 117:25478',
         'financial inclusion 017:03823',
         'blockchain 011:02023',
         'china 009:01947',
         'artificialintelligence 008:01915',
         'crowd-funding 007:01245',
         'reg-tech 006:01481',
         'sustainability 006:01357',
         'covid-19 006:01224',
         'digital finance 005:02052'],
     1: ['financial-technology 015:02734',
         'green finance 011:02844',
         'financial literacy 005:00665',
         'economic-growth 005:00660',
         'sustainable development 005:00604'],
     2: ['banking 010:02599',
         'innovation 009:01703',
         'financial services 007:01673',
         'technology 007:01409',
         'banks 005:00769']}


    >>> mapping = (
    ...     ClusterToItems()
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
    ...     .using_association_index(AssociationIndex.NONE)
    ...     .using_clustering_algorithm_or_dict("louvain")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> pprint(mapping)
    {0: ['fintech',
         'financial inclusion',
         'blockchain',
         'china',
         'artificialintelligence',
         'crowd-funding',
         'reg-tech',
         'sustainability',
         'covid-19',
         'digital finance'],
     1: ['financial-technology',
         'green finance',
         'financial literacy',
         'economic-growth',
         'sustainable development'],
     2: ['banking', 'innovation', 'financial services', 'technology', 'banks']}


"""

from tm2p._intern import ParamsMixin
from tm2p._intern.nx import cluster_nx_graph, create_clusters_to_terms_mapping
from tm2p.portfolio.thematic_structure.co_occurrence.network._intern.create_nx_graph import (
    create_nx_graph,
)


class ClusterToItems(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        use_counters = self.params.counters
        self.params.counters = True
        nx_graph = create_nx_graph(params=self.params)
        nx_graph = cluster_nx_graph(params=self.params, nx_graph=nx_graph)
        mapping = create_clusters_to_terms_mapping(nx_graph=nx_graph)
        if use_counters is False:
            self.params.counters = False
            for cluster, items in mapping.items():
                mapping[cluster] = [" ".join(item.split(" ")[:-1]) for item in items]

        return mapping
