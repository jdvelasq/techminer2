"""
MatrixList
===============================================================================

Smoke tests:
    >>> from techminer2 import CorpusField, ItemsOrderBy
    >>> from techminer2.discover.occurrence_matrix.ctry_x_src import MatrixList
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
    0         RESOUR POLIC 007:01074  CHN 045:09715    6
    1         FINANC INNOV 005:00877  CHN 045:09715    3
    2  INT REV FINANC ANAL 005:00992  CHN 045:09715    3
    3  INT REV FINANC ANAL 005:00992  GBR 033:06802    3
    4             BUS ECON 002:00748  DEU 013:05295    2
    5             BUS ECON 002:00748  FRA 011:02475    2
    6   ENV SCI POLLUT RES 002:00387  CHN 045:09715    2
    7         EUR J FINANC 004:01002  CHN 045:09715    2
    8         EUR J FINANC 004:01002  GBR 033:06802    2
    9         FINANC MANAG 002:00376  USA 031:09562    2




"""

from techminer2 import CorpusField
from techminer2._internals import ParamsMixin

from .._internals import MatrixList as BaseMatrixList


class MatrixList(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        return (
            BaseMatrixList()
            .with_params(self.params)
            .with_column_field(CorpusField.CTRY_ISO3)
            .with_index_field(CorpusField.SRC_ISO4_NORM)
            .run()
        )
