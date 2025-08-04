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
    >>> from techminer2.packages.networks.coupling.organizations  import NodeDegreeDataFrame

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
    ...     .where_root_directory_is("examples/fintech/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... ).head(15)


    >>> # Display the resulting data frame
    >>> print(df)  # doctest: +NORMALIZE_WHITESPACE
    Node                                               Name  Degree
    0     0                 Goethe Univ Frankfurt (DEU) 2:1065       4
    1     1                        Univ of Sydney (AUS) 2:0300       4
    2     2               Pennsylvania State Univ (USA) 1:0576       4
    3     3            Singapore Manag Univ (SMU) (SGP) 1:0576       4
    4     4                      Univ of Delaware (USA) 1:0576       4
    5     5       Fed Reserv Bank of Philadelphia (USA) 3:0317       1
    6     6  Max Planck Inst for Innovation and Competition...       1
    7     7                     Sungkyunkwan Univ (KOR) 2:0307       1
    8     8            Fed Reserv Bank of Chicago (USA) 2:0253       1

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
    ...     .where_root_directory_is("examples/fintech/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... ).head(15)

    >>> # Display the resulting data frame
    >>> print(df)  # doctest: +NORMALIZE_WHITESPACE
       Node                                               Name  Degree
    0     0                 Goethe Univ Frankfurt (DEU) 2:1065       4
    1     1                        Univ of Sydney (AUS) 2:0300       4
    2     2               Pennsylvania State Univ (USA) 1:0576       4
    3     3            Singapore Manag Univ (SMU) (SGP) 1:0576       4
    4     4                      Univ of Delaware (USA) 1:0576       4
    5     5       Fed Reserv Bank of Philadelphia (USA) 3:0317       1
    6     6  Max Planck Inst for Innovation and Competition...       1
    7     7                     Sungkyunkwan Univ (KOR) 2:0307       1
    8     8            Fed Reserv Bank of Chicago (USA) 2:0253       1



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
            .update(terms_order_by="OCC")
            .unit_of_analysis("organizations")
            .run()
        )
