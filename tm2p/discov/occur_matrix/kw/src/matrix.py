"""
Matrix
===============================================================================

Smoke tests:
    >>> from tm2p import ItemsOrderBy
    >>> from tm2p.discov.occur_matrix.kw.src import Matrix
    >>> df = (
    ...     Matrix()
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
    columns                                      fintech 119:26148  ...  blockchain 012:03450
    rows                                                            ...
    RESOUR POLIC 007:01074                                       5  ...                     0
    TECHNOL FORECAST SOC CHANG 006:01575                         6  ...                     1
    INT REV FINANC ANAL 005:00992                                3  ...                     0
    FINANC INNOV 005:00877                                       4  ...                     0
    EUR J FINANC 004:01002                                       4  ...                     0
    SUSTAIN (SWITZERLAND) 004:00741                              3  ...                     0
    RES INT BUS FINANC 004:00530                                 4  ...                     1
    IND MANAG DATA SYST 003:01154                                3  ...                     0
    J ECON BUS 003:00886                                         3  ...                     0
    J OPEN INNOV TECHNOL MARK COMPLEX 003:00477                  2  ...                     0
    <BLANKLINE>
    [10 rows x 10 columns]


"""

from tm2p._internals import ParamsMixin

from ..._internals import Matrix as BaseMatrix
from .._column import COLUMN_FIELD
from ._index import INDEX_FIELD

# how to read the name of the folder where is the current file


class Matrix(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        return (
            BaseMatrix()
            .with_params(self.params)
            .with_column_field(COLUMN_FIELD)
            .with_index_field(INDEX_FIELD)
            .run()
        )
