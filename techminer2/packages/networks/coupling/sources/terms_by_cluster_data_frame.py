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
    >>> from techminer2.packages.networks.coupling.sources import TermsByClusterDataFrame

    >>> df = (
    ...     TermsByClusterDataFrame()
    ...     #
    ...     # UNIT OF ANALYSIS:
    ...     .having_terms_in_top(20)
    ...     .having_citation_threshold(0)
    ...     .having_occurrence_threshold(2)
    ...     .having_terms_in(None)
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


    >>> # Display the resulting data frame
    >>> print(df)  # doctest: +NORMALIZE_WHITESPACE
                                                0                                                1
    0  Industrial Management and Data Systems 2:386          Journal of Economics and Business 3:422
    1                      Electronic Markets 2:287  Journal of Management Information Systems 2:696
    2            Sustainability (Switzerland) 2:150                       Financial Management 2:161
    3        Journal of Innovation Management 1:226
    4                                Symmetry 1:176



"""
from ....._internals.mixins import ParamsMixin
from .._internals.from_others.terms_by_cluster_data_frame import (
    InternalTermsByClusterDataFrame,
)


class TermsByClusterDataFrame(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        return (
            InternalTermsByClusterDataFrame()
            .update(**self.params.__dict__)
            .unit_of_analysis("source_title")
            .run()
        )
