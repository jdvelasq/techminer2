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

## >>> from techminer2.pkgs.networks.citations.articles import TermsByClusterDataFrame
## >>> (
## ...     TermsByClusterDataFrame()
## ...     #
## ...     # UNIT OF ANALYSIS:
## ...     .having_terms_in_top(30)
## ...     .having_citation_threshold(0)
## ...     #
## ...     # CLUSTERING:
## ...     .using_clustering_algorithm_or_dict("louvain")
## ...     #
## ...     # DATABASE:
## ...     .where_directory_is("example/")
## ...     .where_database_is("main")
## ...     .where_record_years_between(None, None)
## ...     .where_record_citations_between(None, None)
## ...     .where_records_match(None)
## ...     #
## ...     .build()
## ... ).head()




"""
from .....internals.mixins import InputFunctionsMixin
from .....internals.nx import (
    internal__cluster_network_graph,
    internal__extract_communities_to_frame,
)
from ..internals.from_articles.create_nx_graph import internal__create_nx_graph


class TermsByClusterDataFrame(
    InputFunctionsMixin,
):
    """:meta private:"""

    def build(self):
        """:meta private:"""

        nx_graph = internal__create_nx_graph(self.params)
        nx_graph = internal__cluster_network_graph(self.params, nx_graph)
        return internal__extract_communities_to_frame(self.params, nx_graph)
