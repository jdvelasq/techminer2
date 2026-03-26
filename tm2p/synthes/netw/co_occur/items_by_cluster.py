"""
ItemsByCluster
===============================================================================


Smoke tests:
    >>> from tm2p import Field, AssociationIndex, ItemOrderBy
    >>> from tm2p.synthes.netw.co_occur import ItemsByCluster
    >>> df = (
    ...     ItemsByCluster()
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
    >>> df
                                      0  ...                             2
    0                 fintech 117:25478  ...             banking 010:02599
    1     financial inclusion 017:03823  ...          innovation 009:01703
    2              blockchain 011:02023  ...  financial services 007:01673
    3                   china 009:01947  ...          technology 007:01409
    4  artificialintelligence 008:01915  ...               banks 005:00769
    5           crowd-funding 007:01245  ...
    6                reg-tech 006:01481  ...
    7          sustainability 006:01357  ...
    8                covid-19 006:01224  ...
    9         digital finance 005:02052  ...
    <BLANKLINE>
    [10 rows x 3 columns]



    >>> df = (
    ...     ItemsByCluster()
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
    >>> df  # doctest: +NORMALIZE_WHITESPACE
                            0                        1                   2
    0                 fintech     financial-technology             banking
    1     financial inclusion            green finance          innovation
    2              blockchain       financial literacy  financial services
    3                   china          economic-growth          technology
    4  artificialintelligence  sustainable development               banks
    5           crowd-funding
    6                reg-tech
    7          sustainability
    8                covid-19
    9         digital finance


"""

from tm2p._intern import ParamsMixin, remove_counters
from tm2p._intern.nx import cluster_nx_graph, extract_communities
from tm2p.synthes.netw.co_occur._intern.create_nx_graph import create_nx_graph


class ItemsByCluster(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        use_counters = self.params.counters
        self.params.counters = True
        nx_graph = create_nx_graph(self.params)
        nx_graph = cluster_nx_graph(self.params, nx_graph)
        communities = extract_communities(nx_graph)
        if use_counters is False:
            self.params.counters = False
            for col in communities.columns:
                communities[col] = communities[col].apply(remove_counters)
        return communities
