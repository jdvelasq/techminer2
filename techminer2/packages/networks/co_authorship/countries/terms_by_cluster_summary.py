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
    >>> from techminer2.packages.networks.co_authorship.countries import TermsByClusterSummary
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
    0        0  ...  United States 16:3189; China 08:1085; South Ko...
    1        1  ...  Germany 07:1814; Netherlands 03:0300; Denmark ...
    2        2  ...  Australia 05:0783; United Kingdom 03:0636; Hon...
    3        3  ...                                Switzerland 04:0660
    4        4  ...                                     Latvia 02:0163
    5        5  ...                                      Spain 01:0225
    6        6  ...                                  Indonesia 01:0102
    7        7  ...                                   Slovenia 01:0102
    8        8  ...                          Brunei Darussalam 01:0090
    <BLANKLINE>
    [9 rows x 4 columns]




"""
from ....._internals.mixins import ParamsMixin
from ...co_occurrence.user.terms_by_cluster_summary import (
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
            .with_field("countries")
            .run()
        )
