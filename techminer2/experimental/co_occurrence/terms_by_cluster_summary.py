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
    >>> from techminer2.experimental.co_occurrence import TermsByClusterSummary
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
    ...     .using_minimum_terms_in_cluster(5)
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
    0        0  ...  FINANCIAL_TECHNOLOGIES 14:2005; FINANCIAL_SERV...
    1        1  ...  FINTECH 44:6942; FINANCE 21:3481; TECHNOLOGIES...
    2        2  ...     BANKS 09:1133; DATA 07:1086; CONSUMERS 07:0925
    3        3  ...                  THE_IMPACT 06:0908; CHINA 06:0673
    4        4  ...               SERVICES 07:1226; INVESTMENT 06:1294
    5        5  ...       PRACTITIONER 06:1194; BUSINESS_MODEL 05:1578
    <BLANKLINE>
    [6 rows x 4 columns]



"""
from ..._internals.mixins import ParamsMixin
from ...packages.networks.co_occurrence.descriptors import (
    TermsByClusterSummary as ClassicalTermsByClusterSummary,
)
from .mixins import RecursiveClusteringMixin


class TermsByClusterSummary(
    ParamsMixin,
    RecursiveClusteringMixin,
):
    """:meta private:"""

    #
    # NOTIFICATIONS:
    # -------------------------------------------------------------------------
    def internal__notify_process_start(self):
        pass

    # -------------------------------------------------------------------------
    def internal__notify_process_end(self):

        if not self.params.quiet:
            pass

    #
    # ALGORITHM:
    # -------------------------------------------------------------------------
    def internal__build_final_dataframe(self):

        equivalence = {t.split(" ")[0]: t for t in self.terms_with_metrics}
        mapping = {}

        for i, terms in enumerate(self.discovered_clusters):
            for term in terms:
                key = equivalence[term]
                mapping[key] = i

        self.data_frame = (
            ClassicalTermsByClusterSummary()
            .update(**self.params.__dict__)
            #
            .using_clustering_algorithm_or_dict(mapping)
            #
            .having_terms_in_top(None)
            .having_terms_ordered_by("OCC")
            .having_term_occurrences_between(None, None)
            .having_term_citations_between(None, None)
            .having_terms_in(self.selected_terms)
            #
            .run()
        )

    # -------------------------------------------------------------------------
    def run(self):
        """:meta private:"""

        self.internal__notify_process_start()
        self.internal__computer_recursive_clusters()
        self.internal__build_final_dataframe()
        self.internal__notify_process_end()

        return self.data_frame
