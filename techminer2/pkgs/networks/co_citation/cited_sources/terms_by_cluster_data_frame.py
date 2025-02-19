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


>>> from techminer2.pkgs.networks.co_citation.cited_sources import TermsByClusterDataFrame
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
                              0  ...                                                  2
0  J STRATEGIC INFORM SYST 1:14  ...                         ELECT COMMER RES APPL 1:32
1                 J FINANC 1:23  ...                      FUTURE GENER COMPUT SYST 1:10
2               MANAGE SCI 1:30  ...  PROC IEEE INT CONF CYBER SECUR CLOUD COMPUT CS...
3            J FINANC ECON 1:20  ...  PROC IEEE INT CONF BIG DATA SECUR CLOUD IEEE B...
4            J BANK FINANC 1:13  ...                                    COMMUN ACM 1:12
<BLANKLINE>
[5 rows x 3 columns]



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
            .unit_of_analysis("cited_sources")
            .build()
        )
