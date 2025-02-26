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

>>> from techminer2.pkgs.networks.coupling.authors import NetworkMetrics
>>> (
...     NetworkMetrics()
...     #
...     # UNIT OF ANALYSIS:
...     .having_terms_in_top(20)
...     .having_citation_threshold(0)
...     .having_occurrence_threshold(2)
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
                    Degree  Betweenness  Closeness  PageRank
Gomber P. 2:1065        10      0.01462   0.526316  0.118738
Hornuf L. 2:0358        10      0.01462   0.526316  0.027604
Koch J.-A. 1:0489       10      0.01462   0.526316  0.065543
Siering M. 1:0489       10      0.01462   0.526316  0.065543
Jagtiani J. 3:0317       8      0.00000   0.438596  0.027560



"""
from ....._internals.mixins import ParamsMixin
from .._internals.from_others.network_metrics import InternalNetworkMetrics


class NetworkMetrics(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):
        return (
            InternalNetworkMetrics()
            .update(**self.params.__dict__)
            .unit_of_analysis("authors")
            .build()
        )
