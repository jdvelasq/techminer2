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

>>> from techminer2.pkgs.networks.citation.countries import TermsByClusterDataFrame
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
...     .where_record_citattions_range_is(None, None)
...     .where_records_match(None)
...     #
...     .build()
... ).head()
                     0  ...                          3
0        China 08:1085  ...            Germany 07:1814
1      Denmark 02:0330  ...  Brunei Darussalam 01:0090
2       France 01:0258  ...                           
3  South Korea 06:1192  ...                           
4  Switzerland 04:0660  ...                           
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
            .unit_of_analysis("countries")
            .build()
        )
