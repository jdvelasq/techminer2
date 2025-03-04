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

>>> from techminer2.pkgs.networks.coupling.authors import TermsByClusterDataFrame
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
                      0  ...              3
0      Gomber P. 2:1065  ...  Gai K. 2:0323
1      Hornuf L. 2:0358  ...  Qiu M. 2:0323
2    Jagtiani J. 3:0317  ...  Sun X. 2:0323
3  Kauffman R.J. 1:0576  ...               
4     Koch J.-A. 1:0489  ...               
<BLANKLINE>
[5 rows x 4 columns]
                               



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
            .unit_of_analysis("authors")
            .run()
        )
