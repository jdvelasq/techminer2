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
    >>> from techminer2.packages.networks.co_authorship.authors import TermsByClusterSummary
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
    0        0  ...  Gomber P. 2:1065; Kauffman R.J. 1:0576; Parker...
    1        1  ...        Gai K. 2:0323; Qiu M. 2:0323; Sun X. 2:0323
    2        2  ...  Dolata M. 2:0181; Schwabe G. 2:0181; Zavolokin...
    3        3  ...  Buchak G. 1:0390; Matvos G. 1:0390; Piskorski ...
    4        4  ...              Jagtiani J. 3:0317; Lemieux C. 2:0253
    5        5  ...                    Lee I. 1:0557; Shin Y.J. 1:0557
    6        6  ...                                   Hornuf L. 2:0358
    <BLANKLINE>
    [7 rows x 4 columns]



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
            .with_field("authors")
            .run()
        )
