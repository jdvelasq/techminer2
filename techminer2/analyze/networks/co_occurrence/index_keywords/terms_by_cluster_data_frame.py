"""
Terms by Cluster Frame
===============================================================================


Smoke tests:
    >>> from techminer2.co_occurrence_network.index_keywords import TermsByClusterDataFrame
    >>> df = (
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
    >>> df   # doctest: +SKIP
                                           0  ...                             3
    0                        FINANCE 10:1866  ...               SURVEYS 03:0484
    1              FINANCIAL_SERVICE 05:1115  ...  FINANCIAL_INDUSTRIES 02:0323
    2                       COMMERCE 03:0846  ...  SECURITY_AND_PRIVACY 02:0323
    3        SUSTAINABLE_DEVELOPMENT 03:0227  ...
    4                     BLOCKCHAIN 02:0736  ...
    5  FINANCIAL_SERVICES_INDUSTRIES 02:0696  ...
    6           DEVELOPING_COUNTRIES 02:0248  ...
    <BLANKLINE>
    [7 rows x 4 columns]



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
            .with_field("index_keywords")
            .run()
        )
