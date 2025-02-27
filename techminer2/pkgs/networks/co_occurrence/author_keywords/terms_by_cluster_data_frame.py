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


>>> from techminer2.pkgs.networks.co_occurrence.author_keywords import TermsByClusterDataFrame
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
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     .where_records_match(None)
...     #
...     .build()
... )
                             0  ...                                3
0              FINTECH 31:5168  ...  ARTIFICIAL_INTELLIGENCE 02:0327
1  FINANCIAL_INCLUSION 03:0590  ...                  FINANCE 02:0309
2         CROWDFUNDING 03:0335  ...                   ROBOTS 02:0289
3      BUSINESS_MODELS 02:0759  ...                                 
4       CYBER_SECURITY 02:0342  ...                                 
5           CASE_STUDY 02:0340  ...                                 
6           BLOCKCHAIN 02:0305  ...                                 
7              REGTECH 02:0266  ...                                 
<BLANKLINE>
[8 rows x 4 columns]


"""
from ....._internals.mixins import ParamsMixin
from ..user.terms_by_cluster_data_frame import (
    TermsByClusterDataFrame as UserTermsByClusterDataFrame,
)


class TermsByClusterDataFrame(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):
        """:meta private:"""

        return (
            UserTermsByClusterDataFrame()
            .update(**self.params.__dict__)
            .with_field("author_keywords")
            .build()
        )
