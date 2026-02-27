"""
MatrixList
===============================================================================

Smoke tests:
    >>> from techminer2 import CorpusField, ItemsOrderBy
    >>> from techminer2.discover.occurrence_matrix.ctry.org import MatrixList
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
                                               rows        columns  OCC
    0    SOUTHWEST UNIV FINANC ECON [CHN] 008:02269  CHN 045:09715    8
    1                      UNIV ZÜR [CHE] 007:00971  CHE 008:01458    7
    2         FED RESERV BANK PHILA [USA] 005:01156  USA 031:09562    5
    3                   PEKING UNIV [CHN] 004:00576  CHN 045:09715    4
    4            ADAM SMITH BUS SCH [GBR] 003:00398  GBR 033:06802    3
    5                HENLEY BUS SCH [GBR] 003:00605  GBR 033:06802    3
    6               HORIZ UNIV COLL [ARE] 003:00254  CHN 045:09715    3
    7  MAX PLANCK INST INNOV COMPET [DEU] 003:00904  DEU 013:05295    3
    8                 SHANGHAI UNIV [CHN] 003:00911  CHN 045:09715    3
    9                 SOONGSIL UNIV [KOR] 003:00377  KOR 011:02378    3


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
