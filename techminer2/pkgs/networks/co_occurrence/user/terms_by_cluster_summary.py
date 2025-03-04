# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Terms by Cluster Summary
===============================================================================


>>> from techminer2.pkgs.networks.co_occurrence.user import TermsByClusterSummary
>>> (
...     TermsByClusterSummary()
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
   Cluster  ...                                              Terms
0        0  ...  FINTECH; FINANCIAL_INCLUSION; CROWDFUNDING; BU...
1        1  ...  INNOVATION; FINANCIAL_SERVICES; FINANCIAL_TECH...
2        2  ...  MARKETPLACE_LENDING; LENDINGCLUB; PEER_TO_PEER...
3        3  ...           ARTIFICIAL_INTELLIGENCE; FINANCE; ROBOTS
<BLANKLINE>
[4 rows x 4 columns]

>>> from techminer2.pkgs.networks.co_occurrence.user import TermsByClusterSummary
>>> (
...     TermsByClusterSummary()
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
   Cluster  ...                                              Terms
0        0  ...  FINTECH 31:5168; FINANCIAL_INCLUSION 03:0590; ...
1        1  ...  INNOVATION 07:0911; FINANCIAL_SERVICES 04:0667...
2        2  ...  MARKETPLACE_LENDING 03:0317; LENDINGCLUB 02:02...
3        3  ...  ARTIFICIAL_INTELLIGENCE 02:0327; FINANCE 02:03...
<BLANKLINE>
[4 rows x 4 columns]


"""
from ....._internals.mixins import ParamsMixin
from ....._internals.nx import (
    internal__cluster_nx_graph,
    internal__summarize_communities,
)
from .._internals.create_nx_graph import internal__create_nx_graph


class TermsByClusterSummary(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        nx_graph = internal__create_nx_graph(self.params)
        nx_graph = internal__cluster_nx_graph(self.params, nx_graph)
        return internal__summarize_communities(self.params, nx_graph)
