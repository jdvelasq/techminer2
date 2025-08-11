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
    >>> from techminer2.packages.networks.co_citation.cited_references import TermsByClusterDataFrame
    >>> (
    ...     TermsByClusterDataFrame()
    ...     #
    ...     # UNIT OF ANALYSIS:
    ...     .having_terms_in_top(30)
    ...     .having_citation_threshold(0)
    ...     .having_terms_in(None)
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
    ... ).head(10)
                                               0  ...                                         2
    0   Zavolokina L., 2016, FINANCIAL INNOV 1:3  ...         Jagtiani J., 2018, J ECON BUS 1:2
    1         Gabor D., 2017, NEW POLIT ECON 1:2  ...  Anagnostopoulos I., 2018, J ECON BUS 1:1
    2   Ryu H.-S., 2018, IND MANAGE DATA SYS 1:2  ...
    3            Alt R., 2018, ELECTRON MARK 1:1  ...
    4    Gai K., 2018, J NETWORK COMPUT APPL 1:1  ...
    5           Li Y., 2017, FINANCIAL INNOV 1:1  ...
    6  Stewart H., 2018, INF COMPUT SECURITY 1:1  ...
    <BLANKLINE>
    [7 rows x 3 columns]




"""
from techminer2._internals.mixins import ParamsMixin
from techminer2.packages.networks.co_citation._internals.terms_by_cluster_data_frame import (
    TermsByClusterDataFrame as InternalTermsByClusterDataFrame,
)


class TermsByClusterDataFrame(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        return (
            InternalTermsByClusterDataFrame()
            .update(**self.params.__dict__)
            .unit_of_analysis("cited_references")
            .run()
        )
