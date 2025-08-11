# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Network Degree Frame
===============================================================================


Example:
    >>> from techminer2.packages.networks.coupling.authors  import NodeDegreeDataFrame
    >>> (
    ...     NodeDegreeDataFrame()
    ...     #
    ...     # UNIT OF ANALYSIS:
    ...     .having_terms_in_top(20)
    ...     .having_citation_threshold(0)
    ...     .having_occurrence_threshold(2)
    ...     .having_terms_in(None)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory_is("examples/fintech/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... ).head()
       Node                  Name  Degree
    0     0      Gomber P. 2:1065       3
    1     1  Kauffman R.J. 1:0576       3
    2     2      Parker C. 1:0576       3
    3     3     Weber B.W. 1:0576       3
    4     4    Jagtiani J. 3:0317       1




"""
from techminer2._internals.mixins import ParamsMixin
from techminer2.packages.networks.coupling._internals.from_others.node_degree_data_frame import (
    InternalNodeDegreeDataFrame,
)


class NodeDegreeDataFrame(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        return (
            InternalNodeDegreeDataFrame()
            .update(**self.params.__dict__)
            .update(terms_order_by="OCC")
            .unit_of_analysis("authors")
            .run()
        )
