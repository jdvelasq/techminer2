"""
Matrix
===============================================================================

Smoke tests:
    >>> from tm2p import ItemsOrderBy
    >>> from tm2p.discov.occur_matrix.authkw.concept import Matrix
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
    columns                         fintech 117:25478  ...  financial services 007:01673
    rows                                               ...
    fintech 155:33245                             117  ...                             7
    financial technology 051:09258                 31  ...                             3
    finance 050:10972                              28  ...                             1
    innovation 033:07734                           21  ...                             3
    china 033:06419                                20  ...                             0
    financial services 030:06887                   20  ...                             7
    banks 029:06252                                22  ...                             2
    technology 028:05172                           16  ...                             2
    the development 026:05689                      19  ...                             2
    banking 025:04664                              15  ...                             4
    <BLANKLINE>
    [10 rows x 10 columns]


"""

from tm2p._intern import ParamsMixin

from ..._intern import Matrix as BaseMatrix
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
