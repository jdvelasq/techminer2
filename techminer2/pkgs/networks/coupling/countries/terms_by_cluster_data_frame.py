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

>>> from techminer2.pkgs.networks.coupling.countries import TermsByClusterDataFrame
>>> (
...     TermsByClusterDataFrame()
...     #
...     # UNIT OF ANALYSIS:
...     .having_terms_in_top(20)
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
                     0                      1                    2
0      Denmark 02:0330      Australia 05:0783  South Korea 06:1192
1       France 01:0258          China 08:1085   Kazakhstan 01:0121
2      Germany 07:1814      Hong Kong 01:0178        Spain 01:0225
3    Indonesia 01:0102         Sweden 01:0160                     
4  Netherlands 03:0300  United States 16:3189                     
                                 



"""
from .....internals.mixins import InputFunctionsMixin
from ..internals.from_others.terms_by_cluster_data_frame import (
    InternalTermsByClusterDataFrame,
)


class TermsByClusterDataFrame(
    InputFunctionsMixin,
):
    """:meta private:"""

    def build(self):
        return (
            InternalTermsByClusterDataFrame()
            .update_params(**self.params.__dict__)
            .unit_of_analysis("countries")
            .build()
        )
