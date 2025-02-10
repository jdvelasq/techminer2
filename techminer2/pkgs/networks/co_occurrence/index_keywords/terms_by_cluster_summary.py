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


>>> from techminer2.pkgs.networks.co_occurrence.index_keywords import TermsByClusterSummary
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
...     .where_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     .where_records_match(None)
...     #
...     .build()
... )
   Cluster  ...                                              Terms
0        0  ...  FINANCE 10:1866; FINANCIAL_SERVICE 04:1036; CO...
1        1  ...  FINTECH 10:1412; ELECTRONIC_MONEY 03:0305; PER...
2        2  ...  SURVEYS 03:0484; CYBER_SECURITY 02:0342; FINAN...
<BLANKLINE>
[3 rows x 4 columns]





"""
from .....internals.mixins import InputFunctionsMixin
from ..user.terms_by_cluster_summary import (
    TermsByClusterSummary as UserTermsByClusterSummary,
)


class TermsByClusterSummary(
    InputFunctionsMixin,
):
    """:meta private:"""

    def build(self):
        """:meta private:"""

        return (
            UserTermsByClusterSummary()
            .update_params(**self.params.__dict__)
            .with_field("index_keywords")
            .build()
        )
