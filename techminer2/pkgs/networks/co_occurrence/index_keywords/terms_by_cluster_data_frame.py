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


>>> from techminer2.pkgs.networks.co_occurrence.index_keywords import TermsByClusterDataFrame
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
                                       0  ...                             2
0                        FINANCE 10:1866  ...               SURVEYS 03:0484
1              FINANCIAL_SERVICE 04:1036  ...        CYBER_SECURITY 02:0342
2                       COMMERCE 03:0846  ...    FINANCIAL_INDUSTRY 02:0323
3        SUSTAINABLE_DEVELOPMENT 03:0227  ...  SECURITY_AND_PRIVACY 02:0323
4                     BLOCKCHAIN 02:0736  ...                              
5  FINANCIAL_SERVICES_INDUSTRIES 02:0696  ...                              
6               FINANCIAL_SYSTEM 02:0385  ...                              
7           DEVELOPING_COUNTRIES 02:0248  ...                              
<BLANKLINE>
[8 rows x 3 columns]


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
            .with_field("index_keywords")
            .build()
        )
