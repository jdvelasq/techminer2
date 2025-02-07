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

## >>> from techminer2.pkgs.networks.coupling.articles import TermsByClusterDataFrame
## >>> (
## ...     TermsByClusterDataFrame()
## ...     #
## ...     # UNIT OF ANALYSIS:
## ...     .having_terms_in_top(20)
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
## ... )




"""
from .....internals.mixins import InputFunctionsMixin
from .....internals.nx import (
    internal__cluster_nx_graph,
    internal__extract_communities_to_frame,
)
from ..internals.from_articles.create_nx_graph import internal__create_nx_graph


class TermsByClusterDataFrame(
    InputFunctionsMixin,
):
    """:meta private:"""

    def build(self):
        pass


def _terms_by_cluster_frame(
    #
    # ARTICLE PARAMS:
    top_n=None,
    citations_threshold=0,
    #
    # NETWORK PARAMS:
    algorithm_or_dict="louvain",
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):

    nx_graph = internal__create_nx_graph(
        #
        # COLUMN PARAMS:
        top_n=top_n,
        citations_threshold=citations_threshold,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    nx_graph = internal__cluster_nx_graph(
        #
        # FUNCTION PARAMS:
        nx_graph=nx_graph,
        #
        # NETWORK CLUSTERING:
        algorithm_or_dict=algorithm_or_dict,
    )

    return internal__extract_communities_to_frame(
        #
        # FUNCTION PARAMS:
        nx_graph=nx_graph,
        conserve_counters=True,
    )
