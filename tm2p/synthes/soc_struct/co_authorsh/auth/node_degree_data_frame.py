"""
Node Degree Frame
===============================================================================


Smoke tests:
    >>> from tm2p.packages.networks.co_authorship.authors import NodeDegreeDataFrame
    >>> (
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
       Node                  Name  Degree
    0     0      Gomber P. 2:1065       5
    1     1  Kauffman R.J. 1:0576       3
    2     2      Parker C. 1:0576       3
    3     3     Weber B.W. 1:0576       3
    4     4         Gai K. 2:0323       2



"""

from tm2p._intern import ParamsMixin
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
            .with_source_field("authors")
            .run()
        )
