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

>>> from techminer2.pkgs.networks.co_citation.cited_references import NodeDegreeDataFrame
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
   Node                                        Name  Degree
0     0         Burtch G., Ghose A., Wattal S. 1:13      15
1     1  Lin M., Prabhala N.R., Viswanathan S. 1:08      15
2     2   Zavolokina L., Dolata M., Schwabe G. 1:06      14
3     3         Duarte J., Siegel S., Young L. 1:06      13
4     4       Skan J., Dickerson J., Masood S. 1:05      13



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
            .unit_of_analysis("cited_references")
            .run()
        )
