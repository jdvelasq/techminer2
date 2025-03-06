# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Network Degree Frame
===============================================================================

Example:
    >>> from techminer2.packages.networks.coupling.sources  import NodeDegreeDataFrame

    >>> df = (
    ...     NodeDegreeDataFrame()
    ...     #
    ...     # UNIT OF ANALYSIS:
    ...     .having_terms_in_top(20)
    ...     .having_citation_threshold(0)
    ...     .having_occurrence_threshold(2)
    ...     .having_terms_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_term_counters(True)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory_is("example/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... ).head(15)

    >>> # Display the resulting data frame
    >>> print(df)  # doctest: +NORMALIZE_WHITESPACE
    Node                                             Name  Degree
    0     0                         Electronic Markets 2:287       5
    1     1          Journal of Economics and Business 3:422       4
    2     2     Industrial Management and Data Systems 2:386       3
    3     3                                   Symmetry 1:176       3
    4     4  Journal of Management Information Systems 2:696       2
    5     5               Sustainability (Switzerland) 2:150       2
    6     6           Journal of Innovation Management 1:226       2
    7     7                       Financial Management 2:161       1




    >>> df = (
    ...     NodeDegreeDataFrame()
    ...     #
    ...     # UNIT OF ANALYSIS:
    ...     .having_terms_in_top(20)
    ...     .having_citation_threshold(0)
    ...     .having_occurrence_threshold(2)
    ...     .having_terms_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_term_counters(False)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory_is("example/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... ).head(15)

    >>> # Display the resulting data frame
    >>> print(df)  # doctest: +NORMALIZE_WHITESPACE



"""
from ....._internals.mixins import ParamsMixin
from .._internals.from_others.node_degree_data_frame import InternalNodeDegreeDataFrame


class NodeDegreeDataFrame(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        return (
            InternalNodeDegreeDataFrame()
            .update(**self.params.__dict__)
            .unit_of_analysis("source_title")
            .run()
        )
