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
    >>> from techminer2.thesaurus.descriptors import ApplyThesaurus, InitializeThesaurus

    >>> # Restore the column values to initial values
    >>> InitializeThesaurus(root_directory="example/", quiet=True).run()
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
                                             0                               1                  2
    0           FINANCIAL_TECHNOLOGIES 14:2005                 FINTECH 44:6942      BANKS 09:1133
    1                FINANCIAL_SERVICE 12:2100                 FINANCE 21:3481       DATA 07:1086
    2                  THE_DEVELOPMENT 09:1293            TECHNOLOGIES 17:1943  CONSUMERS 07:0925
    3                       REGULATORS 08:0974              INNOVATION 15:2741
    4                         SERVICES 07:1226  THE_FINANCIAL_INDUSTRY 09:2006
    5                          BANKING 07:0851              THE_IMPACT 06:0908
    6                       INVESTMENT 06:1294                   CHINA 06:0673
    7  THE_FINANCIAL_SERVICES_INDUSTRY 06:1237
    8                     PRACTITIONER 06:1194
    9                   BUSINESS_MODEL 05:1578


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
