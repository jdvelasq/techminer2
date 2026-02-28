"""
Matrix
===============================================================================

Smoke tests:
    >>> from tm2p import ItemsOrderBy
    >>> from tm2p.discov.occur_matrix.auth.authkw import Matrix
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
    columns                            Jagtiani J. 005:01156  ...  Kauffman R.J. 002:01445
    rows                                                      ...
    fintech 117:25478                                      5  ...                        0
    financial inclusion 017:03823                          0  ...                        0
    financial technology 014:02508                         0  ...                        0
    green finance 011:02844                                0  ...                        0
    blockchain 011:02023                                   1  ...                        0
    banking 010:02599                                      0  ...                        0
    china 009:01947                                        1  ...                        0
    innovation 009:01703                                   0  ...                        0
    artificial intelligence 008:01915                      0  ...                        0
    financial services 007:01673                           0  ...                        0
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
