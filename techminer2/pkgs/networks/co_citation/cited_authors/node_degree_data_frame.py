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

>>> from techminer2.pkgs.networks.co_citation.cited_authors import NodeDegreeDataFrame
>>> (
...     NodeDegreeDataFrame()
...     #
...     # UNIT OF ANALYSIS:
...     .having_terms_in_top(30)
...     .having_citation_threshold(0)
...     .having_terms_in(None)
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_range_is(None, None)
...     .where_record_citations_range_is(None, None)
...     .where_records_match(None)
...     #
...     .run()
... ).head()
   Node                Name  Degree
0     0  Zavolokina L. 1:09      23
1     1      Gomber P. 1:09      22
2     2         Lin M. 1:11      21
3     3      Burtch G. 1:16      20
4     4      Dapp T.F. 1:06      19




"""
from ....._internals.mixins import ParamsMixin
from .._internals.node_degree_data_frame import (
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
