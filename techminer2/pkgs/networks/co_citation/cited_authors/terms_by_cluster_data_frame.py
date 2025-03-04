# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Terms by Cluster Frame
===============================================================================


>>> from techminer2.pkgs.networks.co_citation.cited_authors import TermsByClusterDataFrame
>>> (
...     TermsByClusterDataFrame()
...     #
...     # UNIT OF ANALYSIS:
...     .having_terms_in_top(30)
...     .having_citation_threshold(0)
...     .having_terms_in(None)
...     #
...     # CLUSTERING:
...     .using_clustering_algorithm_or_dict("louvain")
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
                   0                   1                  2
0   Berger A.N. 1:06   Clemons E.K. 1:13        Gai K. 1:43
1   Boot A.W.A. 1:08  Kauffman R.J. 1:13         Li Y. 1:08
2        Lin M. 1:11      Hornuf L. 1:12       Shim Y. 1:09
3    Agarwal S. 1:07       Klohn L. 1:06    Davis F.D. 1:10
4  Philippon T. 1:09      Burtch G. 1:16  Venkatesh V. 1:13

"""
from ....._internals.mixins import ParamsMixin
from .._internals.terms_by_cluster_data_frame import (
    TermsByClusterDataFrame as InternalTermsByClusterDataFrame,
)


class TermsByClusterDataFrame(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        return (
            InternalTermsByClusterDataFrame()
            .update(**self.params.__dict__)
            .unit_of_analysis("cited_authors")
            .run()
        )
