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
    >>> from techminer2.packages.networks.coupling.documents import TermsByClusterDataFrame
    >>> (
    ...     TermsByClusterDataFrame()
    ...     #
    ...     # UNIT OF ANALYSIS:
    ...     .having_terms_in_top(20)
    ...     .having_citation_threshold(0)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering_algorithm_or_dict("louvain")
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
                                                0  ...                                       3
    0    Gomber P., 2018, J MANAGE INF SYST 1:576  ...  Jagtiani J., 2019, FINANC MANAGE 1:097
    1  Anagnostopoulos I., 2018, J ECON BUS 1:202  ...     Jagtiani J., 2018, J ECON BUS 1:064
    2           Alt R., 2018, ELECTRON MARK 1:150  ...
    3    Gozman D., 2018, J MANAGE INF SYST 1:120  ...
    4  Iman N., 2018, ELECT COMMER RES APPL 1:102  ...
    5         Zhao Q., 2019, SUSTAINABILITY 1:079  ...
    <BLANKLINE>
    [6 rows x 4 columns]


"""
from ....._internals.mixins import ParamsMixin
from ....._internals.nx import (
    internal__cluster_nx_graph,
    internal__extract_communities_to_frame,
)
from .._internals.from_documents.create_nx_graph import internal__create_nx_graph


class TermsByClusterDataFrame(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        nx_graph = internal__create_nx_graph(self.params)
        nx_graph = internal__cluster_nx_graph(params=self.params, nx_graph=nx_graph)
        return internal__extract_communities_to_frame(
            params=self.params, nx_graph=nx_graph
        )
