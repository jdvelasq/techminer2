"""
Node Degree Frame
===============================================================================


Smoke tests:
    >>> from techminer2.co_occurrence_network.index_keywords import NodeDegreeDataFrame
    >>> df = (
    ...     NodeDegreeDataFrame()
    ...     #
    ...     # FIELD:
    ...     .having_items_in_top(20)
    ...     .having_items_ordered_by("OCC")
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_term_counters(True)
    ...     #
    ...     # NETWORK:
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
    ... ).head()
    >>> df  # doctest: +SKIP
       Node                       Name  Degree
    0     0            FINANCE 10:1866      17
    1     1            FINTECH 10:1412      16
    2     2  FINANCIAL_SERVICE 05:1115      11
    3     3     CYBER_SECURITY 02:0342       9
    4     4           COMMERCE 03:0846       7


"""

from techminer2._internals import ParamsMixin
from techminer2.analyze._networks.co_occurrence.usr.node_degree_data_frame import (
    NodeDegreeDataFrame as UserNodeDegreeDataFrame,
)


class NodeDegreeDataFrame(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        return (
            UserNodeDegreeDataFrame()
            .update(**self.params.__dict__)
            .with_field("index_keywords")
            .run()
        )
