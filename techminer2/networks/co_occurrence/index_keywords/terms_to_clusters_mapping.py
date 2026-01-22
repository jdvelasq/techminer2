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
    >>> from techminer2.co_occurrence_network.index_keywords import TermsToClustersMapping
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
    >>> pprint(mapping)  # doctest: +SKIP
    {'BLOCKCHAIN 02:0736': 0,
     'COMMERCE 03:0846': 0,
     'CYBER_SECURITY 02:0342': 1,
     'DESIGN_METHODOLOGY_APPROACH 02:0329': 1,
     'DEVELOPING_COUNTRIES 02:0248': 0,
     'ELECTRONIC_MONEY 03:0305': 2,
     'FINANCE 10:1866': 0,
     'FINANCIAL_INDUSTRIES 02:0323': 3,
     'FINANCIAL_INSTITUTION 02:0262': 2,
     'FINANCIAL_SERVICE 05:1115': 0,
     'FINANCIAL_SERVICES_INDUSTRIES 02:0696': 0,
     'FINANCIAL_SYSTEM 02:0385': 1,
     'FINTECH 10:1412': 2,
     'INFORMATION_SYSTEMS 02:0235': 2,
     'INVESTMENT 02:0418': 1,
     'PERCEIVED_USEFULNESS 02:0346': 1,
     'SALES 02:0329': 1,
     'SECURITY_AND_PRIVACY 02:0323': 3,
     'SURVEYS 03:0484': 3,
     'SUSTAINABLE_DEVELOPMENT 03:0227': 0}


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
    >>> pprint(mapping)  # doctest: +SKIP
    {'BLOCKCHAIN': 0,
     'COMMERCE': 0,
     'CYBER_SECURITY': 1,
     'DESIGN_METHODOLOGY_APPROACH': 1,
     'DEVELOPING_COUNTRIES': 0,
     'ELECTRONIC_MONEY': 2,
     'FINANCE': 0,
     'FINANCIAL_INDUSTRIES': 3,
     'FINANCIAL_INSTITUTION': 2,
     'FINANCIAL_SERVICE': 0,
     'FINANCIAL_SERVICES_INDUSTRIES': 0,
     'FINANCIAL_SYSTEM': 1,
     'FINTECH': 2,
     'INFORMATION_SYSTEMS': 2,
     'INVESTMENT': 1,
     'PERCEIVED_USEFULNESS': 1,
     'SALES': 1,
     'SECURITY_AND_PRIVACY': 3,
     'SURVEYS': 3,
     'SUSTAINABLE_DEVELOPMENT': 0}


"""
from techminer2._internals.mixins import ParamsMixin
from techminer2.networks.co_occurrence.usr.terms_to_clusters_mapping import (
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
            .with_field("index_keywords")
            .run()
        )
