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


Smoke tests:
    >>> from techminer2.co_occurrence_network.user import ClustersToTermsMapping
    >>> mapping = (
    ...     ClustersToTermsMapping()
    ...     #
    ...     # FIELD:
    ...     .with_field("raw_keywords")
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
    ...     .where_root_directory("examples/tests/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> from pprint import pprint
    >>> pprint(mapping)
    {0: ['FINTECH 32:5393',
         'INNOVATION 08:0990',
         'FINANCIAL_SERVICES 05:0746',
         'FINANCIAL_INCLUSION 03:0590',
         'FINANCIAL_INSTITUTION 03:0488',
         'SURVEYS 03:0484',
         'BANKING 03:0370',
         'MARKETPLACE_LENDING 03:0317',
         'ELECTRONIC_MONEY 03:0305'],
     1: ['FINANCE 11:1950',
         'FINANCIAL_SERVICE 04:1036',
         'BUSINESS_MODELS 03:1335',
         'BLOCKCHAIN 03:0881',
         'COMMERCE 03:0846',
         'FINANCIAL_SERVICES_INDUSTRIES 02:0696'],
     2: ['FINANCIAL_TECHNOLOGY 03:0461',
         'CROWDFUNDING 03:0335',
         'SUSTAINABILITY 03:0227',
         'SUSTAINABLE_DEVELOPMENT 03:0227',
         'LITERATURE_REVIEW 02:0560']}



"""
from techminer2._internals import ParamsMixin
from techminer2._internals.nx import (
    internal__cluster_nx_graph,
    internal__create_clusters_to_terms_mapping,
)
from techminer2.analyze.networks.co_occurrence._internals.create_nx_graph import (
    internal__create_nx_graph,
)


class ClustersToTermsMapping(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        nx_graph = internal__create_nx_graph(params=self.params)
        nx_graph = internal__cluster_nx_graph(params=self.params, nx_graph=nx_graph)
        mapping = internal__create_clusters_to_terms_mapping(
            params=self.params, nx_graph=nx_graph
        )

        return mapping
