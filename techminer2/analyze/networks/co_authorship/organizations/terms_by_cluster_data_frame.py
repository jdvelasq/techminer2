"""
Terms by Cluster Frame
===============================================================================



Smoke tests:
    >>> from techminer2.packages.networks.co_authorship.organizations import TermsByClusterDataFrame
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
    ...     .where_root_directory("examples/tests/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
                                             0  ...                            9
    0       Goethe Univ Frankfurt (DEU) 2:1065  ...  Univ of Latvia (LVA) 2:0163
    1     Pennsylvania State Univ (USA) 1:0576  ...
    2  Singapore Manag Univ (SMU) (SGP) 1:0576  ...
    3            Univ of Delaware (USA) 1:0576  ...
    <BLANKLINE>
    [4 rows x 10 columns]

"""

from techminer2._internals import ParamsMixin
from techminer2.analyze.networks.co_occurrence.usr.terms_by_cluster_data_frame import (
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
            .with_field("organizations")
            .run()
        )
