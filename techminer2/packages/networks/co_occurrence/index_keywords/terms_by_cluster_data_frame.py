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


Example:
    >>> from techminer2.packages.networks.co_occurrence.index_keywords import TermsByClusterDataFrame
    >>> df = (
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
    ...     .where_root_directory_is("examples/fintech/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> df   # doctest: +SKIP
                                           0  ...                             3
    0                        FINANCE 10:1866  ...               SURVEYS 03:0484
    1              FINANCIAL_SERVICE 05:1115  ...  FINANCIAL_INDUSTRIES 02:0323
    2                       COMMERCE 03:0846  ...  SECURITY_AND_PRIVACY 02:0323
    3        SUSTAINABLE_DEVELOPMENT 03:0227  ...
    4                     BLOCKCHAIN 02:0736  ...
    5  FINANCIAL_SERVICES_INDUSTRIES 02:0696  ...
    6           DEVELOPING_COUNTRIES 02:0248  ...
    <BLANKLINE>
    [7 rows x 4 columns]



"""
from techminer2._internals.mixins import ParamsMixin
from techminer2.packages.networks.co_occurrence.user.terms_by_cluster_data_frame import (
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
            .with_field("index_keywords")
            .run()
        )
