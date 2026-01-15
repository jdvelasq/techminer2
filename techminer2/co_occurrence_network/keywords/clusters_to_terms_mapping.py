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
    >>> from techminer2.co_occurrence_network.keywords import ClustersToTermsMapping
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
    {0: ['FINTECH 32:5393',
         'FINANCE 11:1950',
         'FINANCIAL_SERVICE 08:1680',
         'INNOVATION 08:0990',
         'BUSINESS_MODEL 04:1472',
         'BLOCKCHAIN 04:0945',
         'FINANCIAL_SERVICES_INDUSTRIES 03:0949',
         'SURVEYS 03:0484',
         'BANKING 03:0370',
         'MARKETPLACE_LENDING 03:0317',
         'ELECTRONIC_MONEY 03:0305'],
     1: ['FINANCIAL_TECHNOLOGIES 03:0461',
         'CROWDFUNDING 03:0335',
         'SUSTAINABILITY 03:0227',
         'SUSTAINABLE_DEVELOPMENT 03:0227',
         'LITERATURE_REVIEW 02:0560'],
     2: ['FINANCIAL_INSTITUTION 04:0746',
         'COMMERCE 03:0846',
         'FINANCIAL_INCLUSION 03:0590',
         'DIGITAL_TECHNOLOGIES 02:0494']}


"""
from techminer2._internals.mixins import ParamsMixin
from techminer2.co_occurrence_network.usr.clusters_to_terms_mapping import (
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
            .with_field("keywords")
            .run()
        )
