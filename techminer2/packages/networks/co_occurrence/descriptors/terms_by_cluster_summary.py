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


>>> from techminer2.packages.networks.co_occurrence.descriptors import TermsByClusterSummary
>>> (
...     TermsByClusterSummary()
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
   Cluster  ...                                              Terms
0        0  ...  THIS_PAPER 14:2240; FINANCIAL_SERVICE 12:2100;...
1        1  ...  FINTECH 46:7183; FINANCE 21:3481; FINANCIAL_TE...
<BLANKLINE>
[2 rows x 4 columns]




"""
from ....._internals.mixins import ParamsMixin
from ..user.terms_by_cluster_summary import (
    TermsByClusterSummary as UserTermsByClusterSummary,
)


class TermsByClusterSummary(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        return (
            UserTermsByClusterSummary()
            .update(**self.params.__dict__)
            .with_field("descriptors")
            .run()
        )
