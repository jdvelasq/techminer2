"""
Terms to Cluster Mapping
===============================================================================


Smoke tests:
    >>> from techminer2.co_occurrence_network.descriptors import TermsToClustersMapping
    >>> mapping = (
    ...     TermsToClustersMapping()
    ...     #
    ...     # FIELD:
    ...     .having_items_in_top(20)
    ...     .having_items_ordered_by("OCC")
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_term_counters(True)
    ...     #
    ...     # NETWORK:
    ...     .using_clustering_algorithm_or_dict("louvain")
    ...     .using_association_index("association")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/data/")
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

Smoke tests:
    >>> mapping = (
    ...     TermsToClustersMapping()
    ...     #
    ...     # FIELD:
    ...     .having_items_in_top(20)
    ...     .having_items_ordered_by("OCC")
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_term_counters(False)
    ...     #
    ...     # NETWORK:
    ...     .using_clustering_algorithm_or_dict("louvain")
    ...     .using_association_index("association")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/data/")
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

from techminer2._internals import ParamsMixin
from techminer2.analyze.networks.co_occurrence.usr.terms_to_clusters_mapping import (
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
