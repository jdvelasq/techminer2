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


>>> from techminer2.pkgs.networks.co_occurrence.author_keywords import TermsToClustersMapping
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
{'ARTIFICIAL_INTELLIGENCE 02:0327': 3,
 'BANKING 02:0291': 1,
 'BLOCKCHAIN 02:0305': 0,
 'BUSINESS_MODELS 02:0759': 0,
 'CASE_STUDY 02:0340': 0,
 'CROWDFUNDING 03:0335': 0,
 'CYBER_SECURITY 02:0342': 0,
 'FINANCE 02:0309': 3,
 'FINANCIAL_INCLUSION 03:0590': 0,
 'FINANCIAL_SERVICES 04:0667': 1,
 'FINANCIAL_TECHNOLOGY 03:0461': 1,
 'FINTECH 31:5168': 0,
 'INNOVATION 07:0911': 1,
 'LENDINGCLUB 02:0253': 2,
 'MARKETPLACE_LENDING 03:0317': 2,
 'PEER_TO_PEER_LENDING 02:0253': 2,
 'REGTECH 02:0266': 0,
 'ROBOTS 02:0289': 3,
 'SHADOW_BANKING 02:0253': 2,
 'TECHNOLOGY 02:0310': 1}



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
            .with_field("author_keywords")
            .build()
        )
