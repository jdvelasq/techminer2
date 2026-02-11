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


Smoke tests:
    >>> from techminer2.analyze.experimental.emergence import TermsByClusterSummary
    >>> df = (
    ...     TermsByClusterSummary()
    ...     #
    ...     # EMERGENCE:
    ...     .using_baseline_periods(3)
    ...     .using_recent_periods(3)
    ...     .using_novelty_threshold(0.15)
    ...     .using_total_records_threshold(7)
    ...     .using_periods_with_at_least_one_record(3)
    ...     .using_ratio_threshold(0.5)
    ...     #
    ...     # NETWORK:
    ...     .using_clustering_algorithm_or_dict("louvain")
    ...     .using_association_index("association")
    ...     .using_minimum_terms_in_cluster(5)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("examples/small/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> df # doctest: +SKIP
       Cluster  ...                                              Terms
    0        0  ...  FINANCIAL_TECHNOLOGIES 12:1615; BANKS 08:1049;...
    <BLANKLINE>
    [1 rows x 4 columns]


"""
from techminer2._internals import ParamsMixin
from techminer2.analyze.experimental.emergence.mixins import RecursiveClusteringMixin
from techminer2.analyze.networks.co_occurrence.descriptors import (
    TermsByClusterSummary as ClassicalTermsByClusterSummary,
)


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
            .having_items_in_top(None)
            .having_items_ordered_by("OCC")
            .having_item_occurrences_between(None, None)
            .having_item_citations_between(None, None)
            .having_items_in(self.selected_terms)
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


#
