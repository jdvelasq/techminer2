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
...     .where_root_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_range_is(None, None)
...     .where_record_citations_range_is(None, None)
...     .where_records_match(None)
...     #
...     .run()
... ).head()
                   0                    1                    2
0  Australia 05:0783      Denmark 02:0330  South Korea 06:1192
1      China 08:1085      Germany 07:1814        Spain 01:0225
2  Hong Kong 01:0178  Netherlands 03:0300   Kazakhstan 01:0121
3     Latvia 02:0163    Singapore 01:0576                     
4   Slovenia 01:0102  Switzerland 04:0660                     
                               



"""
from ....._internals.mixins import ParamsMixin
from .._internals.from_others.terms_by_cluster_data_frame import (
    InternalTermsByClusterDataFrame,
)


class TermsByClusterDataFrame(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        return (
            InternalTermsByClusterDataFrame()
            .update(**self.params.__dict__)
            .unit_of_analysis("countries")
            .run()
        )
