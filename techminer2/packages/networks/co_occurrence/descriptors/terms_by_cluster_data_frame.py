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
    >>> from techminer2.packages.networks.co_occurrence.descriptors import TermsByClusterDataFrame
    >>> from techminer2.thesaurus.descriptors import ApplyThesaurus, CreateThesaurus

    >>> # Restore the column values to initial values
    >>> CreateThesaurus(root_directory="example/", quiet=True).run()
    >>> ApplyThesaurus(root_directory="example/", quiet=True).run()

    >>> # Generate terms by cluster data frame
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
    ...     .where_root_directory_is("example/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )

    >>> # Display the resulting data frame
    >>> print(df.to_string()) # doctest: +NORMALIZE_WHITESPACE
                                              0                               1
    0                        THIS_PAPER 14:2240                 FINTECH 46:7183
    1                 FINANCIAL_SERVICE 12:2100                 FINANCE 21:3481
    2                          SERVICES 09:1527  FINANCIAL_TECHNOLOGIES 18:2455
    3                             BANKS 09:1133              INNOVATION 16:2845
    4                   THE_DEVELOPMENT 08:1173            TECHNOLOGIES 15:1810
    5                        REGULATORS 08:0974              THIS_STUDY 14:1737
    6                              DATA 07:1086  THE_FINANCIAL_INDUSTRY 09:2006
    7                           BANKING 07:0851            THIS_ARTICLE 06:1360
    8                        THE_AUTHOR 07:0828
    9                        INVESTMENT 06:1294
    10  THE_FINANCIAL_SERVICES_INDUSTRY 06:1237
    11                      THE_PURPOSE 06:1046


"""
from ....._internals.mixins import ParamsMixin
from ..user.terms_by_cluster_data_frame import (
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
            .with_field("descriptors")
            .run()
        )
