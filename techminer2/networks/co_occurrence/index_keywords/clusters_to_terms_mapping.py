# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Clusters to Terms Mapping
===============================================================================

Example:
    >>> from techminer2.co_occurrence_network.index_keywords import ClustersToTermsMapping
    >>> mapping = (
    ...     ClustersToTermsMapping()
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
from techminer2._internals.mixins import ParamsMixin
from techminer2.co_occurrence.usr.clusters_to_terms_mapping import (
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
