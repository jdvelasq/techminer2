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


Example:
    >>> from techminer2.packages.networks.co_occurrence.keywords import TermsByClusterSummary
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
    ...     .where_root_directory_is("examples/fintech/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
       Cluster  ...                                              Terms
    0        0  ...  FINTECH 32:5393; FINANCE 11:1950; FINANCIAL_SE...
    1        1  ...  FINANCIAL_TECHNOLOGIES 03:0461; CROWDFUNDING 0...
    2        2  ...  FINANCIAL_INSTITUTION 04:0746; COMMERCE 03:084...
    <BLANKLINE>
    [3 rows x 4 columns]


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
            .with_field("keywords")
            .run()
        )
