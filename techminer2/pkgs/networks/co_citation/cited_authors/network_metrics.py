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
...     .where_root_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_range_is(None, None)
...     .where_record_citations_range_is(None, None)
...     .where_records_match(None)
...     #
...     .run()
... ).head()
                    Degree  Betweenness  Closeness  PageRank
Zavolokina L. 1:09      23     0.106147   0.828571  0.055935
Gomber P. 1:09          22     0.049606   0.805556  0.052428
Lin M. 1:11             21     0.075575   0.783784  0.052154
Burtch G. 1:16          20     0.043628   0.763158  0.048395
Dapp T.F. 1:06          19     0.036768   0.743590  0.046041


"""
from ....._internals.mixins import ParamsMixin
from .._internals.network_metrics import NetworkMetrics as InternalNetworkMetrics


class NetworkMetrics(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        return (
            InternalNetworkMetrics()
            .update(**self.params.__dict__)
            .unit_of_analysis("cited_authors")
            .run()
        )
