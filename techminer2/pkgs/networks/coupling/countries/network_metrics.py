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

>>> from techminer2.pkgs.networks.coupling.countries import NetworkMetrics
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
...     .where_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     .where_records_match(None)
...     #
...     .build()
... ).head()
                        Degree  Betweenness  Closeness  PageRank
United States 16:3189       16     0.218869   0.900000  0.217602
Germany 07:1814             15     0.104490   0.857143  0.134298
Australia 05:0783           13     0.093923   0.782609  0.097323
China 08:1085               13     0.053400   0.782609  0.141063
United Kingdom 03:0636      12     0.072246   0.750000  0.047458



"""
from .....internals.mixins import InputFunctionsMixin
from ..internals.from_others.network_metrics import InternalNetworkMetrics


class NetworkMetrics(
    InputFunctionsMixin,
):
    """:meta private:"""

    def build(self):
        return (
            InternalNetworkMetrics()
            .update_params(**self.params.__dict__)
            .unit_of_analysis("countries")
            .build()
        )
