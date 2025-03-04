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

>>> from techminer2.pkgs.networks.citation.organizations import TermsByClusterDataFrame
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
... ).head()
                                                   0  ...                               3
0  CESifo, Poschingerstr. 5, Munich, 81679, Germa...  ...   Univ of Zaragoza (ESP) 1:0225
1                        Univ of Zurich (CHE) 3:0434  ...  Sungkyunkwan Univ (KOR) 2:0307
2  Max Planck Inst for Innovation and Competition...  ...                                
3                         SKEMA Bus Sch (FRA) 1:0258  ...                                
4                        Univ of Bremen (DEU) 1:0258  ...                                
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

    def run(self):
        return (
            OtherTermsByClusterDataFrame()
            .update(**self.params.__dict__)
            .unit_of_analysis("organizations")
            .run()
        )
