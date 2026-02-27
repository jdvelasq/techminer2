"""
Matrix
===============================================================================

Smoke tests:
    >>> from techminer2 import ItemsOrderBy
    >>> from techminer2.discover.occurrence_matrix.authkw_x_idxkw import Matrix
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
    columns                            fintech 117:25478  ...  financial services 007:01673
    rows                                                  ...
    finance 028:07080                                 15  ...                             1
    fintech 024:05279                                 22  ...                             1
    sustainable development 017:02470                  7  ...                             0
    innovation 014:02604                              11  ...                             0
    china 010:02031                                    6  ...                             0
    sustainability 010:01546                           7  ...                             0
    economic development 008:02384                     5  ...                             0
    financial service 007:02627                        4  ...                             1
    blockchain 006:02515                               4  ...                             0
    commerce 006:02013                                 3  ...                             0
    <BLANKLINE>
    [10 rows x 10 columns]

"""

from techminer2 import CorpusField
from techminer2._internals import ParamsMixin

from .._internals import Matrix as BaseMatrix


class Matrix(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        return (
            BaseMatrix()
            .with_params(self.params)
            .with_column_field(CorpusField.AUTHKW_NORM)
            .with_index_field(CorpusField.IDXKW_NORM)
            .run()
        )
