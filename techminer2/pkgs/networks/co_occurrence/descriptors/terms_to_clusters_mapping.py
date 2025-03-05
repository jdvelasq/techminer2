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


>>> from techminer2.pkgs.networks.co_occurrence.descriptors import TermsToClustersMapping
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
 'BANKS 09:1133': 0,
 'DATA 07:1086': 0,
 'FINANCE 21:3481': 1,
 'FINANCIAL_SERVICE 12:2100': 0,
 'FINANCIAL_TECHNOLOGIES 18:2455': 1,
 'FINTECH 46:7183': 1,
 'INNOVATION 16:2845': 1,
 'INVESTMENT 06:1294': 0,
 'REGULATORS 08:0974': 0,
 'SERVICES 09:1527': 0,
 'TECHNOLOGIES 15:1810': 1,
 'THE_AUTHOR 07:0828': 0,
 'THE_DEVELOPMENT 08:1173': 0,
 'THE_FINANCIAL_INDUSTRY 09:2006': 1,
 'THE_FINANCIAL_SERVICES_INDUSTRY 06:1237': 0,
 'THE_PURPOSE 06:1046': 0,
 'THIS_ARTICLE 06:1360': 1,
 'THIS_PAPER 14:2240': 0,
 'THIS_STUDY 14:1737': 1}

 
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
 'BANKS': 0,
 'DATA': 0,
 'FINANCE': 1,
 'FINANCIAL_SERVICE': 0,
 'FINANCIAL_TECHNOLOGIES': 1,
 'FINTECH': 1,
 'INNOVATION': 1,
 'INVESTMENT': 0,
 'REGULATORS': 0,
 'SERVICES': 0,
 'TECHNOLOGIES': 1,
 'THE_AUTHOR': 0,
 'THE_DEVELOPMENT': 0,
 'THE_FINANCIAL_INDUSTRY': 1,
 'THE_FINANCIAL_SERVICES_INDUSTRY': 0,
 'THE_PURPOSE': 0,
 'THIS_ARTICLE': 1,
 'THIS_PAPER': 0,
 'THIS_STUDY': 1}

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
