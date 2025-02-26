# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Network Metrics
===============================================================================


>>> from techminer2.pkgs.networks.co_citation.cited_references import NetworkMetrics
>>> (
...     NetworkMetrics()
...     #
...     # UNIT OF ANALYSIS:
...     .having_terms_in_top(30)
...     .having_citation_threshold(0)
...     .having_terms_in(None)
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     .where_records_match(None)
...     #
...     .build()
... ).head()
                                                Degree  ...  PageRank
Lin M., 2013, MANAGE SCI 1:7                        16  ...  0.050778
Burtch G., 2013, INF SYST RES 1:4                   15  ...  0.046530
Polasik M., 2015, INT J ELECT COMMER 1:3            15  ...  0.046589
Dahlberg T., 2008, ELECT COMMER RES APPL 1:3        14  ...  0.043624
Burtch G., 2014, MIS QUART MANAGE INF SYST 1:4      12  ...  0.038056
<BLANKLINE>
[5 rows x 4 columns]


"""
from ....._internals.mixins import ParamsMixin
from .._internals.network_metrics import NetworkMetrics as InternalNetworkMetrics


class NetworkMetrics(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):
        return (
            InternalNetworkMetrics()
            .update(**self.params.__dict__)
            .unit_of_analysis("cited_references")
            .build()
        )
