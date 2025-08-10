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
    >>> from techminer2.packages.networks.co_occurrence.descriptors import ClustersToTermsMapping
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
    ...     .where_root_directory_is("examples/fintech/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> from pprint import pprint
    >>> pprint(mapping)
    {0: ['FINANCIAL_TECHNOLOGIES 14:2005',
         'FINANCIAL_SERVICE 12:2100',
         'THE_DEVELOPMENT 09:1293',
         'REGULATORS 08:0974',
         'SERVICES 07:1226',
         'BANKING 07:0851',
         'INVESTMENT 06:1294',
         'THE_FINANCIAL_SERVICES_INDUSTRY 06:1237',
         'PRACTITIONER 06:1194',
         'BUSINESS_MODEL 05:1578'],
     1: ['FINTECH 44:6942',
         'FINANCE 21:3481',
         'TECHNOLOGIES 17:1943',
         'INNOVATION 15:2741',
         'THE_FINANCIAL_INDUSTRY 09:2006',
         'THE_IMPACT 06:0908',
         'CHINA 06:0673'],
     2: ['BANKS 09:1133', 'DATA 07:1086', 'CONSUMERS 07:0925']}



"""
from ....._internals.mixins import ParamsMixin
from ..user.clusters_to_terms_mapping import \
    ClustersToTermsMapping as UserClustersToTermsMapping


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
