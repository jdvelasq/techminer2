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
    >>> from techminer2.packages.networks.co_authorship.organizations import TermsByClusterSummary
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
    ...     .where_root_directory("examples/small/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
       Cluster  ...                                              Terms
    0        0  ...  Goethe Univ Frankfurt (DEU) 2:1065; Pennsylvan...
    1        1  ...  Columbia Grad Sch of Bus (USA) 1:0390; Univ of...
    2        2  ...  Baylor Univ (USA) 2:0395; Univ of New South Wa...
    3        3  ...  Fed Reserv Bank of Philadelphia (USA) 3:0317; ...
    4        4  ...  Hankyong Nac Univ (KOR) 1:0557; Western Illino...
    5        5  ...                        Univ of Zurich (CHE) 3:0434
    6        6  ...  Max Planck Inst for Innovation and Competition...
    7        7  ...                             Pace Univ (USA) 2:0323
    8        8  ...                     Sungkyunkwan Univ (KOR) 2:0307
    9        9  ...                        Univ of Latvia (LVA) 2:0163
    <BLANKLINE>
    [10 rows x 4 columns]




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
            .with_field("organizations")
            .run()
        )
