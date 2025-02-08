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


>>> from techminer2.pkgs.networks.co_occurrence.author_keywords import NetworkMetrics
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
...     .where_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     .where_records_match(None)
...     #
...     .build()
... ).head()
                            Degree  Betweenness  Closeness  PageRank
FINTECH 31:5168                 18     0.761793   0.950000  0.240341
FINANCIAL_SERVICES 04:0667       7     0.056725   0.612903  0.065863
INNOVATION 07:0911               6     0.036452   0.593750  0.083155
FINANCE 02:0309                  5     0.015984   0.575758  0.038939
TECHNOLOGY 02:0310               5     0.028655   0.575758  0.042338


"""
from .....internals.mixins import InputFunctionsMixin
from ..internals.network_metrics import InternalNetworkMetrics


class NetworkMetrics(
    InputFunctionsMixin,
):
    """:meta private:"""

    def build(self):
        """:meta private:"""

        return (
            InternalNetworkMetrics()
            .update_params(**self.params.__dict__)
            .with_field("author_keywords")
            .build()
        )
