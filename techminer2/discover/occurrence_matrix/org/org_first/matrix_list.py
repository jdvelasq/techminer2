"""
MatrixList
===============================================================================

Smoke tests:
    >>> from techminer2 import CorpusField, ItemsOrderBy
    >>> from techminer2.discover.occurrence_matrix.org.org_first import MatrixList
    >>> df = (
    ...     MatrixList()
    ...     #
    ...     # COLUMNS:
    ...     .having_column_items_in_top(10)
    ...     .having_column_items_ordered_by(ItemsOrderBy.OCC)
    ...     .having_column_item_occurrences_between(None, None)
    ...     .having_column_item_citations_between(None, None)
    ...     .having_column_items_in(None)
    ...     #
    ...     # ROWS:
    ...     .having_index_items_in_top(None)
    ...     .having_index_items_ordered_by(ItemsOrderBy.OCC)
    ...     .having_index_item_occurrences_between(2, None)
    ...     .having_index_item_citations_between(None, None)
    ...     .having_index_items_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_item_counters(True)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/fintech/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> type(df).__name__
    'DataFrame'
    >>> df.shape[0] > 1
    True
    >>> df.shape[1] > 1
    True
    >>> df.head(10)
                                             rows  ... OCC
    0  SOUTHWEST UNIV FINANC ECON [CHN] 005:01236  ...   8
    1                    UNIV ZÜR [CHE] 005:00659  ...   6
    2              UNIV HONG KONG [HKG] 002:00380  ...   4
    3                             [N/A] 004:00192  ...   4
    4       FED RESERV BANK PHILA [USA] 003:00682  ...   3
    5         XI'AN JIAOTONG UNIV [CHN] 003:00689  ...   3
    6             CHANDIGARH UNIV [IND] 002:00183  ...   2
    7               IMP COLL LOND [GBR] 002:00474  ...   2
    8                   LATV UNIV [LVA] 002:00273  ...   2
    9               SHANGHAI UNIV [CHN] 002:00656  ...   2
    <BLANKLINE>
    [10 rows x 3 columns]


"""

from techminer2._internals import ParamsMixin

from ..._internals import MatrixList as BaseMatrixList
from .._column import COLUMN_FIELD
from ._index import INDEX_FIELD


class MatrixList(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        return (
            BaseMatrixList()
            .with_params(self.params)
            .with_column_field(COLUMN_FIELD)
            .with_index_field(INDEX_FIELD)
            .run()
        )
