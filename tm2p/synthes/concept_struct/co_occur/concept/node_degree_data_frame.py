"""
Node Degree Frame
===============================================================================


Smoke tests:
    >>> from tm2p.co_occurrence_network.descriptors import NodeDegreeDataFrame
    >>> df =(
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
    ... )
    >>> df.head() # doctest: +SKIP
       Node                     Name  Degree
    0     0          FINTECH 38:6131      19
    1     1       REGULATORS 08:0974      18
    2     2  THE_DEVELOPMENT 09:1293      16
    3     3     PRACTITIONER 06:1194      16
    4     4     TECHNOLOGIES 15:1633      15


"""

from tm2p._internals import ParamsMixin
from tm2p.synthes.concept_struct.co_occur.usr.node_degree_data_frame import (
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
            .with_source_field("descriptors")
            .run()
        )
