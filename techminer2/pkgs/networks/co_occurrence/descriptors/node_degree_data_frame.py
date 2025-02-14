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

>>> from techminer2.pkgs.networks.co_occurrence.descriptors import NodeDegreeDataFrame
>>> (
...     NodeDegreeDataFrame()
...     #
...     # FIELD:
...     .having_terms_in_top(20)
...     .having_terms_ordered_by("OCC")
...     .having_term_occurrences_between(None, None)
...     .having_term_citations_between(None, None)
...     .having_terms_in(None)
...     #
...     # COUNTERS:
...     .using_term_counters(True)
...     #
...     # NETWORK:
...     .using_association_index("association")
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     .where_records_match(None)
...     #
...     .build()
... ).head()
   Node                Name  Degree
0     0     FINTECH 46:7183      19
1     1     FINANCE 21:3481      19
2     2  TECHNOLOGY 13:1594      19
3     3       BANKS 09:1133      19
4     4  REGULATORS 08:0974      19



"""
from .....internals.mixins import ParamsMixin
from ..user.node_degree_data_frame import NodeDegreeDataFrame as UserNodeDegreeDataFrame


class NodeDegreeDataFrame(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):
        """:meta private:"""

        return (
            UserNodeDegreeDataFrame()
            .update(**self.params.__dict__)
            .with_field("descriptors")
            .build()
        )
