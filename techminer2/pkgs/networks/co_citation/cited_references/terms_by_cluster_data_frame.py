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


>>> from techminer2.pkgs.networks.co_citation.cited_references import TermsByClusterDataFrame
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
...     .where_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     .where_records_match(None)
...     #
...     .build()
... ).head()
                                                   0  ...                                                  4
0  Adomavicius G., 2008, MIS QUART MANAGE INF SYS...  ...           Morse A., 2015, ANNU REV FINANC ECON 1:3
1           Au Y.A., 2008, ELECT COMMER RES APPL 1:3  ...  Fichman R.G., 2014, MIS QUART MANAGE INF SYST 1:3
2            Liu J., 2015, ELECT COMMER RES APPL 1:4  ...            Jun J., 2016, ASIAPAC J FINANC STUD 1:3
3                  Burtch G., 2013, INF SYST RES 1:4  ...                                                   
4       Dahlberg T., 2015, ELECT COMMER RES APPL 1:3  ...                                                   
<BLANKLINE>
[5 rows x 5 columns]



"""
from ....._internals.mixins import ParamsMixin
from .._internals.terms_by_cluster_data_frame import (
    TermsByClusterDataFrame as InternalTermsByClusterDataFrame,
)


class TermsByClusterDataFrame(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):
        return (
            InternalTermsByClusterDataFrame()
            .update(**self.params.__dict__)
            .unit_of_analysis("cited_references")
            .build()
        )
