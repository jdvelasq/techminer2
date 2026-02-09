# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Terms by Cluster Data Frame
===============================================================================


Example:
    >>> from techminer2.co_occurrence_network.user import TermsByClusterDataFrame
    >>> (
    ...     TermsByClusterDataFrame()
    ...     #
    ...     # FIELD:
    ...     .with_field("raw_keywords")
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
                                   0  ...                                2
    0                FINTECH 32:5393  ...     FINANCIAL_TECHNOLOGY 03:0461
    1             INNOVATION 08:0990  ...             CROWDFUNDING 03:0335
    2     FINANCIAL_SERVICES 05:0746  ...           SUSTAINABILITY 03:0227
    3    FINANCIAL_INCLUSION 03:0590  ...  SUSTAINABLE_DEVELOPMENT 03:0227
    4  FINANCIAL_INSTITUTION 03:0488  ...        LITERATURE_REVIEW 02:0560
    5                SURVEYS 03:0484  ...
    6                BANKING 03:0370  ...
    7    MARKETPLACE_LENDING 03:0317  ...
    8       ELECTRONIC_MONEY 03:0305  ...
    <BLANKLINE>
    [9 rows x 3 columns]





"""
from techminer2._internals import ParamsMixin
from techminer2._internals.nx import (
    internal__cluster_nx_graph,
    internal__extract_communities_to_frame,
)
from techminer2.analyze.networks.co_occurrence._internals.create_nx_graph import (
    internal__create_nx_graph,
)


class TermsByClusterDataFrame(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        nx_graph = internal__create_nx_graph(self.params)
        nx_graph = internal__cluster_nx_graph(self.params, nx_graph)
        return internal__extract_communities_to_frame(self.params, nx_graph)

        nx_graph = internal__create_nx_graph(self.params)
        nx_graph = internal__cluster_nx_graph(self.params, nx_graph)
        return internal__extract_communities_to_frame(self.params, nx_graph)
