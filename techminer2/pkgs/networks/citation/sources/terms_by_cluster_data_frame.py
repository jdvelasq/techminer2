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

>>> from techminer2.pkgs.networks.citation.sources import TermsByClusterDataFrame
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
...     .where_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     .where_records_match(None)
...     #
...     .build()
... ).head()
                                                   0  ...                                        3
0                            Business Horizons 1:557  ...               Financial Management 2:161
1                     Small Business Economics 1:258  ...  Journal of Economics and Business 3:422
2  Business and Information Systems Engineering 1...  ...               Financial Innovation 2:190
3                 Sustainability (Switzerland) 2:150  ...                                         
4                       China Economic Journal 1:096  ...                                         
<BLANKLINE>
[5 rows x 4 columns]



"""
from ....._internals.mixins import ParamsMixin
from .._internals.from_others.terms_by_cluster_data_frame import (
    TermsByClusterDataFrame as OtherTermsByClusterDataFrame,
)


class TermsByClusterDataFrame(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):
        return (
            OtherTermsByClusterDataFrame()
            .update(**self.params.__dict__)
            .unit_of_analysis("source_title")
            .build()
        )
