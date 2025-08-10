# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Node Degree Frame
===============================================================================


Example:
    >>> from techminer2.packages.networks.citation.organizations  import NodeDegreeDataFrame
    >>> (
    ...     NodeDegreeDataFrame()
    ...     #
    ...     # UNIT OF ANALYSIS:
    ...     .having_terms_in_top(30)
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
       Node                                          Name  Degree
    0     0                   Univ of Zurich (CHE) 3:0434       5
    1     1            Goethe Univ Frankfurt (DEU) 2:1065       5
    2     2                   Univ of Sydney (AUS) 2:0300       4
    3     3  Fed Reserv Bank of Philadelphia (USA) 3:0317       2
    4     4       Fed Reserv Bank of Chicago (USA) 2:0253       2



"""

from ....._internals.mixins import ParamsMixin
from .._internals.from_others.node_degree_data_frame import \
    NodeDegreeDataFrame as OtherNodeDegreeDataFrame


class NodeDegreeDataFrame(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        return (
            OtherNodeDegreeDataFrame()
            .update(**self.params.__dict__)
            .update(terms_order_by="OCC")
            .unit_of_analysis("organizations")
            .run()
        )
