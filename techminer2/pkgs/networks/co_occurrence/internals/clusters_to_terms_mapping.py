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


## >>> from techminer2.pkgs.co_occurrence_network import ClustersToTermsMapping
## >>> mapping = (
## ...     ClustersToTermsMapping()
## ...     #
## ...     # FIELD:
## ...     .with_field("author_keywords")
## ...     .having_terms_in_top(10)
## ...     .having_terms_ordered_by("OCC")
## ...     .having_term_occurrences_between(None, None)
## ...     .having_term_citations_between(None, None)
## ...     .having_terms_in(None)
## ...     #
## ...     # COUNTERS:
## ...     .using_term_counters(True)
## ...     #
## ...     # NETWORK:
## ...     .using_clustering_algorithm_or_dict("louvain")
## ...     .using_association_index("association")
## ...     #
## ...     # DATABASE:
## ...     .where_directory_is("example/")
## ...     .where_database_is("main")
## ...     .where_record_years_between(None, None)
## ...     .where_record_citations_between(None, None)
## ...     .where_records_match(None)
## ...     #
## ...     .build()
## ... )
## >>> from pprint import pprint
## >>> pprint(mapping)
{0: ['FINTECH 31:5168',
     'FINANCIAL_INCLUSION 03:0590',
     'CROWDFUNDING 03:0335',
     'BUSINESS_MODELS 02:0759',
     'CYBER_SECURITY 02:0342',
     'CASE_STUDY 02:0340',
     'BLOCKCHAIN 02:0305',
     'REGTECH 02:0266'],
 1: ['INNOVATION 07:0911',
     'FINANCIAL_SERVICES 04:0667',
     'FINANCIAL_TECHNOLOGY 03:0461',
     'TECHNOLOGY 02:0310',
     'BANKING 02:0291'],
 2: ['MARKETPLACE_LENDING 03:0317',
     'LENDINGCLUB 02:0253',
     'PEER_TO_PEER_LENDING 02:0253',
     'SHADOW_BANKING 02:0253'],
 3: ['ARTIFICIAL_INTELLIGENCE 02:0327', 'FINANCE 02:0309', 'ROBOTS 02:0289']}


"""
from .....internals.mixins import InputFunctionsMixin
from .....internals.nx import (
    internal__cluster_nx_graph,
    internal__create_clusters_to_terms_mapping,
)
from .create_nx_graph import internal__create_nx_graph


class InternalClustersToTermsMapping(
    InputFunctionsMixin,
):
    """:meta private:"""

    def build(self):
        """:meta private:"""

        nx_graph = internal__create_nx_graph(self.params)
        nx_graph = internal__cluster_nx_graph(self.params, nx_graph)
        mapping = internal__create_clusters_to_terms_mapping(self.params, nx_graph)

        return mapping
