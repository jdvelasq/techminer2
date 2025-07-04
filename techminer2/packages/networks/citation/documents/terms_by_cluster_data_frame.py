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
    >>> from techminer2.packages.networks.citation.documents import TermsByClusterDataFrame
    >>> (
    ...     TermsByClusterDataFrame()
    ...     #
    ...     # UNIT OF ANALYSIS:
    ...     .having_terms_in_top(30)
    ...     .having_citation_threshold(0)
    ...     .using_term_counters(True)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering_algorithm_or_dict("louvain")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory_is("example/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... ).head()
                                                       0  ...                                                  3
    0    Gabor D., 2017, NEW POLIT ECON, V22, P423 1:314  ...  Anagnostopoulos I., 2018, J ECON BUS, V100, P7...
    1  Gai K., 2018, J NETWORK COMPUT APPL, V103, P26...  ...     Zavolokina L., 2016, FINANCIAL INNOV, V2 1:106
    2  Gracia D.B., 2019, IND MANAGE DATA SYS, V119, ...  ...
    3   Leong C., 2017, INT J INF MANAGE, V37, P92 1:180  ...
    4                   Hu Z., 2019, SYMMETRY, V11 1:176  ...
    <BLANKLINE>
    [5 rows x 4 columns]


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
        """:meta private:"""

        nx_graph = internal__create_nx_graph(self.params)
        nx_graph = internal__cluster_nx_graph(self.params, nx_graph)
        return internal__extract_communities_to_frame(self.params, nx_graph)
