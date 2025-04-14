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

>>> from techminer2.packages.networks.citation.sources import TermsByClusterDataFrame
>>> (
...     TermsByClusterDataFrame()
...     #
...     # UNIT OF ANALYSIS:
...     .having_terms_in_top(30)
...     .having_citation_threshold(0)
...     .having_occurrence_threshold(2)
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
... ).head(10)
                                                   0  ...                                        3
0                 Sustainability (Switzerland) 2:150  ...  Journal of Economics and Business 3:422
1                            Business Horizons 1:557  ...               Financial Innovation 2:190
2                     Small Business Economics 1:258  ...               Financial Management 2:161
3  Business and Information Systems Engineering 1...  ...
4  International Journal of Information Managemen...  ...
5                       China Economic Journal 1:096  ...
<BLANKLINE>
[6 rows x 4 columns]


"""
from ....._internals.mixins import ParamsMixin
from .._internals.from_others.terms_by_cluster_data_frame import (
    TermsByClusterDataFrame as OtherTermsByClusterDataFrame,
)


class TermsByClusterDataFrame(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        return (
            OtherTermsByClusterDataFrame()
            .update(**self.params.__dict__)
            .unit_of_analysis("abbr_source_title")
            .run()
        )
