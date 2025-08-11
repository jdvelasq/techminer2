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
    >>> from techminer2.packages.networks.co_occurrence.keywords import TermsToClustersMapping
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
    {'BANKING 03:0370': 0,
     'BLOCKCHAIN 04:0945': 0,
     'BUSINESS_MODEL 04:1472': 0,
     'COMMERCE 03:0846': 2,
     'CROWDFUNDING 03:0335': 1,
     'DIGITAL_TECHNOLOGIES 02:0494': 2,
     'ELECTRONIC_MONEY 03:0305': 0,
     'FINANCE 11:1950': 0,
     'FINANCIAL_INCLUSION 03:0590': 2,
     'FINANCIAL_INSTITUTION 04:0746': 2,
     'FINANCIAL_SERVICE 08:1680': 0,
     'FINANCIAL_SERVICES_INDUSTRIES 03:0949': 0,
     'FINANCIAL_TECHNOLOGIES 03:0461': 1,
     'FINTECH 32:5393': 0,
     'INNOVATION 08:0990': 0,
     'LITERATURE_REVIEW 02:0560': 1,
     'MARKETPLACE_LENDING 03:0317': 0,
     'SURVEYS 03:0484': 0,
     'SUSTAINABILITY 03:0227': 1,
     'SUSTAINABLE_DEVELOPMENT 03:0227': 1}


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
    {'BANKING': 0,
     'BLOCKCHAIN': 0,
     'BUSINESS_MODEL': 0,
     'COMMERCE': 2,
     'CROWDFUNDING': 1,
     'DIGITAL_TECHNOLOGIES': 2,
     'ELECTRONIC_MONEY': 0,
     'FINANCE': 0,
     'FINANCIAL_INCLUSION': 2,
     'FINANCIAL_INSTITUTION': 2,
     'FINANCIAL_SERVICE': 0,
     'FINANCIAL_SERVICES_INDUSTRIES': 0,
     'FINANCIAL_TECHNOLOGIES': 1,
     'FINTECH': 0,
     'INNOVATION': 0,
     'LITERATURE_REVIEW': 1,
     'MARKETPLACE_LENDING': 0,
     'SURVEYS': 0,
     'SUSTAINABILITY': 1,
     'SUSTAINABLE_DEVELOPMENT': 1}



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
            .with_field("keywords")
            .run()
        )
