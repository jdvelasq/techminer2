"""
Terms by Cluster Frame
===============================================================================


Smoke tests:
    >>> from tm2p.packages.networks.co_authorship.countries import TermsByClusterDataFrame
    >>> (
    ...     TermsByClusterDataFrame()
    ...     #
    ...     # FIELD:
    ...     .having_items_in_top(20)
    ...     .having_items_ordered_by("OCC")
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     # NETWORK:
    ...     .using_clustering_algorithm_or_dict("louvain")
    ...     .using_association_index("association")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/fintech/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
                           0  ...                          8
    0  United States 16:3189  ...  Brunei Darussalam 01:0090
    1          China 08:1085  ...
    2    South Korea 06:1192  ...
    3         Sweden 01:0160  ...
    4     Kazakhstan 01:0121  ...
    5        Belgium 01:0101  ...
    <BLANKLINE>
    [6 rows x 9 columns]


"""

from tm2p._internals import ParamsMixin
from tm2p.synthes.concept_struct.co_occur.usr.terms_by_cluster_data_frame import (
    TermsByClusterDataFrame as UserTermsByClusterDataFrame,
)


class TermsByClusterDataFrame(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        return (
            UserTermsByClusterDataFrame()
            .update(**self.params.__dict__)
            .with_source_field("countries")
            .run()
        )
