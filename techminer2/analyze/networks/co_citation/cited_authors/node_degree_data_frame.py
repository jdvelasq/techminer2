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


Smoke tests:
    >>> from techminer2.packages.networks.co_citation.cited_authors import NodeDegreeDataFrame
    >>> (
    ...     NodeDegreeDataFrame()
    ...     #
    ...     # UNIT OF ANALYSIS:
    ...     .having_terms_in_top(30)
    ...     .using_citation_threshold(0)
    ...     .having_terms_in(None)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("examples/tests/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... ).head()
       Node               Name  Degree
    0     0       Leong C. 1:2       9
    1     1  Zavolokina L. 1:3       8
    2     2       Gabor D. 1:2       6
    3     3      Ryu H.-S. 1:2       6
    4     4         Alt R. 1:1       6




"""
from techminer2._internals import ParamsMixin
from techminer2.analyze.networks.co_citation._internals.node_degree_data_frame import (
    NodeDegreeDataFrame as InternalNodeDegreeDataFrame,
)


class NodeDegreeDataFrame(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        return (
            InternalNodeDegreeDataFrame()
            .update(**self.params.__dict__)
            .unit_of_analysis("cited_authors")
            .run()
        )
