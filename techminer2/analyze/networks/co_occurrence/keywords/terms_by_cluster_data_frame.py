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


Smoke tests:
    >>> from techminer2.co_occurrence_network.keywords import TermsByClusterDataFrame
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
    ...     .where_root_directory("examples/small/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> df  # doctest: +SKIP
                                            0  ...                              2
    0                         FINTECH 32:5393  ...  FINANCIAL_INSTITUTION 04:0746
    1                         FINANCE 11:1950  ...               COMMERCE 03:0846
    2               FINANCIAL_SERVICE 08:1680  ...    FINANCIAL_INCLUSION 03:0590
    3                      INNOVATION 08:0990  ...   DIGITAL_TECHNOLOGIES 02:0494
    4                  BUSINESS_MODEL 04:1472  ...
    5                      BLOCKCHAIN 04:0945  ...
    6   FINANCIAL_SERVICES_INDUSTRIES 03:0949  ...
    7                         SURVEYS 03:0484  ...
    8                         BANKING 03:0370  ...
    9             MARKETPLACE_LENDING 03:0317  ...
    10               ELECTRONIC_MONEY 03:0305  ...
    <BLANKLINE>
    [11 rows x 3 columns]

"""
from techminer2._internals import ParamsMixin
from techminer2.analyze.networks.co_occurrence.usr.terms_by_cluster_data_frame import (
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
            .with_field("keywords")
            .run()
        )
