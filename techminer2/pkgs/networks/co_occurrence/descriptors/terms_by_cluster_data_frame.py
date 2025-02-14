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


>>> from techminer2.pkgs.networks.co_occurrence.descriptors import TermsByClusterDataFrame
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
...     .where_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     .where_records_match(None)
...     #
...     .build()
... )
                                          0                               1
0                        THIS_PAPER 14:2240                 FINTECH 46:7183
1                FINANCIAL_SERVICES 11:1862                 FINANCE 21:3481
2                          SERVICES 09:1527    FINANCIAL_TECHNOLOGY 17:2359
3                             BANKS 09:1133              THIS_STUDY 14:1737
4                        REGULATORS 08:0974              INNOVATION 13:2394
5                              DATA 07:1086              TECHNOLOGY 13:1594
6                   THE_DEVELOPMENT 07:1073  THE_FINANCIAL_INDUSTRY 09:2006
7                           BANKING 07:0851            THIS_ARTICLE 06:1360
8   THE_FINANCIAL_SERVICES_INDUSTRY 06:1237               THE_FIELD 06:1031
9                       THE_PURPOSE 06:1046                                
10                        CONSUMERS 06:0804                                


"""
from .....internals.mixins import ParamsMixin
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
            .update_params(**self.params.__dict__)
            .with_field("descriptors")
            .build()
        )
