"""
Matrix
===============================================================================

Smoke tests:
    >>> from tm2p import ItemsOrderBy
    >>> from tm2p.discov.occur_matrix.ctry.idxkw import Matrix
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
    columns                            CHN 045:09715  ...  ITA 008:01041
    rows                                              ...
    finance 028:07080                             15  ...              0
    fintech 024:05279                              7  ...              1
    sustainable development 017:02470             11  ...              2
    innovation 014:02604                           7  ...              0
    china 010:02031                                9  ...              1
    sustainability 010:01546                       5  ...              1
    economic development 008:02384                 5  ...              0
    financial service 007:02627                    1  ...              0
    blockchain 006:02515                           2  ...              0
    commerce 006:02013                             2  ...              0
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
