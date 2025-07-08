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
    >>> from techminer2.packages.networks.co_occurrence.descriptors import TermsToClustersMapping
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
    ...     .where_root_directory_is("example/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> from pprint import pprint
    >>> pprint(mapping)
    {'BANKING 07:0851': 0,
     'BANKS 09:1133': 2,
     'BUSINESS_MODEL 05:1578': 0,
     'CHINA 06:0673': 1,
     'CONSUMERS 07:0925': 2,
     'DATA 07:1086': 2,
     'FINANCE 21:3481': 1,
     'FINANCIAL_SERVICE 12:2100': 0,
     'FINANCIAL_TECHNOLOGIES 14:2005': 0,
     'FINTECH 44:6942': 1,
     'INNOVATION 15:2741': 1,
     'INVESTMENT 06:1294': 0,
     'PRACTITIONER 06:1194': 0,
     'REGULATORS 08:0974': 0,
     'SERVICES 07:1226': 0,
     'TECHNOLOGIES 17:1943': 1,
     'THE_DEVELOPMENT 09:1293': 0,
     'THE_FINANCIAL_INDUSTRY 09:2006': 1,
     'THE_FINANCIAL_SERVICES_INDUSTRY 06:1237': 0,
     'THE_IMPACT 06:0908': 1}


Example:
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
    ...     .where_root_directory_is("example/")
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
     'BANKS': 2,
     'BUSINESS_MODEL': 0,
     'CHINA': 1,
     'CONSUMERS': 2,
     'DATA': 2,
     'FINANCE': 1,
     'FINANCIAL_SERVICE': 0,
     'FINANCIAL_TECHNOLOGIES': 0,
     'FINTECH': 1,
     'INNOVATION': 1,
     'INVESTMENT': 0,
     'PRACTITIONER': 0,
     'REGULATORS': 0,
     'SERVICES': 0,
     'TECHNOLOGIES': 1,
     'THE_DEVELOPMENT': 0,
     'THE_FINANCIAL_INDUSTRY': 1,
     'THE_FINANCIAL_SERVICES_INDUSTRY': 0,
     'THE_IMPACT': 1}


"""
from ....._internals.mixins import ParamsMixin
from ..user.terms_to_clusters_mapping import (
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
