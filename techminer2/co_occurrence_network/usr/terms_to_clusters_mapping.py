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
    >>> from techminer2.co_occurrence_network.user import TermsToClustersMapping
    >>> mapping = (
    ...     TermsToClustersMapping()
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
    ...     .where_root_directory("examples/fintech/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> from pprint import pprint
    >>> pprint(mapping)
    {'BANKING 03:0370': 0,
     'BLOCKCHAIN 03:0881': 1,
     'BUSINESS_MODELS 03:1335': 1,
     'COMMERCE 03:0846': 1,
     'CROWDFUNDING 03:0335': 2,
     'ELECTRONIC_MONEY 03:0305': 0,
     'FINANCE 11:1950': 1,
     'FINANCIAL_INCLUSION 03:0590': 0,
     'FINANCIAL_INSTITUTION 03:0488': 0,
     'FINANCIAL_SERVICE 04:1036': 1,
     'FINANCIAL_SERVICES 05:0746': 0,
     'FINANCIAL_SERVICES_INDUSTRIES 02:0696': 1,
     'FINANCIAL_TECHNOLOGY 03:0461': 2,
     'FINTECH 32:5393': 0,
     'INNOVATION 08:0990': 0,
     'LITERATURE_REVIEW 02:0560': 2,
     'MARKETPLACE_LENDING 03:0317': 0,
     'SURVEYS 03:0484': 0,
     'SUSTAINABILITY 03:0227': 2,
     'SUSTAINABLE_DEVELOPMENT 03:0227': 2}


    >>> mapping = (
    ...     TermsToClustersMapping()
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
    >>> pprint(mapping)
    {'BANKING': 0,
     'BLOCKCHAIN': 1,
     'BUSINESS_MODELS': 1,
     'COMMERCE': 1,
     'CROWDFUNDING': 2,
     'ELECTRONIC_MONEY': 0,
     'FINANCE': 1,
     'FINANCIAL_INCLUSION': 0,
     'FINANCIAL_INSTITUTION': 0,
     'FINANCIAL_SERVICE': 1,
     'FINANCIAL_SERVICES': 0,
     'FINANCIAL_SERVICES_INDUSTRIES': 1,
     'FINANCIAL_TECHNOLOGY': 2,
     'FINTECH': 0,
     'INNOVATION': 0,
     'LITERATURE_REVIEW': 2,
     'MARKETPLACE_LENDING': 0,
     'SURVEYS': 0,
     'SUSTAINABILITY': 2,
     'SUSTAINABLE_DEVELOPMENT': 2}



"""
from techminer2._internals.mixins import ParamsMixin
from techminer2._internals.nx import (
    internal__cluster_nx_graph,
    internal__create_terms_to_clusters_mapping,
)
from techminer2.co_occurrence_network._internals.create_nx_graph import (
    internal__create_nx_graph,
)


class TermsToClustersMapping(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        nx_graph = internal__create_nx_graph(self.params)
        nx_graph = internal__cluster_nx_graph(self.params, nx_graph)
        return internal__create_terms_to_clusters_mapping(self.params, nx_graph)

        nx_graph = internal__create_nx_graph(self.params)
        nx_graph = internal__cluster_nx_graph(self.params, nx_graph)
        return internal__create_terms_to_clusters_mapping(self.params, nx_graph)
