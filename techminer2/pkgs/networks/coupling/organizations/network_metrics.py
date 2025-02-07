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

## >>> from techminer2.pkgs.networks.coupling.organizations import NetworkMetrics
## >>> (
## ...     NetworkMetrics()
## ...     #
## ...     # UNIT OF ANALYSIS:
## ...     .having_terms_in_top(20)
## ...     .having_citation_threshold(0)
## ...     .having_occurrence_threshold(2)
## ...     .having_terms_in(None)
## ...     #
## ...     # DATABASE:
## ...     .where_directory_is("example/")
## ...     .where_database_is("main")
## ...     .where_record_years_between(None, None)
## ...     .where_record_citations_between(None, None)
## ...     .where_records_match(None)
## ...     #
## ...     .build()
## ... ).head()



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
            .unit_of_analysis("organizations")
            .build()
        )
