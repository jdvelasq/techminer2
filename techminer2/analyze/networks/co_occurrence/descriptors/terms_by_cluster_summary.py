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
    >>> from techminer2.co_occurrence_network.descriptors import TermsByClusterSummary
    >>> df = (
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
    ...     .where_root_directory("examples/tests/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> df # doctest: +SKIP
       Cluster  ...                                              Terms
    0        0  ...  FINTECH 38:6131; THE_FINANCIAL_INDUSTRY 09:200...
    1        1  ...  TECHNOLOGIES 15:1633; FINANCIAL_TECHNOLOGIES 1...
    <BLANKLINE>
    [2 rows x 4 columns]


"""
from techminer2._internals import ParamsMixin
from techminer2.analyze.networks.co_occurrence.usr.terms_by_cluster_summary import (
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
