# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Node Degree Frame
===============================================================================


Example:
    >>> #
    >>> # TEST PREPARATION
    >>> #
    >>> from techminer2.thesaurus.descriptors import ApplyThesaurus, InitializeThesaurus
    >>> InitializeThesaurus(root_directory="example/", quiet=True).run()
    >>> ApplyThesaurus(root_directory="example/", quiet=True).run()



    >>> #
    >>> # CODE TESTED
    >>> #
    >>> from techminer2.packages.networks.co_occurrence.author_keywords import NodeDegreeDataFrame
    >>> (
    ...     NodeDegreeDataFrame()
    ...     #
    ...     # FIELD:
    ...     .having_terms_in_top(20)
    ...     .having_terms_ordered_by("OCC")
    ...     .having_term_occurrences_between(None, None)
    ...     .having_term_citations_between(None, None)
    ...     .having_terms_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_term_counters(True)
    ...     #
    ...     # NETWORK:
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
    ... ).head(15)
        Node                             Name  Degree
    0      0                  FINTECH 31:5168      18
    1      1        FINANCIAL_SERVICE 04:0667       8
    2      2               INNOVATION 07:0911       7
    3      3             TECHNOLOGIES 02:0310       6
    4      4               BLOCKCHAIN 03:0369       5
    5      5    FINANCIAL_INSTITUTION 02:0484       5
    6      6                  FINANCE 02:0309       5
    7      7                   ROBOTS 02:0289       5
    8      8                  REGTECH 02:0266       5
    9      9           BUSINESS_MODEL 03:0896       4
    10    10   FINANCIAL_TECHNOLOGIES 03:0461       4
    11    11                  BANKING 02:0291       4
    12    12      MARKETPLACE_LENDING 03:0317       3
    13    13             CASE_STUDIES 02:0340       3
    14    14  ARTIFICIAL_INTELLIGENCE 02:0327       3



>>> #
>>> # CODE TESTED
>>> #
>>> from techminer2.packages.networks.co_occurrence.author_keywords import NodeDegreeDataFrame
>>> (
...     NodeDegreeDataFrame()
...     #
...     # FIELD:
...     .having_terms_in_top(20)
...     .having_terms_ordered_by("OCC")
...     .having_term_occurrences_between(None, None)
...     .having_term_citations_between(None, None)
...     .having_terms_in(None)
...     #
...     # COUNTERS:
...     .using_term_counters(False)
...     #
...     # NETWORK:
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
... ).head(15)
    Node                             Name  Degree
0      0                  FINTECH 31:5168      18
1      1        FINANCIAL_SERVICE 04:0667       8
2      2               INNOVATION 07:0911       7
3      3             TECHNOLOGIES 02:0310       6
4      4               BLOCKCHAIN 03:0369       5
5      5    FINANCIAL_INSTITUTION 02:0484       5
6      6                  FINANCE 02:0309       5
7      7                   ROBOTS 02:0289       5
8      8                  REGTECH 02:0266       5
9      9           BUSINESS_MODEL 03:0896       4
10    10   FINANCIAL_TECHNOLOGIES 03:0461       4
11    11                  BANKING 02:0291       4
12    12      MARKETPLACE_LENDING 03:0317       3
13    13             CASE_STUDIES 02:0340       3
14    14  ARTIFICIAL_INTELLIGENCE 02:0327       3




"""
from ....._internals.mixins import ParamsMixin
from ..user.node_degree_data_frame import NodeDegreeDataFrame as UserNodeDegreeDataFrame


class NodeDegreeDataFrame(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        return (
            UserNodeDegreeDataFrame()
            .update(**self.params.__dict__)
            .with_field("author_keywords")
            .run()
        )
