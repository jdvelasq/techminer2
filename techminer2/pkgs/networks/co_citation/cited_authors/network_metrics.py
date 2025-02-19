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


>>> from techminer2.pkgs.networks.co_citation.cited_authors import NetworkMetrics
>>> (
...     NetworkMetrics()
...     #
...     # UNIT OF ANALYSIS:
...     .having_terms_in_top(30)
...     .having_citation_threshold(0)
...     .having_terms_in(None)
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
                   Degree  Betweenness  Closeness  PageRank
Burtch G. 1:14         19     0.079539   0.717949  0.056952
Lin M. 1:09            19     0.079539   0.717949  0.056952
Dahlberg T. 1:06       15     0.039062   0.651163  0.045606
Mackenzie A. 1:04      15     0.176372   0.666667  0.050477
Gomber P. 1:08         14     0.058402   0.595745  0.043989


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
            .unit_of_analysis("cited_authors")
            .build()
        )
