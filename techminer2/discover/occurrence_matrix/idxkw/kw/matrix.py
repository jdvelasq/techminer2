"""
Matrix
===============================================================================

Smoke tests:
    >>> from techminer2 import ItemsOrderBy
    >>> from techminer2.discover.occurrence_matrix.idxkw.kw import Matrix
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
    columns                            finance 028:07080  ...  commerce 006:02013
    rows                                                  ...
    fintech 119:26148                                 16  ...                   4
    finance 029:07137                                 28  ...                   4
    innovation 020:03916                               8  ...                   1
    china 018:03596                                    7  ...                   0
    financial inclusion 017:03823                      2  ...                   1
    financial technology 015:02583                     2  ...                   0
    sustainable development 015:02158                  8  ...                   1
    banking 013:03043                                  1  ...                   0
    sustainability 013:02308                           5  ...                   1
    blockchain 012:03450                               3  ...                   2
    <BLANKLINE>
    [10 rows x 10 columns]


"""

from techminer2._internals import ParamsMixin

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
