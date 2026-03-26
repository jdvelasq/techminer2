"""
ItemsByCluster
===============================================================================


Smoke tests:
    >>> from tm2p import CitationUnit
    >>> from tm2p.synthes.netw.cit import ItemsByCluster
    >>> df = (
    ...     ItemsByCluster()
    ...     #
    ...     # CITATION UNIT:
    ...     .with_citation_unit(CitationUnit.DOC)
    ...     .having_items_in_top(30)
    ...     .having_items_in(None)
    ...     .having_citation_threshold(0)
    ...     .having_occurrence_threshold(2)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering_algorithm_or_dict("louvain")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> df.head()  # doctest: +NORMALIZE_WHITESPACE
                                                       0  ...                                                  3
    0  Arner DW, 2020, EUR BUS ORGAN LAW RE, V21, P7,...  ...  Anagnostopoulos I, 2018, J ECON BUS, V100, P7,...
    1  Sangwan V, 2019, STUD ECON FINANC, V37, P71, D...  ...  Muganyi T, 2022, FINANC INNOV, V8, DOI 10.1186...
    2  Arner DW, 2019, EUR BUS ORGAN LAW RE, V20, P55...  ...  Chao X, 2022, INT REV FINANC ANAL, V80, DOI 10...
    3  Nasir A, 2021, APPL SCI-BASEL, V11, DOI 10.339...  ...
    4  Buckley RP, 2020, J BANK REGUL, V21, P26, DOI ...  ...
    <BLANKLINE>
    [5 rows x 4 columns]


    >>> df = (
    ...     ItemsByCluster()
    ...     #
    ...     # UNIT OF ANALYSIS:
    ...     .with_citation_unit(CitationUnit.DOC)
    ...     .having_items_in_top(30)
    ...     .having_citation_threshold(0)
    ...     .having_occurrence_threshold(2)
    ...     .having_items_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(False)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering_algorithm_or_dict("louvain")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> df.head()  # doctest: +NORMALIZE_WHITESPACE
                                                       0  ...                                                  3
    0  Arner DW, 2020, EUR BUS ORGAN LAW RE, V21, P7,...  ...  Anagnostopoulos I, 2018, J ECON BUS, V100, P7,...
    1  Sangwan V, 2019, STUD ECON FINANC, V37, P71, D...  ...  Muganyi T, 2022, FINANC INNOV, V8, DOI 10.1186...
    2  Arner DW, 2019, EUR BUS ORGAN LAW RE, V20, P55...  ...  Chao X, 2022, INT REV FINANC ANAL, V80, DOI 10...
    3  Nasir A, 2021, APPL SCI-BASEL, V11, DOI 10.339...  ...
    4  Buckley RP, 2020, J BANK REGUL, V21, P26, DOI ...  ...
    <BLANKLINE>
    [5 rows x 4 columns]


    >>> df = (
    ...     ItemsByCluster()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_citation_unit(CitationUnit.AUTH)
    ...     .having_items_in_top(30)
    ...     .having_citation_threshold(0)
    ...     .having_occurrence_threshold(2)
    ...     .having_items_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering_algorithm_or_dict("louvain")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> df.head()  # doctest: +NORMALIZE_WHITESPACE
                                 0  ...                  4
    0             Xia YF 004:00008  ...    Li JY 002:00019
    1  Anagnostopoulos I 002:00284  ...  Maiti A 002:00019
    2        von Solms J 002:00029  ...
    3              Li DH 002:00005  ...
    4            Yang SJ 002:00005  ...
    <BLANKLINE>
    [5 rows x 5 columns]


    >>> df = (
    ...     ItemsByCluster()
    ...     #
    ...     # UNIT OF ANALYSIS:
    ...     .with_citation_unit(CitationUnit.AUTH)
    ...     .having_items_in_top(30)
    ...     .having_citation_threshold(0)
    ...     .having_occurrence_threshold(2)
    ...     .having_items_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(False)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering_algorithm_or_dict("louvain")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> df.head()  # doctest: +NORMALIZE_WHITESPACE
                       0            1             2            3        4
    0             Xia YF     Becker M   Zetzsche DA    Kshetri N    Li JY
    1  Anagnostopoulos I     Karim ME      Arner DW     Arsyad I  Maiti A
    2        von Solms J  Kunhibava S    Buckley RP  Kharisma DB
    3              Li DH    Muneeza A  Miglionico A     Wiwoho J
    4            Yang SJ   Mustapha Z


"""

from tm2p import CitationUnit, ItemOrderBy
from tm2p._intern import ParamsMixin
from tm2p.synthes.netw.cit._intern.doc import (
    ItemsByClusterDataFrame as DocItemsByClusterDataFrame,
)
from tm2p.synthes.netw.cit._intern.other import (
    ItemsByClusterDataFrame as OtherItemsByClusterDataFrame,
)


class ItemsByCluster(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        if self.params.citation_unit == CitationUnit.DOC:
            ItemsByCluster = DocItemsByClusterDataFrame
        else:
            ItemsByCluster = OtherItemsByClusterDataFrame

        return (
            ItemsByCluster()
            .update(**self.params.__dict__)
            .update(items_order_by=ItemOrderBy.OCC)
            .run()
        )
