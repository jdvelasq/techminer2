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
    >>> InitializeThesaurus(root_directory="examples/fintech/", quiet=True).run()
    >>> ApplyThesaurus(root_directory="examples/fintech/", quiet=True).run()

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
    ...     .where_root_directory_is("examples/fintech/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )

    >>> # Display the resulting data frame
    >>> print(df.to_string()) # doctest: +SKIP
                                    0                                        1
    0                 FINTECH 38:6131                     TECHNOLOGIES 15:1633
    1  THE_FINANCIAL_INDUSTRY 09:2006           FINANCIAL_TECHNOLOGIES 12:1615
    2                   BANKS 08:1049                          FINANCE 10:1188
    3                    DATA 07:1086                  THE_DEVELOPMENT 09:1293
    4               CONSUMERS 07:0925                       INNOVATION 08:1816
    5            PRACTITIONER 06:1194                       REGULATORS 08:0974
    6              THE_IMPACT 06:0908  THE_FINANCIAL_SERVICES_INDUSTRY 06:1237
    7    THE_FINANCIAL_SECTOR 05:1147               FINANCIAL_SERVICES 06:1116
    8  INFORMATION_TECHNOLOGY 05:1101                         SERVICES 06:1089
    9       FINTECH_COMPANIES 05:1072                            CHINA 06:0673


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
            .with_field("descriptors")
            .run()
        )
