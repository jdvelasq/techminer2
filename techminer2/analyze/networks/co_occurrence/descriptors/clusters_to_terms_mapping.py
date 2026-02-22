"""
Clusters to Terms Mapping
===============================================================================


Smoke tests:
    >>> from techminer2.co_occurrence_network.descriptors import ClustersToTermsMapping
    >>> mapping = (
    ...     ClustersToTermsMapping()
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
    ...     .where_root_directory("examples/tests/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> from pprint import pprint
    >>> pprint(mapping) # doctest: +SKIP
    {0: ['FINTECH 38:6131',
         'THE_FINANCIAL_INDUSTRY 09:2006',
         'BANKS 08:1049',
         'DATA 07:1086',
         'CONSUMERS 07:0925',
         'PRACTITIONER 06:1194',
         'THE_IMPACT 06:0908',
         'THE_FINANCIAL_SECTOR 05:1147',
         'INFORMATION_TECHNOLOGY 05:1101',
         'FINTECH_COMPANIES 05:1072'],
     1: ['TECHNOLOGIES 15:1633',
         'FINANCIAL_TECHNOLOGIES 12:1615',
         'FINANCE 10:1188',
         'THE_DEVELOPMENT 09:1293',
         'INNOVATION 08:1816',
         'REGULATORS 08:0974',
         'THE_FINANCIAL_SERVICES_INDUSTRY 06:1237',
         'FINANCIAL_SERVICES 06:1116',
         'SERVICES 06:1089',
         'CHINA 06:0673']}


"""

from techminer2._internals import ParamsMixin
from techminer2.analyze.networks.co_occurrence.usr.clusters_to_terms_mapping import (
    ClustersToTermsMapping as UserClustersToTermsMapping,
)


class ClustersToTermsMapping(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        return (
            UserClustersToTermsMapping()
            .update(**self.params.__dict__)
            .with_field("descriptors")
            .run()
        )
