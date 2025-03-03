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


>>> from techminer2.pkgs.networks.co_authorship.countries import NetworkMetrics
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
United States 16:3189       8     0.253411   0.494152  0.187008
Australia 05:0783           6     0.147173   0.423559  0.126959
Germany 07:1814             5     0.115010   0.386728  0.098902
China 08:1085               4     0.012671   0.386728  0.115357
Denmark 02:0330             4     0.050682   0.355789  0.074453

"""
from ....._internals.mixins import ParamsMixin
from ...co_occurrence.user.network_metrics import NetworkMetrics as UserNetworkMetrics


class NetworkMetrics(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):
        """:meta private:"""

        return (
            UserNetworkMetrics()
            .update(**self.params.__dict__)
            .with_field("countries")
            .build()
        )
