# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Terms to Cluster Mapping
===============================================================================


Example:
    >>> from techminer2.packages.networks.co_occurrence.descriptors import TermsToClustersMapping
    >>> mapping = (
    ...     TermsToClustersMapping()
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
    ...     .using_clustering_algorithm_or_dict("louvain")
    ...     .using_association_index("association")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("examples/fintech/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> from pprint import pprint
    >>> pprint(mapping) # doctest: +SKIP
    {'BANKS 08:1049': 0,
     'CHINA 06:0673': 1,
     'CONSUMERS 07:0925': 0,
     'DATA 07:1086': 0,
     'FINANCE 10:1188': 1,
     'FINANCIAL_SERVICES 06:1116': 1,
     'FINANCIAL_TECHNOLOGIES 12:1615': 1,
     'FINTECH 38:6131': 0,
     'FINTECH_COMPANIES 05:1072': 0,
     'INFORMATION_TECHNOLOGY 05:1101': 0,
     'INNOVATION 08:1816': 1,
     'PRACTITIONER 06:1194': 0,
     'REGULATORS 08:0974': 1,
     'SERVICES 06:1089': 1,
     'TECHNOLOGIES 15:1633': 1,
     'THE_DEVELOPMENT 09:1293': 1,
     'THE_FINANCIAL_INDUSTRY 09:2006': 0,
     'THE_FINANCIAL_SECTOR 05:1147': 0,
     'THE_FINANCIAL_SERVICES_INDUSTRY 06:1237': 1,
     'THE_IMPACT 06:0908': 0}

Example:
    >>> mapping = (
    ...     TermsToClustersMapping()
    ...     #
    ...     # FIELD:
    ...     .having_terms_in_top(20)
    ...     .having_terms_ordered_by("OCC")
    ...     .having_term_occurrences_between(None, None)
    ...     .having_term_citations_between(None, None)
    ...     .having_terms_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_term_counters(False)
    ...     #
    ...     # NETWORK:
    ...     .using_clustering_algorithm_or_dict("louvain")
    ...     .using_association_index("association")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("examples/fintech/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> from pprint import pprint
    >>> pprint(mapping) # doctest: +SKIP
    {'BANKS': 0,
     'CHINA': 1,
     'CONSUMERS': 0,
     'DATA': 0,
     'FINANCE': 1,
     'FINANCIAL_SERVICES': 1,
     'FINANCIAL_TECHNOLOGIES': 1,
     'FINTECH': 0,
     'FINTECH_COMPANIES': 0,
     'INFORMATION_TECHNOLOGY': 0,
     'INNOVATION': 1,
     'PRACTITIONER': 0,
     'REGULATORS': 1,
     'SERVICES': 1,
     'TECHNOLOGIES': 1,
     'THE_DEVELOPMENT': 1,
     'THE_FINANCIAL_INDUSTRY': 0,
     'THE_FINANCIAL_SECTOR': 0,
     'THE_FINANCIAL_SERVICES_INDUSTRY': 1,
     'THE_IMPACT': 0}



"""
from techminer2._internals.mixins import ParamsMixin
from techminer2.packages.networks.co_occurrence.user.terms_to_clusters_mapping import (
    TermsToClustersMapping as UserTermsToClusterMapping,
)


class TermsToClustersMapping(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        return (
            UserTermsToClusterMapping()
            .update(**self.params.__dict__)
            .with_field("descriptors")
            .run()
        )
