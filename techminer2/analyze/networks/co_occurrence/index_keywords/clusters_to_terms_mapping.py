"""
Clusters to Terms Mapping
===============================================================================

Smoke tests:
    >>> from techminer2.co_occurrence_network.index_keywords import ClustersToTermsMapping
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
    >>> pprint(mapping)  # doctest: +SKIP
    {0: ['FINANCE 10:1866',
         'FINANCIAL_SERVICE 05:1115',
         'COMMERCE 03:0846',
         'SUSTAINABLE_DEVELOPMENT 03:0227',
         'BLOCKCHAIN 02:0736',
         'FINANCIAL_SERVICES_INDUSTRIES 02:0696',
         'DEVELOPING_COUNTRIES 02:0248'],
     1: ['INVESTMENT 02:0418',
         'FINANCIAL_SYSTEM 02:0385',
         'PERCEIVED_USEFULNESS 02:0346',
         'CYBER_SECURITY 02:0342',
         'DESIGN_METHODOLOGY_APPROACH 02:0329',
         'SALES 02:0329'],
     2: ['FINTECH 10:1412',
         'ELECTRONIC_MONEY 03:0305',
         'FINANCIAL_INSTITUTION 02:0262',
         'INFORMATION_SYSTEMS 02:0235'],
     3: ['SURVEYS 03:0484',
         'FINANCIAL_INDUSTRIES 02:0323',
         'SECURITY_AND_PRIVACY 02:0323']}


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
            .with_field("index_keywords")
            .run()
        )
