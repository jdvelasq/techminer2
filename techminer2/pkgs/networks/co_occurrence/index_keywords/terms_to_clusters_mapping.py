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


>>> from techminer2.pkgs.networks.co_occurrence.index_keywords import TermsToClustersMapping
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
...     .where_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     .where_records_match(None)
...     #
...     .build()
... )
>>> from pprint import pprint
>>> pprint(mapping)
{'BLOCKCHAIN 02:0736': 0,
 'COMMERCE 03:0846': 0,
 'CYBER_SECURITY 02:0342': 2,
 'DESIGN_METHODOLOGY_APPROACH 02:0329': 1,
 'DEVELOPING_COUNTRIES 02:0248': 0,
 'ELECTRONIC_MONEY 03:0305': 1,
 'FINANCE 10:1866': 0,
 'FINANCIAL_INDUSTRY 02:0323': 2,
 'FINANCIAL_INSTITUTION 02:0262': 1,
 'FINANCIAL_SERVICE 04:1036': 0,
 'FINANCIAL_SERVICES_INDUSTRIES 02:0696': 0,
 'FINANCIAL_SYSTEM 02:0385': 0,
 'FINTECH 10:1412': 1,
 'INFORMATION_SYSTEMS 02:0235': 1,
 'PERCEIVED_USEFULNESS 02:0346': 1,
 'SALES 02:0329': 1,
 'SECURITY_AND_PRIVACY 02:0323': 2,
 'SURVEYS 03:0484': 2,
 'SUSTAINABLE_DEVELOPMENT 03:0227': 0,
 'THEORETICAL_FRAMEWORK 02:0206': 1}





"""
from .....internals.mixins import InputFunctionsMixin
from ..user.terms_to_clusters_mapping import (
    TermsToClustersMapping as UserTermsToClusterMapping,
)


class TermsToClustersMapping(
    InputFunctionsMixin,
):
    """:meta private:"""

    def build(self):
        """:meta private:"""

        return (
            UserTermsToClusterMapping()
            .update_params(**self.params.__dict__)
            .with_field("index_keywords")
            .build()
        )
