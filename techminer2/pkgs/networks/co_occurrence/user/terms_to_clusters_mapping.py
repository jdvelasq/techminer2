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


>>> from techminer2.pkgs.networks.co_occurrence.user import TermsToClustersMapping
>>> mapping = (
...     TermsToClustersMapping()
...     #
...     # FIELD:
...     .with_field("author_keywords")
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
from ....._internals.mixins import ParamsMixin
from ....._internals.nx import (
    internal__cluster_nx_graph,
    internal__create_terms_to_clusters_mapping,
)
from .._internals.create_nx_graph import internal__create_nx_graph


class TermsToClustersMapping(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        nx_graph = internal__create_nx_graph(self.params)
        nx_graph = internal__cluster_nx_graph(self.params, nx_graph)
        return internal__create_terms_to_clusters_mapping(self.params, nx_graph)
