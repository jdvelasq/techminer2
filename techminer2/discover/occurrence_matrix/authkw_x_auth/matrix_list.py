"""
MatrixList
===============================================================================

Smoke tests:
    >>> from techminer2 import CorpusField, ItemsOrderBy
    >>> from techminer2.discover.occurrence_matrix.authkw_x_auth import MatrixList
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
                          rows            columns  OCC
    0    Jagtiani J. 005:01156  fintech 117:25478    5
    1      Dolata M. 003:00330  fintech 117:25478    3
    2      Hornuf L. 003:00904  fintech 117:25478    3
    3          Li X. 003:00894  fintech 117:25478    3
    4     Schwabe G. 003:00330  fintech 117:25478    3
    5  Zavolokina L. 003:00330  fintech 117:25478    3
    6   Al-Okaily M. 002:00191  fintech 117:25478    2
    7  Al-Sartawi A. 002:00274  fintech 117:25478    2
    8       Allen F. 002:00474  fintech 117:25478    2
    9     Arner D.W. 003:00911  fintech 117:25478    2


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
            .with_column_field(CorpusField.AUTHKW_NORM)
            .with_index_field(CorpusField.AUTH_NORM)
            .run()
        )
