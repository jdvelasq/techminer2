# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Metrics
===============================================================================


>>> from techminer2.pkgs.networks.co_occurrence.descriptors import NetworkMetrics
>>> (
...     NetworkMetrics()
...     #
...     # FIELD:
...     .having_terms_in_top(20)
...     .having_terms_ordered_by("OCC")
...     .having_term_occurrences_between(None, None)
...     .having_term_citations_between(None, None)
...     .having_terms_in(None)
...     #
...     # COUNTERS:
...     .using_term_counters(True)
...     #
...     # NETWORK:
...     .using_association_index("association")
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
                    Degree  Betweenness  Closeness  PageRank
BANKS 09:1133           19     0.013932        1.0  0.048466
FINANCE 21:3481         19     0.013932        1.0  0.073548
FINTECH 46:7183         19     0.013932        1.0  0.137497
REGULATORS 08:0974      19     0.013932        1.0  0.046255
TECHNOLOGY 13:1594      19     0.013932        1.0  0.059519

"""
from ....._internals.mixins import ParamsMixin
from ..user.network_metrics import NetworkMetrics as UserNetworkMetrics


class NetworkMetrics(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):
        """:meta private:"""

        return (
            UserNetworkMetrics()
            .update(**self.params.__dict__)
            .with_field("descriptors")
            .build()
        )
