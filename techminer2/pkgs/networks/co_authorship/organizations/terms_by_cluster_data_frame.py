# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Terms by Cluster Frame
===============================================================================


>>> from techminer2.pkgs.networks.co_authorship.organizations import TermsByClusterDataFrame
>>> (
...     TermsByClusterDataFrame()
...     #
...     # FIELD:
...     .having_terms_in_top(20)
...     .having_terms_ordered_by("OCC")
...     .having_term_occurrences_between(None, None)
...     .having_term_citations_between(None, None)
...     .having_terms_in(None)
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
                                         0  ...                            9
0       Goethe Univ Frankfurt (DEU) 2:1065  ...  Univ of Latvia (LVA) 2:0163
1     Pennsylvania State Univ (USA) 1:0576  ...                             
2  Singapore Manag Univ (SMU) (SGP) 1:0576  ...                             
3            Univ of Delaware (USA) 1:0576  ...                             
<BLANKLINE>
[4 rows x 10 columns]

"""
from ....._internals.mixins import ParamsMixin
from ...co_occurrence.user.terms_by_cluster_data_frame import (
    TermsByClusterDataFrame as UserTermsByClusterDataFrame,
)


class TermsByClusterDataFrame(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        return (
            UserTermsByClusterDataFrame()
            .update(**self.params.__dict__)
            .with_field("organizations")
            .run()
        )
